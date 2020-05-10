import mysql.connector as mysql


class Manager:
    """This class manages all the connection and operations on the database"""

    def __init__(self, host, username, password, database, charset="UTF8", auth='mysql_native_password', port=3306):
        """Constructor function"""
        # Get credentials to enstablish connection
        self.host = host
        self.username = username
        self.password = password
        self.database = database
        self.charset = charset
        self.auth = auth
        self.port = port

        # Database stuff
        self.connection = None
        self.cursor = None

    def connect(self):
        """Connect to database"""
        self.connection = mysql.connect(host=self.host,
                                        user=self.username,
                                        password=self.password,
                                        database=self.database,
                                        auth_plugin=self.auth)
        self.cursor = self.connection.cursor()

    def close(self):
        """Closes the connection to the database"""
        self.cursor.close()
        self.connection.close()
        
    def insert_receipe(self, name, description):
        """Insert events in the database"""
        # Connect to DB
        self.connect()
        try:
            # Prepare query                     
            query = "INSERT INTO receipt VALUES({0}, '{1}', '{2}')".format(0, name,  description)
            # Execute query
            self.cursor.execute(query)
            self.connection.commit()

        except mysql.Error as e:
            if e.errno == 1062:
                print("Entry '{0}' exists. Skipping".format(name))
            else:
                print("Unknown error! Exiting...")
                raise e
        finally:
            # Close connection
            self.close()
            
    def insert_ingredient(self, en_name, ingredient_name, calories):
        """Insert events in the database"""
        # Connect to DB
        self.connect()
        try:
            # Prepare query 
            query = "INSERT INTO ingredient VALUES({0}, '{1}', '{2}', '{3}')".format(0, ingredient_name, en_name, calories)
            # Execute query
            self.cursor.execute(query)
            self.connection.commit()

        except mysql.Error as e:
            if e.errno == 1062:
                print("Entry '{0}' exists. Skipping".format(ingredient_name))
            else:
                print("Unknown error! Exiting...")
                raise e
        finally:
            # Close connection
            self.close()
            
    def contain_ingredient(self, name):
        """Insert events in the database"""
        # Connect to DB
        self.connect()
        try:
            # Prepare query                     
            query = "select name from ingredient where name = '" + name + "'"
            # Execute query
            self.cursor.execute(query)
            return len(self.cursor.fetchall()) > 0
            
        finally:
            # Close connection
            self.close()
    
    def search_set_ingredient(self, name):
        """Insert events in the database"""
        # Connect to DB
        self.connect()
        try:
            # Prepare query                     
            query = "select name from ingredient where instr ( name , '"+ name +"')"
            # Execute query
            self.cursor.execute(query)
            return self.cursor.fetchall()
            
        finally:
            # Close connection
            self.close()
            
    def select(self, table, par):
        """Insert events in the database"""
        # Connect to DB
        self.connect()
        try:
            # Prepare query                     
            query = "select " + par + " from " + table 
            # Execute query
            self.cursor.execute(query)
            return self.cursor.fetchall()
            
        finally:
            # Close connection
            self.close()
    def ingredientByName(self, name):
        """Insert events in the database"""
        # Connect to DB
        self.connect()
        try:
            # Prepare query                     
            query = "select id from ingredient where name = '" + name + "'"
            # Execute query
            self.cursor.execute(query)
            return self.cursor.fetchall()            
        finally:
            # Close connection
            self.close()
            
    def insert_Receip_ingredient(self, id_ingredient, id_receipe, amount, name):
        """Insert events in the database"""
        # Connect to DB
        self.connect()
        try:
            # Prepare query                     
            query = "INSERT INTO receiptingredients VALUES({0}, {1}, {2}, '{3}')".format(0, id_ingredient,  id_receipe, amount)
            # Execute query
            self.cursor.execute(query)
            self.connection.commit()

        except mysql.Error as e:
            if e.errno == 1062:
                print("Entry '{0}' exists. Skipping".format(name))
            else:
                print("Unknown error! Exiting...")
                raise e
        finally:
            # Close connection
            self.close()            
    
    def ingredientAppByName(self, name):
        """Insert events in the database"""
        # Connect to DB
        self.connect()
        try:
            # Prepare query                     
            query = "select id from ingredientapp where name = '" + name + "'"
            # Execute query
            self.cursor.execute(query)
            return self.cursor.fetchall()            
        finally:
            # Close connection
            self.close()
            
    def update(self, table, par):
        """Insert events in the database"""
        # Connect to DB
        self.connect()
        try:
            # Prepare query                     
            query = "UPDATE "+ table + " SET " + par 
            
            # Execute query
            self.cursor.execute(query)
            return self.cursor.fetchall()
            
        finally:
            # Close connection
            self.close()   
    
    def IstantReceipSearch(self, ingredients):
        """Insert events in the database"""
        # Connect to DB
        self.connect()
        
        try:
            found_receipe = []
            query_receipe = "select distinct id_receipeeipt from receiptingredients where " 
            for ing in ingredients: 
                query_receipe +=  "id_ingredientredient = " + str(ing) + " or "
            
            query_receipe = query_receipe[:-4]
            print(query_receipe)
            self.cursor.execute(query_receipe)
            receips = self.cursor.fetchall()
            print(receips)
            
            for id_receipe in receips:            
                ok = True
                # Prepare query                     
                query = "select id_ingredientredient from receiptingredients where id_receipeeipt = " + str(id_receipe[0]) 
                # Execute query
                self.cursor.execute(query)
                result = self.cursor.fetchall()
                if len(ingredients) < len(result):
                    continue
                #print("receip" + str(id_receipe[0]))
                for ing in result:
                    #print(ing)
                    if not any(ing[0] == s for s in ingredients):
                    #if ing not in ingredients:
                        #print(ing)
                        ok = False
                        break
                if ok:
                    query_receipe = "select name from receipt where id = " + str(id_receipe[0])
                    self.cursor.execute(query_receipe)
                    final_result = self.cursor.fetchall()
                    found_receipe.append([final_result[0][0], id_receipe[0]])
                    print(found_receipe)
                    
            return found_receipe
            
        # except mysql.Error as e: 
            # print(e)
            # return [e, 0] 
            
        finally:
            # Close connection
            self.close()
            
    def ReceipSearch(self, ingredients):
        """Insert events in the database"""
        # Connect to DB
        self.connect()
        
        try:
            found_receipe = []
            query_receipe = "select distinct id_receipeeipt, name from receiptingredients where " 
            for ing in ingredients: 
                query_receipe +=  "id_ingredientredient = " + ing + " or "
            
            query_receipe = query_receipe[:-4]
            self.cursor.execute(query_receipe)
            receips = self.cursor.fetchall()
            
            for id_receipe in receips:            
                query_receipe = "select name from receips where id = " + id_receipe[0]
                self.cursor.execute(query_receipe)
                final_result = self.cursor.fetchall()
                found_receipe.append(final_result[0][0], id_receipe[0])
            
            return found_receipe
            
        except mysql.Error as e: 
            print(e[1])        
            return [e[1], 0] 
            
        finally:
            # Close connection
            self.close()