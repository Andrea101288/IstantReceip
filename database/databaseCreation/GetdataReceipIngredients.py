from database.manager import Manager
from database import settings
import time
import pdb

# get data from txt file to save receipes data
file = open("../receips.txt", "r")
 
find_ing = False
find_main_ing = False
change = False
ingredients = []

# Create a new instance of db manager
manager = Manager(settings.host,
                  settings.username,
                  settings.passwd,
                  settings.database,
                  settings.charset)
manager.connect()
i = 0

# seraching for the ingredient names and amount in the text file
for line in file.readlines():
    # pdb.set_trace()
    if "-Nome" in line:
        change = True
        continue

    if ":" in line:
        continue

    if "-Ing_Principale" in line:
        find_main_ing = True
        continue

    if find_main_ing:
        main_ing = line.strip()
        main_ing_id = manager.ingredientByName(main_ing)[0][0]

        print(f"main ing: {main_ing}")
        print(f"main ing id: {main_ing_id}")
        find_main_ing = False

    if "-Ingredienti" in line:
        find_ing = True
        change = False
        i = i + 1
        continue

    if "-Preparazione" in line:
        find_ing = False
        continue

    if find_ing:
        ingredient = line.split("= ")[1].replace("\n", "").strip()
        if "''" in ingredient:
            ingredient = ingredient.replace("''", "'")
        print(ingredient)
        amount = line.split(" =")[0]

        if not find_main_ing and not change:
            # Insert the new ingredient in the database
            print("ciao")
            ing = manager.ingredientByName(ingredient)[0][0]
            print(ing)
            print("inserting..")
            manager.insert_Receip_ingredient(ing, i, amount, main_ing_id)
            print("inserted")
            time.sleep(0.05)
        if ":" in ingredient:
            continue
print("DONE")
             
manager.close()  
file.close()