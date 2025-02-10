import sqlite3, os.path, uuid


def create_table_users():
    if os.path.exists('./db/data.db'):
        return "Database exist"
    else:
        # Create table
        try:
            
            # Users 
            sqliteConnection = sqlite3.connect('./db/data.db')
            sqlite_create_table_query = '''CREATE TABLE IF NOT EXISTS users (
                                            id VARCHAR(255) PRIMARY KEY,
                                            username VARCHAR(255) NOT NULL,
                                            password VARCHAR(255) NOT NULL
                                            );'''
            cursor = sqliteConnection.cursor()
            print("Successfully Connected to SQLite")
            cursor.execute(sqlite_create_table_query)
            sqliteConnection.commit()
            print("SQLite table users created")
            
        except sqlite3.Error as error:
            print("Error while creating a sqlite table", error)
        finally:
            if sqliteConnection:
                sqliteConnection.close()
                print("sqlite connection is closed")
                
                
                    
def create_table_subscr():
    if os.path.exists('./db/data.db'):
        return "Database exist"
    else:
        # Create table
        try:
            # Subscriptions 
            sqliteConnection = sqlite3.connect('./db/data.db')
            sqlite_create_table_query = '''CREATE TABLE IF NOT EXISTS subscriptions (
                                            id VARCHAR(255) PRIMARY KEY,
                                            sbcrName VARCHAR(255) NOT NULL,
                                            sbcrtype VARCHAR(255) NOT NULL,
                                            sbcrperiod INTEGER NOT NULL,
                                            sbcrdescription VARCHAR(255) NOT NULL,
                                            sbcrdeeplink VARCHAR(255) NOT NULL,
                                            sbcrprice INTEGER NOT NULL
                                            );'''
            cursor = sqliteConnection.cursor()
            print("Successfully Connected to SQLite")
            cursor.execute(sqlite_create_table_query)
            sqliteConnection.commit()
            print("SQLite table subscriptions created")
            
        except sqlite3.Error as error:
            print("Error while creating a sqlite table", error)
        finally:
            if sqliteConnection:
                sqliteConnection.close()
                print("sqlite connection is closed")

                    

def insert_user(username, password):
    # Insert data
    try:
        sqliteConnection = sqlite3.connect('./db/data.db')
        cursor = sqliteConnection.cursor()
        print("Successfully Connected to SQLite")
        cursor.execute("INSERT INTO users VALUES ((?), (?))", (username, password, ) )
        sqliteConnection.commit()
        print("Data successfully inserted", cursor.rowcount)
        cursor.close()

    except sqlite3.Error as error:
        print("Error while inserting data in users", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print("sqlite connection is closed")
            
            
def insert_subscription(name, type, period, description, deeplink, price):
    # Insert data
    try:
        sqliteConnection = sqlite3.connect('./db/data.db')
        cursor = sqliteConnection.cursor()
        print("Successfully Connected to SQLite")
        statement = "INSERT INTO subscriptions VALUES ('%s', '%s', '%s', '%s', '%s', '%s', '%s')" % (str(uuid.uuid4()), name, type, period, description, deeplink, price)
        cursor.execute(statement)
        sqliteConnection.commit()
        print("Data successfully inserted", cursor.rowcount)
        cursor.close()

    except sqlite3.Error as error:
        print("Error while inserting data in subscription table", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print("sqlite connection is closed")
            

def get_subscription():
    elements = []
    data = []
    #Check data
    try:
        
        sqliteConnection = sqlite3.connect('./db/data.db')
        cursor = sqliteConnection.cursor()
        print("Successfully Connected to SQLite")
        cursor.execute("SELECT * FROM subscriptions")
        records = cursor.fetchall()
        # print(records)
        for row in records:
            elements.append(row[0])
            elements.append(row[1])
            elements.append(row[2])
            elements.append(row[3])
            elements.append(row[4])
            elements.append(row[5])
            elements.append(row[6])
            data.append(elements)
            elements = []   
        
        cursor.close()
        
        return data
    
    except sqlite3.Error as error:
        print("Error while getting data from subscriptions", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print("sqlite connection is closed")
            
