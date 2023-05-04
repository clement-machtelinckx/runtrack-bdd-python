import mysql.connector


mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Clement2203$",
  database="laplateforme"
)
mycursor = mydb.cursor()

salle = ("SELECT * FROM salles;")
nom = ("SELECT nom, superficie FROM salles;")
sup = ("SELECT superficie FROM salles;")
mycursor.execute(nom)
result = mycursor.fetchall()
for row in result:
  print(row)