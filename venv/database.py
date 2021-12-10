#Database class to store and query students
import sqlite3 

class Database:
    #constructor
    def __init__(self):
        self.__conn = sqlite3.connect('sjsu_cs122.db')
        self.__c = self.__conn.cursor()
    
    #insert a student
    def insert(self, data):
        self.__c.execute("INSERT INTO students VALUES (?, ?, ?, ?, ?, ?, ?)", (None, data["name"], data["sjsuid"], data["hw"],
        data["exam"], data["year"], data["email"]))
        self.__conn.commit()

    #get data given an ID
    def getStudentById(self, id):
        self.__c.execute("SELECT * FROM students WHERE id=:id", {"id": id})
        results = self.__c.fetchall() 
        return results
    
    #get all students
    def getAll(self):
        self.__c.execute("SELECT * FROM students")
        results = self.__c.fetchall() 
        return results