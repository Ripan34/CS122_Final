#Database class to store and query students

import sqlite3  #import sqlite database

class Database:
    #constructor
    #connects with database file and gets a cursor
    def __init__(self):
        self.__conn = sqlite3.connect('sjsu_cs122.db') #connect the given database file
        self.__c = self.__conn.cursor() #get the cursor from the connection
    
    #insert a student 
    #parameters: data (dict of student info)
    def insert(self, data):
        self.__c.execute("INSERT INTO students VALUES (?, ?, ?, ?, ?, ?, ?)", (None, data["name"], data["sjsuid"], data["hw"],
        data["exam"], data["year"], data["email"]))
        self.__conn.commit()

    #get a student given an ID
    #return: a list of touples
    def getStudentById(self, id):
        self.__c.execute("SELECT * FROM students WHERE id=:id", {"id": id})
        results = self.__c.fetchall() 
        return results
    
    #Fetch all students from the database
    def getAll(self):
        self.__c.execute("SELECT * FROM students")
        results = self.__c.fetchall() 
        return results