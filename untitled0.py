# -*- coding: utf-8 -*-
"""
Created on Fri Jan 24 07:01:46 2020

@author: USER
"""
from pylab import *
import numpy as np

m = np.linspace(0, 60, 60)
z = m.reshape(10, 6)
imshow(z)
show()