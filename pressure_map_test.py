## Pressure map test ##
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
