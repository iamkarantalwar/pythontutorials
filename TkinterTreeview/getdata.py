

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
def fetch():
    cursor.execute("""SELECT * FROM `mytable` """)
    return(cursor.fetchall())
   
    
