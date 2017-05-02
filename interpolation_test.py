import sys
sys.path.append('C:\\Users\\Elfen\\Desktop\\Algonum5\\Interpolation-and-integration')

## Interpolation tests ##
# coding: utf-8

from interpolation import *
from Open import *

def display_interpolation():
    file = "C:\\Users\\Elfen\\Desktop\\Algonum5\\Interpolation-and-integration\\boe103.txt"
    (ex,ey,ix,iy) = load_foil(file)
    plt.figure(1)
    plt.subplot(121)
    plt.plot([0, 1], [0, 0], color='black')
    plt.plot(ex, ey, "b-o")
    plt.plot(ix, iy, "b-o")
    plt.title("Original points of boe103")

    plt.subplot(122)
    plt.plot([0, 1], [0, 0], color='black')
    extrados = apply_spline(ex, ey, 300)
    intrados = apply_spline(ix, iy, 300)
    plt.plot(extrados[0], extrados[1], "r")
    plt.plot(intrados[0], intrados[1], "r")
    plt.title("Interpolated points of boe103")
    plt.show()

def display_interpolation_lambda():
    file = "C:\\Users\\Elfen\\Desktop\\Algonum5\\Interpolation-and-integration\\boe103.txt"
    (ex,ey,ix,iy) = load_foil(file)
    plt.figure(2)
    plt.subplot(121)
    plt.plot([0, 1], [0, 0], color='black')
    plt.plot(ex, ey, "b-o")
    plt.plot(ix, iy, "b-o")
    plt.title("Original points of boe103")

    nbpoints = 300
    
    extrados = apply_spline_lambda(ex, ey) #lambda
    pas = (ex[len(ex)-1] - ex[0]) / nbpoints
    x1 = np.arange(ex[0], ex[len(ex)-1], pas)
    y1 = []
    for i in range(nbpoints):
        y1.append(extrados(x1[i]))

    intrados = apply_spline_lambda(ix, iy) #lambda
    pas = (ix[len(ix)-1] - ix[0]) / nbpoints
    x2 = np.arange(ix[0], ix[len(ix)-1], pas)
    y2 = []
    for i in range(nbpoints):
        y2.append(intrados(x2[i]))
        
    
    plt.subplot(122)
    plt.plot([0, 1], [0, 0], color='black')
    plt.plot(x1, y1, "r")
    plt.plot(x2, y2, "r")
    plt.title("Interpolated points of boe103")
    plt.show()
    
print("#####################")
print("#   Interpolation   #")
print("#####################")
print("===> Interpolation test for boe103.dat <===")
display_interpolation()
display_interpolation_lambda()
