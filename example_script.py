#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep  5 13:23:11 2020

@author: anonymous
"""

# Python3 Script to read and plot example of Era 5 SST


from netCDF4 import Dataset as ncfile
import numpy as np
from matplotlib.colors import BoundaryNorm
import matplotlib.pyplot as plt
import cartopy

# -------------------------
# LOAD DATA: 
# -------------------------
fil = ncfile('./e5.moda.an.sfc.128_034_sstk.ll025sc.2018010100_2018120100.nc','r')
lat = fil.variables['latitude'][:]
lon = fil.variables['longitude'][:] 
sst = fil.variables['SSTK'][:,:,:] - 273.15 # SST in Degrees C  

# -------------------------
# PLOT January 2018 Sea Surface Temperature 
# -------------------------
#
map_proj = cartopy.crs.LambertCylindrical(central_longitude=200.0)
LAND_highres = cartopy.feature.NaturalEarthFeature('physical', 'land', '50m', edgecolor='face', facecolor = 'black', linewidth=.1)

fig, axs = plt.subplots(1,1, figsize=(10, 3), facecolor='w', edgecolor='k')
axs = plt.subplot(1, 1, 1, projection = map_proj)
axs.add_feature(LAND_highres)
axs.set_title('Era5 SST ($^\circ$C): January 2018', fontsize = 12)
cs = axs.pcolormesh(lon, lat, sst[1,:,:], transform = cartopy.crs.PlateCarree(), norm = BoundaryNorm(np.linspace(0, 30, 31), 256), cmap = 'rainbow')
cbar_ax = fig.add_axes([0.91, 0.2, 0.02, 0.6])
fig.colorbar(cs, cax=cbar_ax)
plt.show()

