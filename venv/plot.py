import pandas as pd #import pandas for dataframe
import seaborn as sns #import seaborn for plotting
import matplotlib.pyplot as plt
from database import Database #Database class to store students


#to plot the relation between hw and exam scores
def plotData():
    dataBase = Database() #initaialize the database from database class
    studentList = dataBase.getAll() #fetch all the students
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

    df = pd.DataFrame.from_dict(data) #create a dataframe from pandas with data of all students
    #convert the hw and exam scores column to numeric values for plotting
    df[["hw", "exam"]] = df[["hw", "exam"]].apply(pd.to_numeric) 
    #lmplot to visualize the relationship between hw and exam scores
    sns.lmplot(data=df,
           x="hw",
           y="exam")
           
    plt.savefig("./static/plot.png") #save the plot as a PNG file