## Pressure map modeled ##
# coding: utf-8

import numpy as np
import matplotlib.pyplot as plt
import interpolation as int
from airflow import *
from Open import *
from pressure_map import *

def create_pressure_map(file):
    (ex, ey, ix, iy) = load_foil(file)
    
    hmin = np.min(iy)
    hmax = np.max(ey)
    
    new_intrados = int.apply_spline_lambda(ix, iy)
    new_extrados = int.apply_spline_lambda(ex, ey)
    
    flow_extrados = create_pressures(hmax, new_extrados, 0.06, 500) # Third parameter changes accuracy
    flow_intrados = create_pressures(hmin, new_intrados, 0.12, 500) # Third parameter changes accuracy
    
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

    #######################
    ## Add colored map ! ##
    #######################

print("#####################")
print("#   Pressure map    #")
print("#####################")
print("===> Colored pressure map for boe103.dat <===")
file = "boe103.txt"
create_pressure_map(file)
