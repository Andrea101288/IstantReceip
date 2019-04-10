from manager import Manager
import settings

# get datas from txt file to save receips data
file = open("ricette.txt", "r") 
 
findI = False
findMI = False 

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
for line in file: 
    if "-Ingredienti" in line:
        findI = True
        ++i
        continue
    if "-Preparazione" in line:
        findI = False
        continue
    if findI:
        ingredient = line.split("= ")[1].replace("\n", "")
        amount = line.split(" =")[0]
        if ":" in ingredient:
            continue
        # Insert the new ingredient in the database
        ing = manager.ingredientByName(ingredient)
        manager.insert_Receip_ingredient(ing[0], i, amount, "False")
        continue
                
    if "-Ing_Principale" in line:
        findMI = True
        continue
    if findMI:
        mainIng = line.replace("\n", "")
        # Insert the new ingredient in the database
        ing = manager.ingredientByName(mainIng)
        #print(ing[0])
        manager.insert_Receip_ingredient(ing[0], i, "", "False")
        findMI = False
    if i%1000: 
      time.sleep(2)    
    
print("DONE")
             
manager.close()  
file.close()