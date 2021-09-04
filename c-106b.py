import plotly.express as px
import csv
import numpy as np

def getDataSource(data_path):
    ice_cream = []
    temperature = []
    cold_drink = []
    with open(data_path) as csv_file:
        csvReader = csv.DictReader(csv_file)
        for row in csvReader:
            ice_cream.append(float(row["Ice-cream Sales"]))
            temperature.append(float(row["Temperature"]))
            cold_drink.append(float(row["Cold drink sales"]))
        
    return {"x" : cold_drink, "y": temperature}

def findCorrelation(dataSource):
    correlation = np.corrcoef(dataSource["x"], dataSource["y"])
    print("Correlation between Temperature and ice_cream", correlation[0,1])

def setup():
    data_path = 'Ice-Cream vs Cold-Drink vs Temperature - Ice Cream Sale vs Temperature data.csv'

    DataSource = getDataSource(data_path)
    findCorrelation(DataSource)

setup()            

