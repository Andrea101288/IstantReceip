from manager import Manager
import settings
import time

# get datas from txt file to save receips data
file = open("IngEnGoogle.txt", "r") 
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
    
    ingredient = line.replace("\n", "")
    if  (not manager.contain_ingredient(ingredient)):        
    # if(ingredient not in stringa):
       # stringa = stringa + ingredient + "| "
       #Insert the new event in the database
       manager.insert_ingredient(ingredient, "", 0)
        
print("DONEEEEEEEEEEEEEEE")
# count = 0
# for s in stringa.split("| "):
    # count += len(s)
    # if count > 25000:
        # count = len(s)
        # i+=1
        # file2 = open("IngEn"+str(i)+".txt", "w")
    # file2.write(s+"\n")
# # for ing in ingTrad.split("\n"):
    # # manager.update("ingredient", "name_en = " + ing + " where id = " + str(i)) 
    # # i = i + 1
             
manager.close()  
file.close()
file2.close