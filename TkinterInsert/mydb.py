
#import the MySql Api
import mysql.connector

#create a bridge between mysql and python
#create the connection
mydb = mysql.connector.connect(
    user="root",
    passwd = "",
    host = "localhost",
    database="mcpc",
    )
#make a cursor
cursor = mydb.cursor()
def insert(tup):
    cursor.execute("""INSERT INTO `mytable`(`username`, `password`)
                    VALUES(%s,%s)""",tup)
    #if you use insert query then it's important to commit the command
    #if you send the data from python to mysql you will use commit
    mydb.commit()
