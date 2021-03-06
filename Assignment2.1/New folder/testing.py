# -*- coding: utf-8 -*-
"""
Created on Sun Feb 25 00:43:43 2018

@author: aldos
"""
from bs4 import BeautifulSoup
from urllib.request import urlopen
import json
        
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
np.random.seed(19680801)


x = [17, 18, 19, 20, 21, 23, 24, 25, 27, 28, 29, 30, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 86, 87] 
y = [392.16, 12.08, 0.25, 1918000.0, 12784.31, 148.35, 0.0, 1.39, 1.85, 68.62, 855.96, 1482.49, 20047.67, 16.11, 13732000.0, 154164.02, 40.72, 2636.18, 24052304.67, 53.25, 3.09, 262264.74, 950706.87, 7.26, 49292879.5, 2496.67, 41676.14, 522.94, 39776299.97, 198935.51, 3135385.13, 808013.57, 137061.97, 2616875.25, 6958.73, 4004731.97, 9702316.28, 48104.19, 12029823.62, 1182819.81, 229582.23, 6031.27, 3980433.97, 319362.32, 74661.68, 17341.6, 360000.0, 556.48, 50159.9, 11878.59, 12221.26, 447.25, 0.49, 56099.98, 469457.55, 6157.6, 0.0, 17275.5, 48.58, 10135294.49, 742499.31, 2353.64, 640.3, 3799894.8, 12782.37, 6990045.27]
 
 

plt.scatter(x, y, c="g", alpha=0.5, marker='o')
plt.locator_params(axis='y', nticks=1000)
plt.xlabel("Leprechauns")
plt.ylabel("Gold")
plt.legend(loc=2)
plt.show()