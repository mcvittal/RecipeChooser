#!/usr/bin/env python

import sqlite3

def clean_singleresult(result):
    tmp = []
    for row in result:
        tmp.append(row)
    tmp2 = []
    for row in tmp:
        tmp2.append(row[0])
    return tmp2

conn = sqlite3.connect("db.db")
conn2 = sqlite3.connect("db.db")
c2 = conn2.cursor()
c = conn.cursor()

# Get prep time preferences from user
#time_pref = input("How long do you want to spend prepping (minutes)?:  ")
#cook_pref = input("How long do you want to spend cooking (Minutes)?:   ")


a = c.execute("SELECT * FROM Fridge")

fridge_table = []

for row in a:
    fridge_table.append(row)


b = c.execute("SELECT recipeID, recipeName FROM RecipeFile")

recipe_table = {}

a = []
# Put the recipe ID's that fit time criteria into a 1D list
for row in b:
    a.append(row)
print("asdfjkdjfkdjfkjsdfjsd")
print(a)
for row in a:
    recipe_table[row[0]] = row[1]

print(recipe_table)

for a_recipeID in recipe_table.keys():
    result = c.execute("SELECT ingredientID, qty, qtyType FROM Ingredients WHERE recipeID =={}".format(a_recipeID))
    ingredients_needed = []
    for row in result:
        ingredients_needed.append(row)
    
    can_make = True
    for ingredient in ingredients_needed:
        fridge_items = c.execute("SELECT ingredientID, qty, qtyType FROM Fridge WHERE ingredientID == {}".format(ingredient[0]))
        exists = 0
        for row in fridge_items:
            exists += 1
        if exists == 0:
            #print("no food for you")
            can_make = False
            break
        else:
            pass
            #print("got it!")
    if can_make:
        print("You can make {}".format(recipe_table[a_recipeID]))


ingredients_i_have = []
for indice in fridge_table:
    ingredients_i_have.append(indice[0])


print(ingredients_i_have)

#print(fridge_table[1][1])

