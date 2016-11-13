#!/usr/bin/env python3

import sqlite3
from datetime import date

#Quantities dict
quantities_dict = {"ml":0,
                   "l":1,
                   "cup":2,
                   "g":3,
                   "lb":4,
                   "kg":5,
                   "count":6}


# Connect to database


conn = sqlite3.connect("db.db")
c = conn.cursor()

response = ""

while "exit" not in response or "quit" not in response:
    print("***** DB Entry *****")
    print("Choose from the following options:")
    print("1. Add something you have in the fridge")
    print("2. Add a recipe")
    response = input("Choose an option (1 or 2):  ")
    response_val = int(response)
    if response_val == 1:
        item_name = input("Enter the name of the item:  ")
        item_qty = input("Enter how much of the item you have:  ")
        print("What measurement of quantity?\nPress Enter if there is no measurement, and its just a count.")
        print("0. mL")
        print("1. L")
        print("2. Cup")
        print("3. Teaspoon")
        print("4. Tablespoon")
        print("5. Pound")
        print("6. Ounce")
        print("7. Gram")
        print("8. Milligram")
        print("9. Kilogram")
        item_qty_type = input("Enter your selection:  ")
        if item_qty_type == "":
            item_qty_type = 10
        else:
            item_qty_type = int(item_qty_type)

        item_expiry = input("Enter the date of expiry (DD-MM-YYYY). Hit Enter if there is no
        expiry date (eg. flour):  ")


        # Begin writing data to the Fridge table
        if item_expiry == "":
            item_expiry = "NULL"

        c.execute("INSERT INTO Fridge VALUES(


