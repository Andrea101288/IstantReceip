from manager import Manager
import settings
# Create a new instance of db manager
manager = Manager(settings.host,
                  settings.username,
                  settings.passwd,
                  settings.database,
                  settings.charset)
manager.connect()

for ingredient in manager.select("ingredient" , "id, name"):
    
    a = manager.search_set_ingredient(ingredient[1][:len(ingredient[1])-2].replace("'", "''"))
    if len(a) > 1:
        fileOut = open("subCategories\\" + ingredient[1] + ".txt", "w")
        for ing in a:
            fileOut.write(ing[0] + "\n")
manager.close()