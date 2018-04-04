#### execute the code with the following command : gunzip -c hygdata_v3.csv.gz | python K_nearest_neighbor.py k


#!/usr/bin/env python

import numpy as np
import sys

no_of_dimensions = 3 ### x,y,z

### loading the data into memory using the numpy array and using only the columns required to caluculate the distance

a=np.loadtxt(r'hygdata_v3.csv', dtype=float, delimiter=',', skiprows=2, usecols=(17,18,19))

a.shape = a.size / no_of_dimensions, no_of_dimensions

point = ['0.000005', '0.000000', '0.000000']  ## cartesian co-ordinates for Sun - change it to include 
                                              ##                                  for any arbitrary point X(x,y,z)
point_arr = np.asarray(point, dtype = float)

from scipy.spatial import KDTree

tree = KDTree(a, leafsize=a.shape[0]+1)
distances, ndx = tree.query([point_arr], k=sys.argv[1])

print a[ndx]

