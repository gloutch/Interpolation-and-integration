import sys
sys.path.append('C:\\Users\\Elfen\\Desktop\\Projet\\Interpolation-and-integration')

## Model airflow tests ##
# coding: utf-8

import numpy as np
import matplotlib.pyplot as plt
from interpolation import *
from airflow import *
from Open import *

def create_airflow_map(file):
    print("#####################")
    print("#   Airflow model   #")
    print("#####################")
    print("===> Laminar flowing for boe103.dat <===")
    (ex, ey, ix, iy) = load_foil(file)
    
    hmin = np.min(iy)
    hmax = np.max(ey)
    
    intrados = apply_spline(ix, iy)
    extrados = apply_spline(ex, ey)
    
    nbpoints = 500
    
    flow_extrados = create_pressures(hmax, extrados, 0.06, nbpoints) # Third parameter changes accuracy
    flow_intrados = create_pressures(hmin, intrados, 0.12, nbpoints) # Third parameter changes accuracy
    
    plt.figure(2)
    pas = (ex[len(ex)-1] - ex[0]) / nbpoints
    x = np.arange(ex[0], ex[len(ex)-1], pas)
    y = []
    
    for i in range(nbpoints):
        y.append(extrados(x[i]))
    plt.plot(x, y, "r")
    
    l = len(flow_extrados)
    for i in range(1, l):
        y = []
        for j in range(nbpoints):
            y.append(flow_extrados[i](x[j]))
        plt.plot(x, y, "b")
    
    y = []
    for i in range(nbpoints):
        y.append(intrados(x[i]))
    plt.plot(x, y, "r")
    
    l = len(flow_intrados)
    for i in range (1, l):
        y = []
        for j in range(nbpoints):
            y.append(flow_intrados[i](x[j]))
        plt.plot(x, y, "b")

    plt.title("Airflow map")
    plt.show()
    
file = "model/boe103.txt"
file = "C:\\Users\\Elfen\\Desktop\\Projet\\Interpolation-and-integration\\model\\boe103.txt"
create_airflow_map(file)
