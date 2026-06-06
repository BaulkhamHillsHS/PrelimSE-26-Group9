import time
import csv
import os

os.system('cls' if os.name == "nt" else 'reset')

poop = input("enter account and pwd ").split()
if len(poop) != 2:
    print("bro who u fooling")
else:
    name = poop[0].strip()
    pwd = poop[1].strip()
    profile = input("which profile are you accessing? ").strip()
    with open("banana.csv", "r") as csv_file:
        banana = csv.reader(csv_file)
        for row in banana:
            if row[0] == name and row[4] == profile:
                currentProfile = row
                currentParent = name
                found = True
    try:
        print(f"Welcome, {currentProfile}")
    except NameError:
        print("not found")
