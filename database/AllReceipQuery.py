from manager import Manager
import settings
import time

# Create a new instance of db manager
manager = Manager(settings.host,
                  settings.username,
                  settings.passwd,
                  settings.database,
                  settings.charset)
manager.connect()

array = ["limone", "pasta", "pepe", "arancia"]
manager.CheckReceipIngredients(array)
print("DONEEEEEEEEEEEEEEE")

             
manager.close()  
