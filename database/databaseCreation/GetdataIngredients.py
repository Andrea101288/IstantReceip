from manager import Manager
import settings
import time
import goslate
import os 
gs = goslate.Goslate()

# get datas from txt file to save receips data
file_2 = open("../IngEn.txt", "w")
find_ingredient = False
string = "|"
ingredients = []
folder = os.listdir("../../")

# Create a new instance of db manager
manager = Manager(settings.host,
                  settings.username,
                  settings.passwd,
                  settings.database,
                  settings.charset)
manager.connect()

i = 0
for file in folder:
    file_2 = open("../"+file, "r") 
    for ingredient in file_2.readlines():
        manager.update("ingredient", "en_name = " + ingredient + " where id = " + str(i)) 
        i = i + 1
print("DONE")
             
manager.close()  
file.close()
