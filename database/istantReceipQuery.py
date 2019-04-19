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

array = [34, 35, 11, 36, 37, 38, 39, 40, 41, 42]
a = manager.CheckIstantReceipIngredients(array)
print(a)
print("DONEEEEEEEEEEEEEEE")

             
manager.close()  
