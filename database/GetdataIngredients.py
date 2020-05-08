from manager import Manager
import settings
import time
import goslate
gs = goslate.Goslate()

# get datas from txt file to save receips data
file = open("ricette.txt", "r") 
file_2 = open("IngEn.txt", "w") 
find_ingredient = False
string = "|"
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
        find_ingredient = True
        continue
    if "-Preparazione" in line:
        find_ingredient = False
        continue
    if find_ingredient:
        ingredient = line.split("= ")[1].replace("\n", "")
        if ":" in ingredient:
            continue
        #if  (not manager.contain_ingredient(ingredient)):         
        if("|"+ingredient+"|" not in string):
           string = string + ingredient + "|"
           #Insert the new event in the database
           # manager.insert_ingredient(ingredient, "", 0)
            

string = string.replace("''", "'")           
i = 1

count = 0
for s in string.split("|"):
    count += len(s)
    if count > 25000:
        count = len(s)
        i+=1
        file_2 = open("IngEn"+str(i)+".txt", "w")
    file_2.write(s+"\n")
# for ing in ingTrad.split("\n"):
    # manager.update("ingredient", "name_en = " + ing + " where id = " + str(i)) 
    # i = i + 1
print("DONE")
             
manager.close()  
file.close()
file_2.close