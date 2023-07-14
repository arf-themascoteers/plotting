import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

data = pd.read_csv("x.csv", header=None).to_numpy()
x = data[:,0]
y = data[:,1]
plt.xlabel("Wavelength (nm)")
plt.ylabel("Reflectance")
plt.plot(x,y)


plt.show()

