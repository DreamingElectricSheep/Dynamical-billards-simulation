# -*- coding: utf-8 -*-
"""
Created on Tue Mar  8 21:52:47 2022

@author: Limc8
"""

import pychrono.core as chrono
import pychrono.irrlicht as chronoirr
import matplotlib.pyplot as plt
import math


mysystem = chrono.ChSystemSMC() #Replace user with your account name for better visualization
chrono.SetChronoDataPath('C:/Users/user/anaconda3/pkgs/pychrono-7.0.0-py39_0/Library/data')


sph_mat = chrono.ChMaterialSurfaceSMC()


# Contact material for container
ground_mat = chrono.ChMaterialSurfaceSMC()

# Create the five walls of the rectangular container, using fixed rigid bodies of 'box' type
# Create the floor
floorBody = chrono.ChBodyEasyBox(5, 0.5, 3, 1000, True, True, ground_mat)# X, Z, Y
floorBody.SetPos(chrono.ChVectorD(0, -2, 0))
floorBody.SetBodyFixed(True)
floorBody.SetCollide(True)
mysystem.Add(floorBody)


# Create the front wall
front_wall = chrono.ChBodyEasyBox(5.99, 2, 1, 1, True, True, ground_mat)
front_wall.SetPos(chrono.ChVectorD(0, -1, -2))
front_wall.SetBodyFixed(True)
front_wall.SetCollide(True)
mysystem.Add(front_wall)

# Create the back wall
back_wall = chrono.ChBodyEasyBox(5.99, 2, 1, 1, True, True, ground_mat)
back_wall.SetPos(chrono.ChVectorD(0, -1, 2))
back_wall.SetBodyFixed(True)
back_wall.SetCollide(True)
mysystem.Add(back_wall)

# Create the left wall
wallBody1 = chrono.ChBodyEasyBox(1, 2, 5.99, 1, True, True, ground_mat)
wallBody1.SetPos(chrono.ChVectorD(-2.5, -1, 0))
wallBody1.SetBodyFixed(True)
wallBody1.SetCollide(True)

# Create the right wall
wallBody2 = chrono.ChBodyEasyBox(1, 2, 5.99, 1, True, True, ground_mat)
wallBody2.SetPos(chrono.ChVectorD(2.5, -1, 0))
wallBody2.SetBodyFixed(True)
wallBody2.SetCollide(True)

def original():
    # Create the left wall
    wallBody1 = chrono.ChBodyEasyBox(1, 2, 5.99, 1, True, True, ground_mat)
    wallBody1.SetPos(chrono.ChVectorD(-2.5, -1, 0))
    wallBody1.SetBodyFixed(True)
    wallBody1.SetCollide(True)

    # Create the right wall
    wallBody2 = chrono.ChBodyEasyBox(1, 2, 5.99, 1, True, True, ground_mat)
    wallBody2.SetPos(chrono.ChVectorD(2.5, -1, 0))
    wallBody2.SetBodyFixed(True)
    wallBody2.SetCollide(True)
    
    mysystem.Add(wallBody1)
    mysystem.Add(wallBody2)
    
    wallBody1.AddAsset(walls)
    wallBody2.AddAsset(walls)

# Extremum/edge case
def extreme():
    curved_left = chrono.ChBodyEasyCylinder(1000000, # Radius
                                     5, # Height
                                     1, # Density
                                     True, # Visualization
                                     True, # Collision
                                     ground_mat) # Contact material
    curved_left.SetPos(chrono.ChVectorD(1000002, 0, 0)) # X, Z, Y (x = r + 2)
    curved_left.SetBodyFixed(True)

    curved_right = chrono.ChBodyEasyCylinder(1000000, # Radius
                                     5, # Height
                                     1, # Density
                                     True, # Visualization
                                     True, # Collision
                                     ground_mat) # Contact material
    curved_right.SetPos(chrono.ChVectorD(-1000002, 0, 0)) # X, Z, Y (x = r + 2)
    curved_right.SetBodyFixed(True)
    
    mysystem.Add(curved_right)
    mysystem.Add(curved_left)
    
    curved_right.AddAsset(walls)
    curved_left.AddAsset(walls)

