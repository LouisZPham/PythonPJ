import pandas as pd
import numpy as np
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv("D:\Python\read2.csv", encoding = 'eng1')
data = data.dropna()
print(data.head())