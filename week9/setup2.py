# Import numpy package for numeric arrays and algebraic functions 
import numpy as np

#Creating plots
import matplotlib.pyplot as plt
import seaborn as sns

#Statistical packages
import sklearn.metrics as sk_metrics
from sklearn import datasets
import sklearn.linear_model as sk_lm
from scipy import stats

#Storing and manipulating data
import pandas as pd

#Some commands to make the plots look nice and big.
plt.rcParams['figure.figsize'] = (8,5)
plt.rcParams['figure.dpi'] = 120
plt.rcParams['lines.markersize'] = 7
plt.rcParams['lines.linewidth'] = 2

#Function returning the RMSE
def calc_RMSE(obs, pred, axis=1):
    return np.sqrt(sk_metrics.mean_squared_error(obs, pred))

#Function to make easier to display correlations nicely
def correlations(df, cat_vars):
    # Make a correlation matrix, if you look at this it would display values only
    cormat = df.loc[:,~df.columns.isin(cat_vars)].corr() 
    #.loc[rows to use (a), columns to use (b)]
    # (a) : - ALL
    # (b) ~ - NOT the columns in cat_vars
    # .corr() function with correlation between the dataframe variables as output

    # Add colours etc 
    sns.heatmap(cormat, annot=True, cmap='coolwarm', vmin=-1, vmax=1)


#Function taking the mean of 
def binned_stats(var, y, y_label):
    bin_means, bin_edges, binnumber = stats.binned_statistic(var,
                       y,
                       statistic='mean', 
                       bins=np.quantile(var,np.arange(0.05,1,0.05)))
    plt.hlines(bin_means, bin_edges[:-1], bin_edges[1:])
    plt.xlabel(var.name)
    plt.ylabel(y_label)
    plt.show()