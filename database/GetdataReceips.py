from manager import Manager
import settings
import time

# get datas from txt file to save receips data
#        file = open("ricette.txt", "r") 
#        fileOut = open("ricetteNew.txt", "w")
#                
        # seraching for the names in the text file
#        for riga in file:        
#            if "-Nome" in riga :
#                fileOut.write(next(file).split("\n")[0] + "&")
#                
#            if "-Preparazione" in riga:
#                fileOut.write(next(file).split("\n")[0] + "\n")
#            
#        file.close()
#        fileOut.close()

fileNew = open("ricetteNew.txt", "r") 

# Create a new instance of db manager
manager = Manager(settings.host,
                  settings.username,
                  settings.passwd,
                  settings.database,
                  settings.charset)
manager.connect()
i = 0
for line in fileNew:
    if "'" in line:
        line.replace("'", "''")
    name = line.split("&")[0]
    description = line.split("&")[1]
    
    # Insert the new event in the database
    manager.insert_receip(name,
                          description)
    ++i
    
    if i%100: 
        time.sleep(1)
        
print("DONE")
             
manager.close()    

