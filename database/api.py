import json
from flask import Flask, request
from flask_restful import Resource, Api
import mysql.connector as mysql

from manager import Manager
import settings

class Receips(Resource):
    """Manages events requests"""

    def get(self):
        # Return value
        rv = []
        receip = {}
        res = []
        rv = manager.select("receipt", "id, name")  
        for rec in rv:
            receip['id'] = rec[0]
            receip['name'] = rec[1]            
            res.append(receip.copy())
        return json.dumps(res)

class Ingredients(Resource):
    """Manages events requests"""

    def get(self):
        # Return value
        rv = []
        print(request.headers)
        rv = manager.select("ingredient", "id, name")   
        return json.dumps(rv)
    
    def post(self):
        # Return value
        rv = []
        rv = manager.select("ingredient", "id, name")   
        return json.dumps(rv)    

        
class IstantReceipSearch(Resource):
    """Manages events requests"""

    def get(self, ingredients):
        # Return value
        rv = []
        rv = manager.IstantReceipSearch(ingredients)   
        return json.dumps(rv)

class StandardReceipSearch(Resource):
    """Manages events requests"""

    def get(self, ingredients):
        # Return value
        rv = []
        rv = manager.ReceipSearch(ingredients)   
        return json.dumps(rv)


if __name__ == '__main__':
    # Init flask
    app = Flask(__name__)
    api = Api(app)

    PORT = 8080

    # Create new db manager
    manager = Manager(settings.host,
                      settings.username,
                      settings.passwd,
                      settings.database,
                      settings.charset)

    # Routes configuration
    api.add_resource(Ingredients, '/ingredients/')
    api.add_resource(Receips, '/receips/')
    api.add_resource(IstantReceipSearch,'/istantReceipSerch/')
    api.add_resource(StandardReceipSearch,'/standardReceipSerch/')
    
    try:
        # Connect to DB
        manager.connect()

        # Start API
        app.run(host='192.168.1.53', port=PORT)
    finally:
        manager.close()
