#!/usr/bin/env python

import sqlite3


conn = sqlite3.connect("db.db")
conn2 = sqlite3.connect("db.db")
c2 = conn2.cursor()
c = conn.cursor()

# Get prep time preferences from user
time_pref = input("How long do you want to spend prepping (minutes)?:  ")
cook_pref = input("How long do you want to spend cooking (Minutes)?:   ")



a = c.execute("SELECT * FROM Fridge")

fridge_table = []

for row in a:
    fridge_table.append(row)


b = c.execute("SELECT * FROM RecipeFile WHERE prepTime <= {} AND cookTime <= {}".format(time_pref, cook_pref))

recipe_table = []
for row in b:
    recipe_table.append(row)


print (fridge_table)
print (recipe_table)

ingredients_i_have = []
for indice in fridge_table:
    ingredients_i_have.append(indice[0])

print(ingredients_i_have)

print(fridge_table[1][1])

