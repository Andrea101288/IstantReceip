import json
from flask import Flask, request
from flask_restful import Resource, Api
import mysql.connector as mysql

from manager import Manager
import settings

class Receipt(Resource):
    """Manages events requests"""

    def get(self, ingredients):
        # Return value
        rv = []
        ingredientsAppId = []
        # Get ingredients from DB
        for ing in ingredients:
            id = manager.ingredientAppByName(ing)
            ingredientsAppId.append(id[0][0])
            
        ingredientsId = []
        for ing in ingredients:
            id = manager.select("ingredientapprel where idIngredientApp = " + ing, "idIngredient")
            ingredientsId = ingredientsId + id
        
    # ingredient = manager.select()

# Create new db manager
manager = Manager(settings.host,
                  settings.username,
                  settings.passwd,
                  settings.database,
                  settings.charset)

manager.connect()                 

# r = Receipt()    
# r.get(["Limoni", "Vanil Zucca"])

manager.close()