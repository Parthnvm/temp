#Seaborn 

import seaborn as sns
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

tips = sns.load_dataset('tips')


sns.catplot(x="day", y="total_bill",data = tips,hue="smoker",palette="Set2")
plt.show()