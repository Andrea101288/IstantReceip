from manager import Manager
import settings
import time
import goslate
gs = goslate.Goslate()

# get datas from txt file to save receips data
file = open("ricette.txt", "r") 
file2 = open("IngEn.txt", "w") 
findI = False
findMI = False 
stringa = ""
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
            stringa = stringa + ingredient + "\n"
            # Insert the new event in the database
            manager.insert_ingredient(ingredient, "", 0)
            
    i = i + 1
    if i%1000: 
      time.sleep(1)
      
ingTrad = gs.translate(stringa,'en')
i = 1
file2.write(stringa)
print("DONEEEEEEEEEEEEEEE")
for ing in ingTrad.split("\n"):
    manager.update("ingredient", "name_en = " + ing + " where id = " + str(i)) 
    i = i + 1
print("DONE")
             
manager.close()  
file.close()
file2.close