# -*- coding: utf-8 -*-
"""
Created on Tue May 17 11:17:52 2022

@author: limc8
"""

import pychrono.core as chrono
import pychrono.irrlicht as chronoirr
import matplotlib.pyplot as plt
import math

mysystem = chrono.ChSystemSMC() #Set 'user' to your username for better visualization
chrono.SetChronoDataPath('C:/Users/user/anaconda3/pkgs/pychrono-7.0.0-py39_0/Library/data')

sph_mat = chrono.ChMaterialSurfaceSMC()
ground_mat = chrono.ChMaterialSurfaceSMC()

floorBody = chrono.ChBodyEasyBox(35, 0.5, 35, 1000, True, True, ground_mat) # X, Z, Y
floorBody.SetPos(chrono.ChVectorD(0, -2, 0))
floorBody.SetBodyFixed(True)
floorBody.SetCollide(True)
mysystem.Add(floorBody)

back_wall = chrono.ChBodyEasyBox(20, 2, 1, 1, True, True, ground_mat)
back_wall.SetPos(chrono.ChVectorD(0, -1, 2))
back_wall.SetBodyFixed(True)
back_wall.SetCollide(True)
mysystem.Add(back_wall)

# Skins/color
mtexturewall = chrono.ChTexture()
mtexturewall.SetTextureFilename(chrono.GetChronoDataFile("/textures/blue.png"))
back_wall.AddAsset(mtexturewall)
floor = chrono.ChTexture()
floor.SetTextureFilename(chrono.GetChronoDataFile("/textures/orange.png"))
floorBody.AddAsset(floor)
mtexture = chrono.ChTexture()
mtexture.SetTextureFilename(chrono.GetChronoDataFile("/textures/red.png"))


sphere = chrono.ChBodyEasySphere(0.25,      # radius size
                                      1000,     # density
                                      True,     # visualization?
                                      True,     # collision?
                                      sph_mat)  # contact material

sphere.AddAsset(mtexture)

#Initial position
sphere.SetPos(chrono.ChVectorD(0, -1.56, 0)) # X, Z, Y
mysystem.Add(sphere)

sphere.SetWvel_par(chrono.ChVectorD(15, 0, -12)) #Y, Z, -X


myapplication = chronoirr.ChIrrApp(mysystem, 'Collision simulation', chronoirr.dimension2du(1024,768))

myapplication.AddTypicalSky()
myapplication.AddTypicalLogo(chrono.GetChronoDataFile('logo_pychrono_alpha.png'))

# Change the middle number to change the zoom amount
myapplication.AddTypicalCamera(chronoirr.vector3df(0, 10, -0.0000000001))
myapplication.AddTypicalLights()

   

myapplication.AssetBindAll();

        
myapplication.AssetUpdateAll();
    

# ---------------------------------------------------------------------
#
#  Run the simulation
#



myapplication.SetTimestep(0.005)  # 'Refreshes' 200 times every second
myapplication.SetTryRealtime(True)

array_time = []
array_x = []
array_y = []
array_z = []
array_speed = []


while(myapplication.GetDevice().run()):
    array_time.append(mysystem.GetChTime())
    array_x.append(sphere.GetPos().x)
    array_y.append(sphere.GetPos().z)
    array_z.append(sphere.GetPos().y)

    

    myapplication.BeginScene()
    myapplication.DrawAll()
    myapplication.DoStep()
    myapplication.EndScene()
    
    if mysystem.GetChTime() >= 5:
          myapplication.GetDevice().closeDevice()
          

def collision_point(array):
    i = 5
    turning_point = False
    while i < len(array) and turning_point == False:
        # Average of before and after for consistency
        before_num_avg = 0
        after_num_avg = 0
        before_num_avg += array[i - 1]
        before_num_avg += array[i - 2]
        before_num_avg += array[i - 3]
        before_num_avg += array[i - 4]
        before_num_avg += array[i - 5]
        
        after_num_avg += array[i]
        after_num_avg += array[i + 1]
        after_num_avg += array[i + 2]
        after_num_avg += array[i + 3]
        after_num_avg += array[i + 4]    
        
        before_num_avg = before_num_avg / 5
        after_num_avg = after_num_avg / 5
        
        if after_num_avg < before_num_avg:
            turning_point = True
        else:
            i += 1
    return i

def find_angle_before(array_x, array_y, i):
    x1 = 0
    y1 = 0
    x2 = 0
    y2 = 0
    
    ii = 0
    while ii < 5:
        x1 += array_x[ii]
        y1 += array_y[ii]
        x2 += array_x[i - ii]
        y2 += array_y[i - ii]
        ii += 1
    # Finding the gradient using y-step/ x-step
    hyp = math.sqrt((y2 - y1)**2 + (x2 - x1)**2)
    adj = x2 - x1
    theta = math.degrees(math.acos(adj/hyp))
    return theta

def find_angle_after(array_x, array_y, i):
    x1 = 0
    y1 = 0
    x2 = 0
    y2 = 0
    
    ii = 0
    while ii < 5:
        x1 += array_x[i + ii]
        y1 += array_y[i + ii]
        x2 += array_x[len(array_x) - (ii + 1)]
        y2 += array_y[len(array_y) - (ii + 1)]
        ii += 1
    # Finding the gradient using y-step/ x-step
    hyp = math.sqrt((y2 - y1)**2 + (x2 - x1)**2)
    
    adj = x2 - x1
    #print(adj, hyp)
    theta = math.degrees(math.acos(adj/hyp))
    return theta
    

i = collision_point(array_y)
theta1 = find_angle_before(array_x, array_y, i) 
theta2 = find_angle_after(array_x, array_y, i)
print("---Results for collision---")
print("The point of collision is at i =", i)
print("At time =", i /200, "seconds")

print("")
print("The initial angle was:", theta1)
print("The resultant angle was:", theta2)


# Plotting the trajectory of the ball
plt.plot(array_time, array_y, 'g', linewidth = '0.5')
    
plt.title("Plot of collision")
plt.xlabel='x position [m]'
plt.ylabel='y posistion [m]'
plt.grid()

plt.show()