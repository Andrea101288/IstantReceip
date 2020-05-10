from database.manager import Manager
from database import settings
import time

fileNew = open("../ReceipsNew.txt", "r")

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
    time.sleep(0.05)
    i+=1

        
print(f"DONE, {i} receipes inserted")
             
manager.close()    

