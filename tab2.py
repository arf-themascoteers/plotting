import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

data = pd.read_csv("tab2.csv", header=None).to_numpy()
properties = ["pH(CaCl2)", "pH(H2O)", "EC", "CaCO3",
              "P", "N", "K", "Stones"]



for i in range(data.shape[0]):
    print(data[i])
    plt.plot(data[i])


plt.xlabel("λ")
plt.ylabel("R^2")
plt.legend(properties)
plt.show()

