import sys
sys.path.append('C:\\Users\\Elfen\\Desktop\\Projet\\Interpolation-and-integration')

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
    for i in np.arange(0., 1., accuracy):
        flows_array.append(flow_function(function, i, h))
    return flows_array
 