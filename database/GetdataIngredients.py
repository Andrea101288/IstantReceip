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
        continue
    if "-Preparazione" in line:
        findI = False
        continue
    if findI:
        ingredient = line.split("= ")[1].replace("\n", "")
        if ":" in ingredient:
            continue
        if  (not manager.contain_ingredient(ingredient)):
            # Insert the new event in the database
            manager.insert_ingredient(ingredient, 0)
        ++i
        if i%100: 
            time.sleep(1) 
        continue
                
    if "-Ing_Principale" in line:
        findMI = True
        continue
    if findMI:
        mainIng = line.replace("\n", "")
        if  (not manager.contain_ingredient(mainIng)):
            # Insert the new event in the database
            manager.insert_ingredient(mainIng, 0)
        findMI = False
    ++i
    if i%100: 
      time.sleep(1)    
    
print("DONE")
             
manager.close()  
file.close()