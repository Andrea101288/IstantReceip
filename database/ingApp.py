from database.manager import Manager
from database import settings

# Create a new instance of db manager
manager = Manager(settings.host,
                  settings.username,
                  settings.passwd,
                  settings.database,
                  settings.charset)
manager.connect()

for ingredient in manager.select("ingredient", "id, name"):
    
    a = manager.search_set_ingredient(ingredient[1][:len(ingredient[1])-2].replace("'", "''"))
    if len(a) > 1:
        file_out = open("subCategories\\" + ingredient[1] + ".txt", "w")
        for ing in a:
            file_out.write(ing[0] + "\n")
manager.close()