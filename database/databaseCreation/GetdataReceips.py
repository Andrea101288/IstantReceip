from database.manager import Manager
from database import settings
import time

fileNew = open("ReceipsNew.txt.txt", "r")

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
    manager.insert_receipe(name, description)
    ++i
    if i%100: 
        time.sleep(1)
        
print("DONE")
             
manager.close()    

