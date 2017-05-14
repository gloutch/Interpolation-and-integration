## Pressure map test ##
# coding: utf-8

import matplotlib.pyplot as plt
from pressure_map import *

def create_pressure_map(file):
    print("#####################")
    print("#   Pressure map    #")
    print("#####################")
    print("===> Colored pressure map for boe103.dat <===")
    eps = 10**(-3)
    M = pressure_to_speed(file, eps)

    fig = plt.figure(5)
    ax = plt.subplot(111)
    im = ax.imshow(M, cmap=plt.get_cmap('hot'))
    fig.colorbar(im)
    plt.show()



