

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
cursor = mydb.cursor()
def fetch():
    cursor.execute("SELECT * FROM `users`")
    return(cursor.fetchall())

def delete(id_):
    cursor.execute("DELETE FROM `users` where `user_id`=%s",(id_,))
    mydb.commit()



   
    
