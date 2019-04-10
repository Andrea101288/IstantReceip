import mysql.connector as mysql


class Manager:
    """This class manages all the connection and operations on the ESN database"""

    def __init__(self, host, username, password, database, charset="UTF8"):
        """Constructor function"""
        # Get credentials to enstablish connection
        self.host = host
        self.username = username
        self.password = password
        self.database = database
        self.charset = charset

        # Database stuff
        self.connection = None
        self.cursor = None

    def connect(self):
        """Connect to database"""
        self.connection = mysql.connect(host=self.host,
                                        user=self.username,
                                        password=self.password,
                                        database=self.database)
        self.cursor = self.connection.cursor()

    def close(self):
        """Closes the connection to the database"""
        self.cursor.close()
        self.connection.close()
        
    def insert_receip(self, name, description):
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
            
    def insert_ingredient(self, name, calories):
        """Insert events in the database"""
        # Connect to DB
        self.connect()
        try:
            # Prepare query                     
            query = "INSERT INTO ingredient VALUES({0}, '{1}', {2})".format(0, name,  calories)
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
            
    def insert_Receip_ingredient(self, idIng, idRec, amount, mainIng):
        """Insert events in the database"""
        # Connect to DB
        self.connect()
        try:
            # Prepare query                     
            query = "INSERT INTO receiptingredients VALUES({0}, {1}, {2}, '{3}', {4})".format(0, idIng,  idRec, amount, mainIng)
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