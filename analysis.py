import pandas as pd
import sklearn
import matplotlib.pyplot as plt
import seaborn as sns  
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics
from sklearn.preprocessing import StandardScaler

# Read in the data
df = pd.read_csv('data/imovel_data.csv')



