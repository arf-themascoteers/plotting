import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df = pd.read_csv("data.csv")
for col in df.columns:
    x = [0.1,0.2,0.3,0.4,0.5]
    y = list(df[col])
    #plt.axis([0,1,0,1])
    plt.plot(x,y)
plt.legend(df.columns)
plt.show()

