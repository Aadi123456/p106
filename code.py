import numpy as np
import csv


def setup():
    dataPath = '/Users/Aadi/Downloads/class106/data1.csv'
    dataSource = getDataSource(dataPath)
    findCorelation(dataSource)

def findCorelation(dataSource):
    corelation = np.corrcoef(dataSource['x'], dataSource['y'])
    print('Corelation between Size of Tv and Average Time spent watching.')

def getDataSource(dataPath):
    tvSize = []
    timeWatchingTV = []
    with open(dataPath) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for now in csv_reader:
            tvSize.append(float(row['Size of TV']))
            timeWatchingTV.append(float(row['Average time spent watching TV in a week (hours)']))
        return{"x":tvSize, "y":timeWatchingTV}

setup()