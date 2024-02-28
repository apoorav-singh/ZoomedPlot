# -*- coding: utf-8 -*-
"""
Created on Wed Feb 28 13:39:24 2024

@author: Apoorav
"""

import numpy as np
from matplotlib import pyplot as plt
# import scienceplots
from mpl_toolkits.axes_grid1.inset_locator import zoomed_inset_axes
from mpl_toolkits.axes_grid1.inset_locator import mark_inset

# plt.style.use('science')

fig, ax = plt.subplots()
axins = zoomed_inset_axes(ax, 5, loc=4) # zoom = 6


def f(m, c, x):
    return m*x + c



x = np.arange(-np.pi/2 + 0.1, np.pi/2 - 0.1, 0.01)
slope = 1
intercept = 0
y = f(slope, intercept, x)
TanPlot = np.tan(x)
SinPlot = np.sin(x)
ax.plot(x, y, "--", label="y = m*x")
ax.plot(x, TanPlot, "--", label="tan(x)")
ax.plot(x, SinPlot, "--", label="sin(x)")
ax.set_xlabel("x", fontsize=18)
ax.set_ylabel("y", fontsize=18)
ax.grid("major")
ax.legend(loc=2)

#-------- Zoomed Plot -----------

axins.plot(x, y, "--", label="y = m*x")
axins.plot(x, TanPlot, "--", label="tan(x)")
axins.plot(x, SinPlot, "--", label="sin(x)")
axins.set_xlim(0.7, 0.9) # Limit the region for zoom in x-axis
axins.set_ylim(0.2, 1.5) # Limit the region for zoom in y-axis
mark_inset(ax, axins, loc1=2, loc2=4, fc="none", ec="0.1")
axins.legend(loc=3)



   


plt.show()