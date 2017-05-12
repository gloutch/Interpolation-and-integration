import sys
# sys.path.append('C:\\Users\\Elfen\\Desktop\\Algonum5\\Interpolation-and-integration')

## Pressure map test ##
# coding: utf-8

import numpy as np
import matplotlib.pyplot as plt
from interpolation import *
from airflow import *
from Open import *
from pressure_map import *

def create_pressure_map(file):
    print("#####################")
    print("#   Pressure map    #")
    print("#####################")
    print("===> Colored pressure map for boe103.dat <===")
    epsilon = 0.5*10**(-2)
    pressure_to_speed(file, epsilon)
        
file = "boe103.txt"
# file = "C:\\Users\\Elfen\\Desktop\\Algonum5\\Interpolation-and-integration\\boe103.txt"
create_pressure_map(file)

