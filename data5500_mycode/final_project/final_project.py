from pycaret.classification import ClassificationExperiment, predict_model
import pandas as pd
import matplotlib
import os
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.metrics import accuracy_score
from sklearn.ensemble import RandomForestClassifier
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout
from tensorflow.keras.utils import to_categorical

curr_dir = os.path.dirname(__file__) # get the current directory of this file

# load training and test data
df = pd.read_csv(os.path.join(curr_dir,'data','train.csv'))
test_df = pd.read_csv(os.path.join(curr_dir,'data','test.csv'))

results_folder = os.path.join(curr_dir, "results")
os.makedirs(results_folder, exist_ok=True)  # create folder if it doesn't exist


# PYCARET MODELS
s = ClassificationExperiment() # sets up PyCaret experiment environment
# deals with categorical variables, train-test split, feature scaling, and more not necessary for this project
s.setup(df, target = 'type_of_attack', session_id = 124) 

# use cross-validation and find the best models
best = s.compare_models()

# combine folds into one and set as final model
final_model = s.finalize_model(best)

print("The best model:", best)

# use best model to make predictions on test data
predictions = s.predict_model(final_model, data=test_df)
predictions.to_csv(os.path.join(results_folder,'predictions.csv'), index=False)

# Feature importance analysis
original_cwd = os.getcwd()          # save current working directory
os.chdir(results_folder)             # temporarily change cwd
s.plot_model(final_model, plot='feature', save=True)
os.chdir(original_cwd)              # return to original cwd


# NEURAL NETWORKS
# parent class
class NeuralNetwork:
    def __init__(self):
        self.model = None

    def train(self, X_train, y_train, epochs=30, batch_size=32, validation_data=None):
        return self.model.fit(
            X_train, y_train,
            epochs=epochs,
            batch_size=batch_size,
            validation_data=validation_data,
            verbose=1)

    def predict(self, X):
        return self.model.predict(X)

    def evaluate(self, X, y):
        return self.model.evaluate(X,y)

# Keras NN child class
class KerasNN(NeuralNetwork):
    def __init__(self, input_dim, output_dim):
        super().__init__()    # run the parent class before this NN version

        self.model = Sequential([
            # input layer: 256 neurons; randomly drops 30% of neurons during training to prevent overfitting, reduce reliance on one neuron = more robust
            Dense(256, activation='relu', input_dim=input_dim),
            Dropout(0.3),
            # layer 1: 128 neurons, Keras auto-infers shape
            Dense(128, activation='relu'),
            Dropout(0.3),
            # layer 2
            Dense(64, activation='relu'),
            Dropout(0.2),
            # output layer
            Dense(output_dim, activation='softmax')
        ])
        # compile model
        self.model.compile(
            optimizer="adam",
            loss="categorical_crossentropy",
            metrics=["accuracy"]
        )

# Random forest child class
class RandomForestModel(NeuralNetwork):
    def __init__(self, n_estimators=100, random_state=42):
        super().__init__()
        self.model = RandomForestClassifier(n_estimators=n_estimators, random_state=random_state)

    def train(self, X_train, y_train):
        self.model.fit(X_train, y_train)
        return self.model

    def evaluate(self, X, y):
        preds = self.model.predict(X)
        return accuracy_score(y, preds)

## PREDICT ON TRAINING DATA USING KERAS
# preprocessing 
categorical_cols = ['protocol_type','service','flag']

X = pd.get_dummies(
    df.drop("type_of_attack", axis=1),
    columns = categorical_cols,
    drop_first=False
)
y = df["type_of_attack"]

# convert target into one-hot vectors (dummy variables)
label_encoder = LabelEncoder()  # assings each attack a number
y_encoded = label_encoder.fit_transform(y)  # .fit() learns the mapping; transform converts target to numbers
# speaking notes: line above will have a for loop with if statments 
y_onehot = to_categorical(y_encoded)    # further converts labels to dummy matrix. 

# train / test split
X_train, X_val, y_train, y_val = train_test_split(
    X, y_onehot, test_size=0.2, random_state=45
)

# scale numeric features
numeric_cols = df.drop(["type_of_attack"] + categorical_cols, axis=1).columns
scaler = StandardScaler()
X[numeric_cols] = scaler.fit_transform(X[numeric_cols])

X_train[numeric_cols] = scaler.transform(X_train[numeric_cols])
X_val[numeric_cols] = scaler.transform(X_val[numeric_cols])


# create model using child class
input_dim = X_train.shape[1] # number of predictors
output_dim = y_onehot.shape[1] # number of classes 

nn_model = KerasNN(input_dim, output_dim)

# train using parent class (python looks for train in the child class; doesn't find it so it goes to parent)
history = nn_model.train(
    X_train, y_train,
    epochs=30,
    batch_size=32,
    validation_data=(X_val, y_val)
)

# evaluate using parent class
loss, accuracy = nn_model.evaluate(X_val, y_val)
print(f"Validation Accuracy: {accuracy:.4f}")

## PREDICT ON TEST DATA
# preprocessing 
test_df = pd.get_dummies(
    test_df,
    columns=categorical_cols,
    drop_first=False
)
# Align columns
test_df = test_df.reindex(columns=X.columns, fill_value=0)
test_df[numeric_cols] = scaler.transform(test_df[numeric_cols])
# predict using parent class
test_preds = nn_model.predict(test_df)
# convert predictions back to labels
pred_labels = label_encoder.inverse_transform(np.argmax(test_preds, axis=1))
# save predictions
pd.DataFrame({"type_of_attack": pred_labels}).to_csv(
    os.path.join(results_folder,"nn_predictions.csv"),
    index=False
)

## PREDICT ON TRAINING DATA USING RF MODEL (not implimenting to test data)
# preprocessing
X_train_rf, X_val_rf, y_train_rf, y_val_rf = train_test_split(
    X, y, test_size=0.2, random_state=42
)
# create instance
rf_model = RandomForestModel()
# train using child class
rf_model.train(X_train_rf, y_train_rf)
# predict using child class (keras using different evaluate method so have to overwrite in child class)
preds_rf = rf_model.predict(X_val_rf) 
# Evaluate
accuracy = rf_model.evaluate(X_val_rf, y_val_rf)
print("Random Forest Accuracy:", accuracy)
