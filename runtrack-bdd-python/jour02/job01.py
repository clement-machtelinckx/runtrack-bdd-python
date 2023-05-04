import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Clement2203$",
  database="laplateforme"
)
mycursor = mydb.cursor()

etud = ("SELECT * FROM etudiant;")
mycursor.execute(etud)
result = mycursor.fetchall()
for row in result:
  print(row)