from DeckOfCards import *

# use class code to create the object that contains a list of the deck of cards from the class DeckOfCards
deck = DeckOfCards()    # telling python to use the blueprint in DeckOfCards class to create an object and the object contains a emplty list soon to be filled by the nested for loops.

# function to play the game 
def play():
    #shuffle and print the decks
    deck.print_deck()
    deck.shuffle_deck()
    deck.print_deck()

    # welcome user to game
    print("Welcome, get stocked, this is blackjack!")

    # deal two cards to the user
    card = deck.get_card() # deck.get_card is a function that returns an object
    card2 = deck.get_card()
    # (calling on the deckOfCards object (created from the class DeckOfCards) to get the first two values in the deck list).

    # variable for if both user and dealer bust, dealer wins 
    ubust = 0
    # variable to evaluate scores if no one busted 
    endGame = 0

    # initiate scores and ace variables, ace to keep track of aces
    score = 0
    scoreDealer = 0
    ace = 0 
    aceD = 0 

    # calculate the user's hand score and track for aces
    score += card.val
    if card.face == 'Ace':
        ace +=1 

    score += card2.val
    if card2.face == 'Ace':
        ace += 1
    print("Your score is: ", score)

    # ask user to hit
    hit = input("would you like a hit? y/n ")

    # if yes, get new card from list and recalculate score
    while hit == 'y':
        card3 = deck.get_card()
        score += card3.val
        # tracks aces
        if card3.face == 'Ace':
            ace += 1 
        print("You drew a", card3)
        # less than 21 ask if they want another hit
        if score <= 21:
            print("Your new score: ", score)
            hit = input("Would you like another hit? y/n ")
        # if they bust and have an ace subtrack score by 10
        if score > 21 and ace != 0:
            print("uh oh over 21.")
            score = score - 10
            ace = 0 
            print("But you had an ace. Your new score: ", score)
            hit = input("Would you like another hit? y/n ")
        if score > 21:  
            print("Your new score:",score,"(over 21). You lose.")
            ubust = 1
            endGame = 1
            hit = 'n'
            break

    # DEALER
    # deal two cards to the dealer 
    # don't have to keep track of where the list you are because it's coming from an object.
    card = deck.get_card() # deck.get_card is a function that returns an object
    card2 = deck.get_card()

    # calculate dealer score and track aces 
    scoreDealer += card.val
    if card.face == 'Ace':
        ace += 1

    scoreDealer += card2.val
    if card2.face == 'Ace':
        ace += 1

    # hit whenever dealers score is less than 17 
    while scoreDealer < 17:
        card3 = deck.get_card()
        scoreDealer += card3.val
        if card2.face == 'Ace':
            ace += 1

        if scoreDealer > 21:
            # account for potential aces
            if aceD != 0:
                scoreDealer = scoreDealer - 10
            # if dealer busted and user didn't
            elif ubust == 0:
                print("The dealer busted, you WIN!")
                endGame = 1 

    x = 21
    # if no one busted evaluate the scores
    if endGame == 0:
        if (x - score) > (x - scoreDealer):
            print("The dealer is closer to 21. You lost.")
        if (x - score) < (x - scoreDealer):
            print("You're closer to 21! You won!")
        if (score - x) == (scoreDealer - x):
            print("The tie goes to the dealer. You lost.")

   

play()

# ask to play again
again = input("Do you want to play again? y/n ")
# however long user says to play again, play again
while again == 'y':
    play()
    again = input("Do you want to play again? y/n ")
else:
    print("Ok, see you later.")
