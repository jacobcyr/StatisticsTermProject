import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("budgets.csv")

x = data["city_population"]

def xBar(x):
    xBar=0
    n=0
    #pandas objects contain strings and i need an integer
    for i in x:
        n+=1
        #remove comma with null string
        niceInt = int(i)
        #add everything together
        xBar+=niceInt
    result = xBar
    return result, n


def sampleMean(x):
    result = xBar(x)
    return result[0] / result[1]

def median(x,oddOREven):
    resultofXbar = xBar(x)

    # how long is the list is it odd or even
    count = 0
    for entry in x:
        count += 1
        if count % 2 == 1:
            oddOREven = "even"
            #add all elements of tyhe data set and divide by n
            data = 0
            for adding in x:
                data+=1
        else:
            oddOREven = "odd"
            pass
        pass
    pass
