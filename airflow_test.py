import sys
sys.path.append('C:\\Users\\Elfen\\Desktop\\Algonum5\\Interpolation-and-integration')

## Model airflow tests ##
# coding: utf-8

import numpy as np
import matplotlib.pyplot as plt
import interpolation as int
from airflow import *
from Open import *

def create_airflow_map(file):
    (ex, ey, ix, iy) = load_foil(file)
    
    hmin = np.min(iy)
    hmax = np.max(ey)
    
    new_intrados = int.apply_spline_lambda(ix, iy)
    new_extrados = int.apply_spline_lambda(ex, ey)
    
    flow_extrados = create_pressures(hmax, new_extrados, 0.06, 500) # Third parameter changes accuracy
    flow_intrados = create_pressures(hmin, new_intrados, 0.12, 500) # Third parameter changes accuracy
    plt.figure(3)
    for i in range(1, len(flow_extrados)):
        plt.plot(flow_extrados[i][0], flow_extrados[i][1], "b")
    for i in range (1, len(flow_intrados)):
        plt.plot(flow_intrados[i][0], flow_intrados[i][1], "b")
    
    extrados = int.apply_spline(ex, ey, 200)
    intrados = int.apply_spline(ix, iy, 200)
    
    plt.plot(extrados[0], extrados[1], "r")
    plt.plot(intrados[0], intrados[1], "r")
    
    plt.title("Airflow map")
    plt.show()

def create_airflow_map_lambda(file):
    (ex, ey, ix, iy) = load_foil(file)
    
    hmin = np.min(iy)
    hmax = np.max(ey)
    
    new_intrados = int.apply_spline_lambda(ix, iy)
    new_extrados = int.apply_spline_lambda(ex, ey)
    
    nbpoints = 500
    
    flow_extrados = create_pressures_lambda(hmax, new_extrados, 0.06, nbpoints) # Third parameter changes accuracy
    flow_intrados = create_pressures_lambda(hmin, new_intrados, 0.12, nbpoints) # Third parameter changes accuracy
    
    plt.figure(4)
    pas = (ex[len(ex)-1] - ex[0]) / nbpoints
    x = np.arange(ex[0], ex[len(ex)-1], pas)
    y = []
    for i in range(1, len(flow_extrados)):
        y = []
        for j in range(nbpoints):
            y.append(flow_extrados[i](x[j]))
        plt.plot(x, y, "b")
    for i in range (1, len(flow_intrados)):
        y = []
        for j in range(nbpoints):
            y.append(flow_intrados[i](x[j]))
        plt.plot(x, y, "b")
    
    extrados = int.apply_spline(ex, ey, 200)
    intrados = int.apply_spline(ix, iy, 200)
    
    plt.plot(extrados[0], extrados[1], "r")
    plt.plot(intrados[0], intrados[1], "r")
    
    plt.title("Airflow map")
    plt.show()

print("#####################")
print("#   Airflow model   #")
print("#####################")
print("===> Laminar flowing for boe103.dat <===")
#file = "boe103.txt"
file = "C:\\Users\\Elfen\\Desktop\\Algonum5\\Interpolation-and-integration\\boe103.txt"
create_airflow_map(file)
create_airflow_map_lambda(file)
