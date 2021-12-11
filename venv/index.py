#index file to create Flask APP
#AUTHOR: Ripandeep Singh

from flask import Flask, request, render_template, redirect #importing flask, request, redirect modules
from database import Database #Database class to store students
import plot #plot file to save a plot png

plot.plotData() #plot the data and save a png in static directory

app = Flask(__name__) #initalize FLASK APP

#home route
@app.route("/") 
def students():
    dataBase = Database() #initaialize the database from database class
    studentList = dataBase.getAll() #get all the saved students from the database
    data = []
    #make a list of students objects fethced from database
    for student in studentList:
        item = {
        "id": student[0],
        "name": student[1],
        "sjsuid": student[2],
        "hw": student[3],
        "exam": student[4],        
        }
        data.append(item)

    #render landing page template by providing the students data
    return render_template("landingPage.html", data=data)

#show student info route using URL parameters
@app.route("/student/<id>")
def showStudent(id):
    dataBase = Database() #initaialize the database from database class
    student = dataBase.getStudentById(id) #query a student with a given ID
    #student data
    data = {
        "name": student[0][1],
        "sjsuid": student[0][2],
        "hw": student[0][3],
        "exam": student[0][4],
        "email": student[0][6],
        "year": student[0][5]
        }

    #render showStudent template by providing the a student fetched by a given ID
    return render_template("showStudent.html", data=data)

#create a new Student route
@app.route("/create")
def create():
    #render create a new student template
    return render_template("addStudent.html")

#to create a new student with POST request
@app.route("/create", methods=['POST'])
def addStudent():
    #use request.FORM to get key value pairs from the request body
    data = {
        "email": request.form['email'], 
        "name": request.form['name'],
        "sjsuid": request.form['sjsuid'],
        "year": request.form['year'],
        "hw": request.form['hw'],
        "exam": request.form['exam']
    }
    database = Database() #initaialize the database from database class
    database.insert(data) #insert the student in the database
    return redirect("/")  #redirect the user to home page using redirect module