import os
import sys
sys.path.append('../../utils/')

import numpy as np
import netCDF4 as nc
import SCM_utils as utils

import time

rep_images = './images/check_old/'

if not(os.path.exists(rep_images)):
    os.makedirs(rep_images)

data0 = {}

f = nc.Dataset('../ARMCU_REF_1D.nc','r')

for var in f.variables:
    if not(var in f.dimensions) and (f[var].ndim <= 3 or f[var][:].shape[0] == 1):
        print var
        data0[var] = utils.read(var,f)

f.close()

data = {}

f = nc.Dataset('ARMCu_driver_RR_new3.nc','r')

for var in f.variables:
    if not(var in f.dimensions) and not(var in ['bounds_lat','bounds_lon']) and (f[var].ndim <= 3  or f[var][:].shape[0] == 1):
        print var
        data[var] = utils.read(var,f)
        #data[var].info()
        if data0.has_key(var):
            data0[var].plot(rep_images=rep_images,var2=data[var],label="SCM-enabled",label2="old")

f.close()
