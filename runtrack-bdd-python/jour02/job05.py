import mysql.connector


mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Clement2203$",
  database="laplateforme"
)
mycursor = mydb.cursor()
etage_sup = ("SELECT SUM(superficie) FROM etage")

mycursor.execute(etage_sup)
result = str(mycursor.fetchall()[0]).replace("(", "").replace(")", "")


print("la superficie total de la plateforme est de " + str(result) + " m carré")
