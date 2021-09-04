import plotly.express as px
import csv
import numpy as np

def getDataSource(data_path):
    student = []
    days = []
    
    with open(data_path) as csv_file:
        csvReader = csv.DictReader(csv_file)
        for row in csvReader:
            student.append(float(row["Marks In Percentage"]))
            days.append(float(row["Days Present"]))
                  
    return {"x" : student, "y": days}

def findCorrelation(dataSource):
    correlation = np.corrcoef(dataSource["x"], dataSource["y"])
    print("Correlation between days and Marks", correlation[0,1])

def setup():
    data_path = 'Student Marks vs Days Present.csv'

    DataSource = getDataSource(data_path)
    findCorrelation(DataSource)

setup()            

