from flask import Flask, request, render_template, redirect
from database import Database #Database class to store users
import plot

app = Flask(__name__)

@app.route("/")
def students():
    dataBase = Database()
    studentList = dataBase.getAll()
    data = []
    for student in studentList:
        item = {
        "id": student[0],
        "name": student[1],
        "sjsuid": student[2],
        "hw": student[3],
        "exam": student[4],        
        }
        data.append(item)
    return render_template("landingPage.html", data=data)

@app.route("/student/<id>")
def showStudent(id):
    dataBase = Database()
    student = dataBase.getStudentById(id)
    data = {
        "name": student[0][1],
        "sjsuid": student[0][2],
        "hw": student[0][3],
        "exam": student[0][4],
        "email": student[0][6],
        "year": student[0][5]
        }
    return render_template("showStudent.html", data=data)

@app.route("/create")
def create():
    return render_template("addStudent.html")

@app.route("/create", methods=['POST'])
def addStudent():
    data = {
        "email": request.form['email'],
        "name": request.form['name'],
        "sjsuid": request.form['sjsuid'],
        "year": request.form['year'],
        "hw": request.form['hw'],
        "exam": request.form['exam']
    }
    database = Database()
    database.insert(data)
    return redirect("/")