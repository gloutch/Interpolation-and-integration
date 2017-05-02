import sys
sys.path.append('C:\\Users\\Elfen\\Desktop\\Algonum5\\Interpolation-and-integration')

import numpy as np;
import re; # regexp
import matplotlib.pyplot as ma;

################################################################
# Airfoil : load profile of a wing
#
# Reads a file whose lines contain coordinates of points,
# separated by an empty line.
# Every line not containing a couple of floats is discarded. 
# Returns a couple constitued of the list of points of the
# extrados and the intrados. 
def load_foil(file):
    f = open(file, 'r')
    matchline = lambda line: re.match(r"\s*([\d\.-]+)\s*([\d\.-]+)", line)
    extra  = [];    intra = []
    rextra = False; rintra = False
    for line in f:
        m = matchline(line)
        if (m != None) and not(rextra):
            rextra = True
        if (m != None) and rextra and not(rintra):
            extra.append(m.groups())
        if (m != None) and rextra and rintra:
            intra.append(m.groups())
        if (m == None) and rextra:
            rintra = True
    
    le = len(extra)
    li = len(intra)
    ex = np.array([float(extra[i][0]) for i in range(le)])
    ey = np.array([float(extra[i][1]) for i in range(le)])
    ix = np.array([float(intra[i][0]) for i in range(li)])
    iy = np.array([float(intra[i][1]) for i in range(li)])
    return(ex,ey,ix,iy)
