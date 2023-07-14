import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn import linear_model

data = pd.read_csv("tab1.csv", header=None).to_numpy()
properties = ["pH(CaCl2)", "pH(H2O)", "EC", "CaCO3",
              "P", "N", "K", "Stones"]
x = data[:,0:1]
y = data[:,4]

regr = linear_model.LinearRegression()
regr.fit(x,y)
s = regr.score(x,y)
print(s)
