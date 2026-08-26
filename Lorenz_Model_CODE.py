#Lorenz model

#Tim August
# 4 / 14 / 26

#Model for atmospheric convection

#Variables in the system:
    #x: fluid flow rate (or convection rate)
    #y: temperature difference
    #z: effects of the nonlinear vertical temperature profile

#The governing equations change over time:
    #dx_dt = sigma*(y - x)
    #dy_dt = x*(rho - z) - y
    #dz_dt = x*y - beta *z

#Here:
    #sigma is the Prandtl number -> it is a ratio of diffusivities
    #rho is the Rayleigh number -> associated with the buoyancy
    #beta refers to the system dimensions

#__________________________________________________________________________________________________________________________________
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d

#__________________________________________________________________________________________________________________________________
#Model parameters:
#This is the time step, dt
dt = 0.01

#This is the time variable
time = np.arange(0, 30, dt)

#x, y, and z 
x = 1 #convection rate
y = 1 #temp diff
z = 1 #nonlinear vertical temp profile

#Constants sigma, rho, and beta can be altered to examine different system behavior
    #Lorenz uses sigma = 10, rho = 28, beta = 8/3

sigma = 10
rho = 28
beta = 8/3

#__________________________________________________________________________________________________________________________________
#This loop can step it forward in time
x_values = []
y_values = []
z_values = []

for t in time:

    #Current state:
    x_values.append(x)
    y_values.append(y)
    z_values.append(z)

    #Derivatives:
    dx_dt = sigma*(y - x) 
    dy_dt = (x*(rho - z) - y) 
    dz_dt = (x * y - beta * z) 

    #Time step: forward Euler
    x += dx_dt * dt
    y += dy_dt * dt
    z += dz_dt * dt
    

x_array = np.array(x_values)
y_array = np.array(y_values)
z_array = np.array(z_values)

#Distance track -> **See README.md**
#distance = np.sqrt((x1_array - x2_array)**2 + (y1_array - y2_array)**2 + (z1_array - z2_array)**2)

#Plotting
fig = plt.figure()
ax = plt.axes(projection = "3d")

ax.plot3D(x_array, y_array, z_array)

#The axis limits may need adjustment depending on the parameters chosen
ax.set_xlim(-25, 25)
ax.set_ylim(-25, 25)
ax.set_zlim(0, 50)

plt.title("Lorenz Attractor Output")

plt.show()
