#import sys
#sys.path.append('C:\\Users\\Elfen\\Desktop\\Algonum5\\Interpolation-and-integration')

## Pressure map modeled ##
# coding: utf-8

import numpy as np
from interpolation import apply_spline
from airflow import *
from Open import *
from integration import *


def pressure_to_speed(file, epsilon):
    (ex, ey, ix, iy) = load_foil(file)
    
    hmin = np.min(iy)
    hmax = np.max(ey)
    
    intrados = apply_spline(ix, iy)
    extrados = apply_spline(ex, ey)
    
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

    M = np.ones((nbpoints, nbpoints))
          
    for i in range(le):
        for j in range(nbpoints):
            k = np.int(nbpoints//2 - round(flow_extrados[i](j/nbpoints)*nbpoints, 0))
            M[k][j] = pressure_speed_extrados[i]   
            
    for i in range(li):
        for j in range(nbpoints):
            k = np.int(nbpoints//2 - round(flow_intrados[i](j/nbpoints)*nbpoints, 0)) 
            M[k][j] = pressure_speed_intrados[i]

    return M
