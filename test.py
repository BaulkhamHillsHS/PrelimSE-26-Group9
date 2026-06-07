import time
import csv
import os

profileList = []
currentProfile = []
multiCurrentProfiles = []

os.system('cls' if os.name == "nt" else 'reset')

details = input("enter account and pwd ").split()
if len(details) != 2:
    print("bro who u fooling")
else:
    name = details[0].strip()
    pwd = details[1].strip()
    ##profile = input("which profile are you accessing? ").strip()
    with open("data.csv", "r") as csv_file:
        data = csv.reader(csv_file)
        for row in data:
            if row[0] == name and row[2] == pwd:
                multiCurrentProfiles.append(row[4])
    try:
        if len(profileList) >= 2:
            print(f"There are {len(profileList)} profiles: {profileList}. Which will you access?")

        else:
            currentProfile = profileList
            print(f"Logging in as {currentProfile[4]}")
    except NameError:
        print("not found")
