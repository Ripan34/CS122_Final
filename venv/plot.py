import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from database import Database #Database class to store users


#to plot the relation between hw and exam scores
def plotData():
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
    df = pd.DataFrame.from_dict(data)
    df[["hw", "exam"]] = df[["hw", "exam"]].apply(pd.to_numeric)
    sns.lmplot(data=df,
           x="hw",
           y="exam").savefig("plot.png")
    plt.savefig("./static/plot.png")

plotData()