import mysql.connector
from mysql.connector import connection, errorcode

class MySQLTester:
    def __init__(self):
        self.username = "demo"
        self.password = "manage"
        self.host = "127.0.0.1"
        self.database = "vuc"
        self.config = { 'user': 'demo',
                        'password': 'manage',
                        'host': '127.0.0.1',
                        'database': 'vuc',
                        'raise_on_warnings': True
                        }        
    def test1(self):
        cnx = connection.MySQLConnection(user= self.username, 
                                        password= self.password,
                              host= self.host,
                              database= self.database)
        print("Connected to DB: %s" % self.database)
        cnx.close()

    def test2(self):
        try:
            cnx = connection.MySQLConnection(user= self.username, 
                              host= self.host,
                              database= self.database)
            print("Connected to DB: %s" % self.database)
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
                print(err)
        else:
            cnx.close()

    def test3(self):
        cnx = connection.MySQLConnection(**self.config)
        print("Connected to DB: %s" % self.config['database'])
        cursor = cnx.cursor()
        cursor.execute("SELECT VERSION()")
        for (item) in cursor:
            print("MySQL version is")
            print(item)
        
        cnx.close()

        
if __name__=='__main__':
    tester = MySQLTester()
    print("--- test 1 ---")
    tester.test1()
    print("--- test 2 ---")
    tester.test2()
    print("--- test 3 ---")
    tester.test3()
