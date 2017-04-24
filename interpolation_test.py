## Interpolation tests ##
# coding: utf-8

from interpolation import *
from Open import *

def display_dat():
    (ex,ey,ix,iy) = load_foil("boe103.txt")
    plt.plot([0, 1], [0, 0], color='black')
    plt.plot(ex, ey, "b-o")
    plt.plot(ix, iy, "b-o")
    plt.title("Original points of boe103")
    plt.show()


display_dat()
