import mysql.connector
from datetime import datetime

class Zoo:
    def __init__(self):
        self.myzoo = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Clement2203$",
            database="zoo"
        )
        self.cursor = self.myzoo.cursor()

    def add_animal(self, nom, race, id_cage, date_naissance, pays):
        date_obj = datetime.strptime(date_naissance, '%Y-%m-%d')
        date_str = date_obj.strftime('%Y-%m-%d')
        new_animal = "INSERT INTO animal (nom, race, id_cage, date_naissance, pays) VALUES (%s, %s, %s, %s, %s)"
        value = (nom, race, id_cage, date_str, pays)
        self.cursor.execute(new_animal, value)
        self.myzoo.commit()
        return self.cursor.lastrowid


    def read_animal(self):
        query = "SELECT * FROM animal;"
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def update_animal(self, id, nom, race, id_cage, date_naissance, pays):
        query = "UPDATE animal nom=%s, race=%s, id_cage=%s, date_naissance=%s, pays=%s WHERE id=%s;"
        value = (id, nom, race, id_cage, date_naissance, pays)
        self.cursor.execute(query, value)
        self.myzoo.commit()

    def delete_animal(self, id):
        query = "DELETE FROM animal WHERE id=%s;"
        value = (id,)
        self.cursor.execute(query, value)
        self.myzoo.commit()

    def add_cage(self,superficie, capacite, occuper=False):
        query = "INSERT INTO cage (superficie, capacité, occuper) VALUES (%s, %s, %s);"
        value = (superficie, capacite, occuper)
        self.cursor.execute(query, value)
        self.myzoo.commit()
        return self.cursor.lastrowid

    def update_cage(self, id, superficie, capacite, occuper=False):
        query = "UPDATE cage superficie=%s capacité=%s occuper=%s WHERE id=%s;"
        value = (id, superficie, capacite, occuper)
        self.cursor.execute(query, value)
        self.myzoo.commit()

    def calcule_superficie(self):
        query = "SELECT SUM(superficie) FROM cage;"
        self.cursor.execute(query)
        resultat = self.cursor.fetchone()
        superficie_tt = resultat[0]
        return superficie_tt


    def read_cage(self):
        query = "SELECT * FROM cage;"
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def delete_cage(self, id):
        query = "DELETE FROM cage WHERE id=%s"
        value = (id,)
        self.cursor.execute(query, value)
        self.myzoo.commit()

    def read_animal_by_cage(self, id_cage):
        query = "SELECT * FROM animal WHERE id_cage=%s;"
        value = (id_cage,)
        self.cursor.execute(query, value)
        return self.cursor.fetchall()


zoo = Zoo()
# zoo.add_animal("baloo", "ours", 3, "2015-06-20", "amerique")
# zoo.add_cage(800, 2, False)
# print(zoo.read_animal())
# print(zoo.calcule_superficie())
print(zoo.read_animal_by_cage(1))
print(zoo.read_animal_by_cage(2))
print(zoo.read_animal_by_cage(3))
print(zoo.read_animal_by_cage(4))
