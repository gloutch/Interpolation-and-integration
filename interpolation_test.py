## Interpolation tests ##
# coding: utf-8

from interpolation import *
from Open import *

def display_interpolation():
    (ex,ey,ix,iy) = load_foil("boe103.txt")
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


print("#####################")
print("#   Interpolation   #")
print("#####################")
print("===> Interpolation test for boe103.dat <===")
display_interpolation()
