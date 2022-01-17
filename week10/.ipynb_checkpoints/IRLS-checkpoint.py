import numpy as np
from numpy.linalg import inv

''' This python file contains the Iteratively Rewighted Least Squares algorithm to get a least squares estimate in logistic regression problems. '''

def IRLS(beta_start,X,y):
    n,p=X.shape # get problem size
    
    beta_hat = np.zeros(n) # initialise estimator (if we skip this line, beta_hat will be a shallow copy of beta_Start)
    beta_hat = beta_start # set estimator to given start vector 
    
    mu = np.zeros(n) # initialise mean vector
    S = np.zeros((n,n)) # initialise weighting matrix
    
    # Iteratively improve the estimator
    for _ in range(1000):
        
        # calculate mean
        for i in range(n):
            mu[i] = 1/(1+np.exp(-np.dot(beta_hat,X[i,:])))
            
        # calculate weighting matrix
        S = np.diag(mu*(1-mu))
        
        if np.prod(mu*(1-mu))==0:
            break
        
        # update beta_hat (split in three lines for better readability)
        inv_XSX = inv(np.matmul(X.transpose(),np.matmul(S,X)))
        SXbeta = np.matmul(S,np.matmul(X,beta_hat))
        beta_hat = np.matmul(inv_XSX,np.matmul(X.transpose(),SXbeta+y-mu))
        
    return beta_hat