## Model airflow ##
# coding: utf-8

import numpy as np
import matplotlib.pyplot as plt
import interpolation as int

# The family of curves describing the airflow above the wing are given by the following equations
def flow_function(function, lbd, h):
    return (lambda x: (1-lbd)*function(x) + lbd*(3*h))

# Creates flows array for a given h and a function
def create_pressures(h, function, accuracy, nb_points):
    flows_array = []
    index = 0
    one_point = 1./nb_points
    
    for i in np.arange(0., 1., accuracy):
        flows_array.append([])
        flows_array[index].append([])
        flows_array[index].append([])
        
        f = flow_function(function, i, h)
        
        for k in range(0, nb_points):
            flows_array[index][0].append(k*one_point)
            flows_array[index][1].append(f(k*one_point))
        
        index +=1
    
    return flows_array
