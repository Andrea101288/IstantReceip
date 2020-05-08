from manager import Manager
import settings 
import time

# get datas from txt file to save receips data
with open("IngEnGoogle.txt", "r") as file:  
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
            manager.insert_ingredient(ingredient, 0)
            
    print("Ingredients Inserting into DB Complete")
                
    manager.close()

