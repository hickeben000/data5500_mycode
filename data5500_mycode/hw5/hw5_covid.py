
import cloudscraper 
import json 
from collections import defaultdict 
from datetime import datetime
import pandas as pd 
import os

states = pd.read_csv("/home/ubuntu/data5500_mycode/hw5/states.txt")

print("Covid confirmed cases statistics")

for state in states["States:"]: 
    
    print("State name: ", state.upper())

    scraper = cloudscraper.create_scraper()
    url = "https://api.covidtracking.com/v1/states/"+ state + "/daily.json"
    response = scraper.get(url)
    data = response.json()

    # find the keys needed and save them as variables 
    daily_cc = "positiveIncrease"
    day = "date"

    # counter to later find average
    days = 0 
    # sum values to variable to later find average
    total_pos_inc = 0 
    # variable to hold most recent date
    rec_date = 0
    # variable to track most recent date (stops interating once most recent date is found)
    recent = 0

    # create a list that tracks months and years - if the key (month, year) doesn't exist it'll initialize a new one at zero. 
    monthly_sums = defaultdict(int)

    # loop through list of dictionaries 
    for dictionary in data:
        # sum all positive increases in cases for all days(dictionaries)
        total_pos_inc += dictionary[daily_cc]
        days += 1

        # Most recent date with no new cases
        if dictionary[daily_cc] == 0 and recent == 0:
            rec_date = dictionary[day]
            recent = 1

        # convert date into datetime object so python can interpret it
        date_obj = datetime.strptime(str(dictionary[day]), "%Y%m%d")

        # use year month as key 
        key = (date_obj.year, date_obj.month)
        
        # add pos_inc for each day to key (python will sum appropriate months because of the keys est. in above lines of code and defaultdict)
        monthly_sums[key] += dictionary["positiveIncrease"]

        
    # find average of new daily confirmed cases and print
    average = total_pos_inc/ days 
    print("Average daily confirmed covid cases for "+ state.upper() +" are:", round(average, 2)) 

    ## Date with the highest new number of covid cases: 
    # max function goes through all dictionaries, finds highest positive inc
    max_score = max(data, key=lambda dict: dict[daily_cc])
    # converts to datetime object, formatted to month, day, year 
    date_obj_h = datetime.strptime(str(max_score[day]), "%Y%m%d")
    formatted_date_h = date_obj_h.strftime("%B %d, %Y")
    print("Date with the highest new number of covid cases:", formatted_date_h)

    ## Most recent date with no new covid cases, pulls variable from for loop
    # convert rec_date into datetime object then format date
    date_obj_r = datetime.strptime(str(rec_date), "%Y%m%d")
    formatted_date_r = date_obj_r.strftime("%B %d, %Y")
    print("Most recent date with no new covid cases:", formatted_date_r)

    ## Month and Year, with the highest new number of covid cases
    # key is a temporary placeholder for data as max() loops through it
    max_month = max(monthly_sums, key=lambda key: monthly_sums[key])
    year, month = max_month  # unpack the tuple
    date_obj_max = datetime(year, month, 1)  # create dummy date - first day of month
    formatted_date_max = date_obj_max.strftime("%B %Y") # only get month and year of dummy date
    print("Month and Year, with the highest new number of covid cases: "+ formatted_date_max +" with "+ str(monthly_sums[max_month]),"cases") 

    ## Month and Year, with the lowest new number of covid cases
    # use min() function to loop through month_sums dictionary to find lowest value
    min_month = min(monthly_sums, key=lambda key: monthly_sums[key]) 
    year, month = min_month # unpack tuple
    date_obj_min = datetime(year, month, 1) # create dummy date - first day of month
    formatted_date_min = date_obj_min.strftime("%B, %Y") # only get month and year of dummy date
    print("Month and Year, with the lowest new number of covid cases: "+ formatted_date_min +" with "+ str(monthly_sums[min_month]),"cases")

    # build dictionary to save data into json files
    state_data = {
        "state name:": state.upper(),
        "average_daily_cases": round(average, 2),
        "highest_case_date": formatted_date_h,
        "most_recent_no_case_date": formatted_date_r,
        "highest_case_month":{"month_year": formatted_date_max, "cases": monthly_sums[max_month]},
        "lowest_case_month":{"month_year": formatted_date_min, "cases":monthly_sums[min_month]}
    }

    # indicates the folder I want to put dictionaries in and dumps dictionaries into files
    folder = "state_json_files"
    with open(f"{folder}/{state.upper()}.json", "w") as f:
        json.dump(state_data, f, indent=4) 
