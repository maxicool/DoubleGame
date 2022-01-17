import numpy as np
from numpy.linalg import inv

import matplotlib as mpl
import matplotlib.pyplot as plt

from ipywidgets import interact

from mpl_toolkits.mplot3d import Axes3D


#Set some parameters to improve the appearance of plots.
plt.rcParams['figure.figsize'] = (8,5)
plt.rcParams['figure.dpi'] = 120
plt.rcParams['lines.markersize'] = 7
plt.rcParams['lines.linewidth'] = 2


#Function returning the root mean squared error between a given set of observed and estimated data.
def rmse(obs, pred, axis=1):
    return np.sqrt(np.sum((obs-pred)**2)/len(obs))


#The following function returns a plot with the observed data, the true function and a (purple) regression line from a #given value b0 of $\beta_0$ and a given value b1 of $\beta_1$.
#The plot also reports the root mean square error (RMSE - see aside below) of the regression line as well as including #vertical dashed lines between the estimated data $\hat{y}_i = \beta_0 + \beta_1 x_i$ and the observed data $y_i$.
def reg_line(x, y, b0, b1):
    y_hat = b0 + b1 * x
    
    plt.plot(x, y, ".", label = "Obs Data")
  #  plt.plot(x, y_truth, "r-", label = "True Func")
    plt.plot(x, y_hat, "m-", label = "Regression")
    plt.legend()
    
    plt.vlines(x, y_hat, y, linestyles="dotted", alpha=0.5, linewidth=1)
    plt.title(r"$\^y={:.2f} + {:.2f} x$   (RMSE = {:.3f})".format(b0, b1, rmse(y, y_hat))) 
    #Using r"$ $" creates a string in math text, similar to Latex
    #.format() passes values, in order, to the curly brackets in the string.
    plt.show()


#Function returning 3D plot of observed data and a regression if betas are provided (default is None)
def reg_line_3d(x1, x2, z, betas = None):
    fig = plt.figure(dpi=100, figsize = (10,8))
    ax = fig.add_subplot(111, projection='3d')
    
    #Set axes labels to be used to make title later
    ax.set_xlabel('$x_1$')
    ax.set_ylabel('$x_2$')
    ax.set_zlabel('$z$')
    
    #Set axes limits
    ax.set_xlim(min(x1), max(x1))
    ax.set_ylim(min(x2), max(x2))
    ax.set_zlim(min(z), max(z))
    
    #Regression
    if (betas is not None):
        X1 = np.linspace(min(x1)-0.1, max(x1)+0.1, num=100)
        X2 = np.linspace(min(x2)-0.1, max(x2)+0.1, num=100)
        X1, X2 = np.meshgrid(X1, X2)
        
        for kind, beta in betas.items():
            
            if kind == "model":
                color = "c"
            elif kind == "truth":
                color = "k"
            
            if (len(beta) == 3):
                b0, b1, b2 = beta
                Z = b0 + b1 * X1 + b2 * X2
                z_pred = b0 + b1 * x1 + b2 * x2
                title = r"$\^z = {:.2f} + {:.2f} x_1 + {:.2f} x_2$   (RMSE = {:.3f})".format(b0, b1, b2, rmse(z, z_pred))
        
            #With interaction between x1 and x2
            elif (len(beta) == 4):
                b0, b1, b2, b3 = beta
                Z = b0 + b1 * X1 + b2 * X2 + b3 * X1 * X2
                z_pred = b0 + b1 * x1 + b2 * x2 + b3 * x1 * x2
                title = r"$\^z = {:.2f} + {:.2f} x_1 + {:.2f} x_2 + {:.2f} x_1 x_2$   (RMSE = {:.3f})".format(b0, b1, b2, b3, rmse(z, z_pred))
            
            ax.plot_surface(X1, X2, Z, color=color, alpha=0.3)
            
            #Add dotted lines between the observed and estimated data 
            if kind == "model":
                for i in range(x1.size):
                    ax.plot(
                        [ x1[i,0],x1[i,0] ],
                        [ x2[i,0],x2[i,0] ],
                        [ z[i,0],z_pred[i,0] ],
                        "k:", linewidth = 1.5
                    )
                
                plt.title(title)    
            
    ax.scatter(x1, x2, z, marker='o', s=40, alpha=1)
    
    plt.show()