def curved1():
    curved_left = chrono.ChBodyEasyCylinder(14, # Radius
                                     5, # Height
                                     1, # Density
                                     True, # Visualization
                                     True, # Collision
                                     ground_mat) # Contact material
    curved_left.SetPos(chrono.ChVectorD(16, 0, 0)) # X, Z, Y
    curved_left.SetBodyFixed(True)

    curved_right = chrono.ChBodyEasyCylinder(14, # Radius
                                     5, # Height
                                     1, # Density
                                     True, # Visualization
                                     True, # Collision
                                     ground_mat) # Contact material
    curved_right.SetPos(chrono.ChVectorD(-16, 0, 0)) # X, Z, Y
    curved_right.SetBodyFixed(True)
    
    mysystem.Add(curved_right)
    mysystem.Add(curved_left)
    
    curved_right.AddAsset(walls)
    curved_left.AddAsset(walls)
    
def curved2():
    curved_left = chrono.ChBodyEasyCylinder(12, # Radius
                                     5, # Height
                                     1, # Density
                                     True, # Visualization
                                     True, # Collision
                                     ground_mat) # Contact material
    curved_left.SetPos(chrono.ChVectorD(14, 0, 0)) # X, Z, Y
    curved_left.SetBodyFixed(True)

    curved_right = chrono.ChBodyEasyCylinder(12, # Radius
                                     5, # Height
                                     1, # Density
                                     True, # Visualization
                                     True, # Collision
                                     ground_mat) # Contact material
    curved_right.SetPos(chrono.ChVectorD(-14, 0, 0)) # X, Z, Y
    curved_right.SetBodyFixed(True)
    
    mysystem.Add(curved_right)
    mysystem.Add(curved_left)
    
    curved_right.AddAsset(walls)
    curved_left.AddAsset(walls)
    
    
def curved3():
    curved_left = chrono.ChBodyEasyCylinder(10, # Radius
                                     5, # Height
                                     1, # Density
                                     True, # Visualization
                                     True, # Collision
                                     ground_mat) # Contact material
    curved_left.SetPos(chrono.ChVectorD(12, 0, 0)) # X, Z, Y
    curved_left.SetBodyFixed(True)

    curved_right = chrono.ChBodyEasyCylinder(10, # Radius
                                     5, # Height
                                     1, # Density
                                     True, # Visualization
                                     True, # Collision
                                     ground_mat) # Contact material
    curved_right.SetPos(chrono.ChVectorD(-12, 0, 0)) # X, Z, Y
    curved_right.SetBodyFixed(True)
    
    mysystem.Add(curved_right)
    mysystem.Add(curved_left)
    
    curved_right.AddAsset(walls)
    curved_left.AddAsset(walls)
    
def curved4():
    curved_left = chrono.ChBodyEasyCylinder(8, # Radius
                                     5, # Height
                                     1, # Density
                                     True, # Visualization
                                     True, # Collision
                                     ground_mat) # Contact material
    curved_left.SetPos(chrono.ChVectorD(10, 0, 0)) # X, Z, Y
    curved_left.SetBodyFixed(True)

    curved_right = chrono.ChBodyEasyCylinder(8, # Radius
                                     5, # Height
                                     1, # Density
                                     True, # Visualization
                                     True, # Collision
                                     ground_mat) # Contact material
    curved_right.SetPos(chrono.ChVectorD(-10, 0, 0)) # X, Z, Y
    curved_right.SetBodyFixed(True)
    
    mysystem.Add(curved_right)
    mysystem.Add(curved_left)
    
    curved_right.AddAsset(walls)
    curved_left.AddAsset(walls)

