import plotly.express as px
import csv
import numpy as np

def getDataSource(data_path):
    coffee = []
    sleep = []
    
    with open(data_path) as csv_file:
        csvReader = csv.DictReader(csv_file)
        for row in csvReader:
           coffee.append(float(row["Coffee in ml"]))
           sleep.append(float(row["sleep in hours"]))
                  
    return {"x" : coffee, "y": sleep}

def findCorrelation(dataSource):
    correlation = np.corrcoef(dataSource["x"], dataSource["y"])
    print("Correlation between sleep and coffee", correlation[0,1])

def setup():
    data_path = 'cups of coffee vs hours of sleep.csv'

    DataSource = getDataSource(data_path)
    findCorrelation(DataSource)

setup()            

