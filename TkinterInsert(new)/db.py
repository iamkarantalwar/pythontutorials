import mysql.connector

mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="",
        database="mcpc")

cursor = mydb.cursor()

def insertData(lis):
    print("From DB FILE")
    print(lis)
    cursor.execute("""INSERT INTO `users`(`name`, `email`, `password`) VALUES
(%s,%s,%s)""",lis)
    mydb.commit()
