# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import pymc as pm

print('Running on pymc v{}'.format(pm.__version__))
np.random.seed(123)

#True parameter values 
alpha, sigma = 1,1
beta = [1,2.5]

#Size of dataset
size = 50

#Predictor variable
A1 = np.random.randn(size)
A2 = np.random.randn(size) * 0.2

#Now let's create the model
#Simulate outcome variable
Y = alpha + beta[0]*A1 + beta[1]*A2 + np.random.randn(size)*sigma

basic_model = pm.Model()

#Create context manager
with basic_model:
    #Prior for unknown model parameters
    alpha = pm.Normal('alpha',mu=0,sigma=10)
    beta = pm.Normal('beta',mu=0,sigma=1,shape=2)
    sigma = pm.HalfNormal('sigma',sigma=1)
    
    #Expected value of outcome
    mu = alpha + beta[0]*A1 + beta[1]*A2
    
    #Likelihood (sampling distribution) of observations
    Y_obs = pm.Normal('Y_obs',mu=mu,sigma=sigma,observed=Y)
    #map = maximum a posteri
    map_estimate = pm.find_MAP(model=basic_model)
    
#Check map_estimate variable after it runs to get your updated priors