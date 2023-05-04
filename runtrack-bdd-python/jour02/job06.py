import mysql.connector


mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Clement2203$",
  database="laplateforme"
)
mycursor = mydb.cursor()
etage_sup = ("SELECT SUM(superficie) FROM salles")

mycursor.execute(etage_sup)
result = str(mycursor.fetchall()[0]).replace("(", "").replace(")", "")


print("la superficie total des salles est de " + str(result) + " m carré")