def curved5():
    curved_left = chrono.ChBodyEasyCylinder(6, # Radius
                                     5, # Height
                                     1, # Density
                                     True, # Visualization
                                     True, # Collision
                                     ground_mat) # Contact material
    curved_left.SetPos(chrono.ChVectorD(8, 0, 0)) # X, Z, Y
    curved_left.SetBodyFixed(True)

    curved_right = chrono.ChBodyEasyCylinder(6, # Radius
                                     5, # Height
                                     1, # Density
                                     True, # Visualization
                                     True, # Collision
                                     ground_mat) # Contact material
    curved_right.SetPos(chrono.ChVectorD(-8, 0, 0)) # X, Z, Y
    curved_right.SetBodyFixed(True)
    
    mysystem.Add(curved_right)
    mysystem.Add(curved_left)
    
    curved_right.AddAsset(walls)
    curved_left.AddAsset(walls)



# Optional, attach  textures for better visualization
mtexturewall = chrono.ChTexture()
mtexturewall.SetTextureFilename(chrono.GetChronoDataFile("/textures/blue.png"))
wallBody1.AddAsset(mtexturewall)
front_wall.AddAsset(mtexturewall)
back_wall.AddAsset(mtexturewall)
floorBody.AddAsset(mtexturewall)

mtexture = chrono.ChTexture()
mtexture.SetTextureFilename(chrono.GetChronoDataFile("/textures/red.png"))

dark_red = chrono.ChTexture()
dark_red.SetTextureFilename(chrono.GetChronoDataFile("/textures/dark red.png"))

bright_red = chrono.ChTexture()
bright_red.SetTextureFilename(chrono.GetChronoDataFile("/textures/bright red.png"))

walls = chrono.ChTexture()
walls.SetTextureFilename(chrono.GetChronoDataFile("/textures/orange.png"))



# Create the sphere
sphere = chrono.ChBodyEasySphere(0.25,      # radius size
                                      1000,     # density
                                      True,     # visualization?
                                      True,     # collision?
                                      sph_mat)  # contact material

sphere.AddAsset(mtexture)

#Initial position
sphere.SetPos(chrono.ChVectorD(0, -1.56, 0)) # X, Z, Y
sphere.GetCollisionModel().SetFamily(1)
sphere.GetCollisionModel().SetFamilyMaskNoCollisionWithFamily(1)
mysystem.Add(sphere)


# Initial velocity
sphere.SetWvel_par(chrono.ChVectorD(15, 0, -15)) #Y, Z, -X


# Which wall
curved1()



myapplication = chronoirr.ChIrrApp(mysystem, 'Chaotic billards', chronoirr.dimension2du(1024,768))

myapplication.AddTypicalSky()
myapplication.AddTypicalLogo(chrono.GetChronoDataFile('logo_pychrono_alpha.png'))
myapplication.AddTypicalCamera(chronoirr.vector3df(0, 10 , -10))
myapplication.AddTypicalLights()

           

myapplication.AssetBindAll();

           

myapplication.AssetUpdateAll();


# ---------------------------------------------------------------------
#
#  Run the simulation
#



myapplication.SetTimestep(0.005)  # 'Refreshes' 200 times every second
myapplication.SetTryRealtime(False)

array_time = []
array_x = []
array_y = []
array_z = []
array_speed = []



while(myapplication.GetDevice().run()):
    array_time.append(mysystem.GetChTime())
    array_y.append(sphere.GetPos().x)
    array_x.append(sphere.GetPos().z)
    array_z.append(sphere.GetPos().y)
    array_speed.append(math.sqrt((sphere.GetPos_dt().x)**2 + (sphere.GetPos_dt().z)**2))
    
    
    myapplication.BeginScene()
    myapplication.DrawAll()
    myapplication.DoStep()
    myapplication.EndScene()
    
    if mysystem.GetChTime() >= 180: # Time the simulation runs for
          myapplication.GetDevice().closeDevice()



# Plotting the trajectory of the ball
plt.plot(array_y, array_x, 'g', linewidth = '0.5')
    
plt.title("Original over 30 seconds")
plt.xlabel='x position [m]'
plt.ylabel='y posistion [m]'
plt.grid()

plt.show()