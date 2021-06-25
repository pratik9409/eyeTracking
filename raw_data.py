import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import seaborn as sns
import cv2


data = pd.read_csv('myrecorded_data.csv')

first = data.loc[(data["quadrant"] == '1st')]
second = data.loc[(data["quadrant"] == '2nd')]
third = data.loc[(data["quadrant"] == '3rd')]
fourth = data.loc[(data["quadrant"] == '4th')]
center = []


sns_plot=sns.regplot(x=data["secs"], y=data["away_from_center"], data=data)
sns_plot.set(xlabel="Time(Seconds)", ylabel = "Away From Center")
plt.show()

sns_plot.figure.savefig('scatter.jpg')
