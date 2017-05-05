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

def pressure_to_speed(file, epsilon):
    (ex, ey, ix, iy) = load_foil(file)
    
    hmin = np.min(iy)
    hmax = np.max(ey)
    
    intrados = int.apply_spline(ix, iy)
    extrados = int.apply_spline(ex, ey)
    
    nbpoints = np.int((ex[len(ex)-1] - ex[0]) / epsilon)

    flow_extrados = create_pressures(hmax, extrados, epsilon, nbpoints) 
    flow_intrados = create_pressures(hmin, intrados, epsilon, nbpoints)
    
    pressure_speed_extrados = []
    pressure_speed_intrados = []
    
    le = len(flow_extrados)
    for i in range(0, le):
        pressure_speed_extrados.append(length_of_plane_curves(flow_extrados[i], ex[0], ex[len(ex)-1], nbpoints, simpson))
    li = len(flow_intrados)
    for i in range(0, li):
        pressure_speed_intrados.append(length_of_plane_curves(flow_intrados[i], ix[0], ix[len(ix)-1], nbpoints, simpson))
    
    # np.ones?
    M = np.zeros((nbpoints, nbpoints))
    for i in range(nbpoints):
        for j in range(nbpoints):
            M[i][j] = 1.0
          
    for i in range(le):
        for j in range(nbpoints):
            M[nbpoints//2 - round(flow_extrados[i](j/nbpoints)*nbpoints, 0)][j] = pressure_speed_extrados[i]   
            
    for i in range(li):
        for j in range(nbpoints):
            M[nbpoints//2 - round(flow_intrados[i](j/nbpoints)*nbpoints, 0)][j] = pressure_speed_intrados[i] 
            
    fig = plt.figure(5)
    ax = plt.subplot(111)
    im = ax.imshow(M, cmap=plt.get_cmap('hot'), interpolation='gaussian')#'nearest')
    #im = plt.gaussian_filter(im, sigma=(14), order=0)
    fig.colorbar(im)
    plt.show()


"""
# Links pressure with air speed
def pressure_to_speed(flows_array, function):
    
    pressure_speed = []
    for i in range(0, len(flows_array)):
        pressure_speed.append(length_of_plane_curves(function, flows_array[i][0], flows_array[i][1], len(flows_array), simpson))
        
    return pressure_speed
"""
