import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

data = pd.read_csv("tab1.csv", header=None).to_numpy()
properties = ["pH(CaCl2)", "pH(H2O)", "EC", "CaCO3",
              "P", "N", "K", "Stones"]
x = data[:,0]
y = data[:,4]
#plt.axis([0,1,0,1])
plt.xlabel("Relation with SOC")
plt.ylabel("Optimal λ")
plt.scatter(x,y)

plt.annotate(properties[0], (x[0], y[0]))
plt.annotate(properties[1], (x[1], y[1]))
plt.annotate(properties[2], (x[2], y[2]))
plt.annotate(properties[3], (x[3], y[3]))
plt.annotate(properties[4], (x[4], y[4]))
plt.annotate(properties[5], (x[5], y[5]))
plt.annotate(properties[6], (x[6], y[6]))
plt.annotate(properties[7], (x[7], y[7]))

plt.show()

