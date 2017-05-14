import sys
sys.path.append('C:\\Users\\Elfen\\Desktop\\Projet\\Interpolation-and-integration')

## Interpolation tests ##
# coding: utf-8

from interpolation import *
import matplotlib.pyplot as plt
from Open import *
    
file1 = "model/boe103.txt"
file2 = "model/HOR20.txt"
file3 = "model/DU84132V.txt"


def display_interpolation(file):
    print("#####################")
    print("#   Interpolation   #")
    print("#####################")
    print("===> Interpolation test for ", file, " <===")
    (ex,ey,ix,iy) = load_foil(file)
    
    nbpoints = 1200
    
    extrados = apply_spline(ex, ey) 
    pas = (ex[len(ex)-1] - ex[0]) / nbpoints
    x1 = np.arange(ex[0], ex[len(ex)-1], pas)
    y1 = np.empty(nbpoints)
    for i in range(nbpoints):
        y1[i] = extrados(x1[i])

    intrados = apply_spline(ix, iy) 
    pas = (ix[len(ix)-1] - ix[0]) / nbpoints
    x2 = np.arange(ix[0], ix[len(ix)-1], pas)
    y2 = np.empty(nbpoints)
    for i in range(nbpoints):
        y2[i] = intrados(x2[i])
        

    plt.plot([0, 1], [0, 0], color='black')

    # interpolaton
    plt.plot(x1, y1, "r")
    plt.plot(x2, y2, "r")
    
    # original shape
    plt.plot(ex, ey, "b--")
    plt.plot(ix, iy, "b--") 

    plt.title("Interpolated points of " + file)
    plt.show()
file1 = "C:\\Users\\Elfen\\Desktop\\Projet\\Interpolation-and-integration\\model\\boe103.txt"
display_interpolation(file1)
