# import sys
# sys.path.append('C:\\Users\\Elfen\\Desktop\\Algonum5\\Interpolation-and-integration')

## Pressure map test ##
# coding: utf-8

import matplotlib.pyplot as plt
from pressure_map import *

def create_pressure_map(file):
    print("#####################")
    print("#   Pressure map    #")
    print("#####################")
    print("===> Colored pressure map for boe103.dat <===")
    eps = 0.5*10**(-2)
    #eps = 0.01
    M = pressure_to_speed(file, eps)

    fig = plt.figure(5)
    ax = plt.subplot(111)
    im = ax.imshow(M, cmap=plt.get_cmap('hot'))#, interpolation='gaussian')#'nearest')
    fig.colorbar(im)
    plt.show()

        
file = "model/boe103.txt"
# file = "C:\\Users\\Elfen\\Desktop\\Algonum5\\Interpolation-and-integration\\boe103.txt"
create_pressure_map(file)

