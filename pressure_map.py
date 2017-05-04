import sys
sys.path.append('C:\\Users\\Elfen\\Desktop\\Algonum5\\Interpolation-and-integration')

## Pressure map modeled ##
# coding: utf-8

import numpy as np
import matplotlib.pyplot as plt
import interpolation as int
from airflow import *
from Open import *
from integration import *

# Links pressure with air speed
def pressure_to_speed(flows_array, function):
    
    pressure_speed = []
    for i in range(0, len(flows_array)):
        pressure_speed.append(length_of_plane_curves(function, flows_array[i][0], flows_array[i][1], len(flows_array), simpson))
        
    return pressure_speed


def pressure_to_speed_lambda():
    file = "C:\\Users\\Elfen\\Desktop\\Algonum5\\Interpolation-and-integration\\boe103.txt"
    (ex, ey, ix, iy) = load_foil(file)
    
    hmin = np.min(iy)
    hmax = np.max(ey)
    
    new_intrados = int.apply_spline_lambda(ix, iy)
    new_extrados = int.apply_spline_lambda(ex, ey)
    
    nbpoints = 100
    flow_extrados = create_pressures_lambda(hmax, new_extrados, 0.01, nbpoints) # Third parameter changes accuracy
    flow_intrados = create_pressures_lambda(hmin, new_intrados, 0.01, nbpoints) # Third parameter changes accuracy
    
    pressure_speed_extrados = []
    pressure_speed_intrados = []
    
    for i in range(0, len(flow_extrados)):
        pressure_speed_extrados.append(length_of_plane_curves(flow_extrados[i], 0, 1, nbpoints, simpson))
    for i in range(0, len(flow_intrados)):
        pressure_speed_intrados.append(length_of_plane_curves(flow_intrados[i], 0, 1, nbpoints, simpson))
    
    M = np.zeros((40, 100))
    for i in range(40):
        for j in range(100):
            M[i][j] = 1.0
          
    for i in range(len(flow_extrados)):
        for j in range(100):
            M[30 - round(flow_extrados[i](j/100)*100, 0)][j] = pressure_speed_extrados[i]   
            
    for i in range(len(flow_intrados)):
        for j in range(100):
            M[30 - round(flow_intrados[i](j/100)*100, 0)][j] = pressure_speed_intrados[i] 
            
    fig = plt.figure(5)
    ax = plt.subplot(111)
    im = ax.imshow(M, cmap=plt.get_cmap('hot'), interpolation='nearest')
    fig.colorbar(im)
    plt.show()

pressure_to_speed_lambda()