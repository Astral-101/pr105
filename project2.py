import csv 
import numpy as np
import plotly.express as px

def readFile(dataPath):
  temperatureList = []
  iceCreamSaleList = []
  with open(dataPath) as f:
    csvData = csv.DictReader(f)
    for row in csvData:
      temperatureList.append(float(row['Temperature']))
      iceCreamSaleList.append(float(row["Ice-cream Sales"]))
  return {"x": temperatureList, "y": iceCreamSaleList }

def plotGraph(dataPath):
  with open(dataPath) as f:
    csvData = csv.DictReader(f)
    fig = px.scatter(csvData, x = "Temperature", y = "Ice-cream Sales")
    fig.show()



def calcCorrelation(dataSource):
  correlation = np.corrcoef(dataSource["x"], dataSource["y"])
  print(correlation[0, 1])
  


def setup():
  dataPath = "Ice-Cream vs Cold-Drink vs Temperature - Ice Cream Sale vs Temperature data.csv"
  dataSource = readFile(dataPath)   
  calcCorrelation(dataSource)
  plotGraph(dataPath)


  



setup()




















