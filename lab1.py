# Aiden Hammond, Sheev Patel, Tyler Haymens
# VPython Lab 
# Nov. 1, 2022

# Imports
import math
from vpython import *
import numpy as np

# VPython
scene = canvas(width=1450, height=700)

# range for arrows 
# creates a cube with side lengths = index
# centered at (0, 0, 0)
side_length = 20
index = range(side_length) 
half_side_length = floor(side_length/2)
field_range = range(-half_side_length, half_side_length)

# range for electrons
# defines the number of rings
num_circles = 4

# Scale factor
scale = 10**(-8)

# Constant
k = 8.98 * 10**(9)
charge = 1.602 * 10**(-19)

# Defines an electron
class Electron:
  
  def __init__(self, x, y, z):
    self.v = vector(x,y,z)
    self.sphere = sphere(pos=vector(x/scale,y/scale,0), radius=0.1, color=color.red)

  def distance_to(self, x, y, z):
    return vector(x,y,z) - self.v 
 
  def getElectricFieldAt(self, x, y, z):
    if (x==0 and y==0 and z==0):
      return vector(0,0,0)
    r = self.distance_to(x*scale,y*scale,z*scale)
    E = k * charge / mag(r)**2
    return E*r.hat

electrons = []

# Creates a disk of electrons 
def drawElectrons():
  # Creates array of electrons
  # Uses circular coordinates
  for r in range(0, num_circles):
    theta = 0
    while theta < 2*pi:
      x = r*cos(theta)*scale
      y = r*sin(theta)*scale
      electrons.append(Electron(x, y, 0))
      dTheta = pi/(4*r) if r else 2*pi
      theta += dTheta

drawElectrons()

# Define ranges for loops

# Initializing array using list comprehension syntax
electric_fields = [[[vector(0,0,0) for z in index] for y in index] for x in index]

# Computing electric field values 
# Loop
# Index is the index for the array of electric fields
# field_range holds the range of actual coordinates for the electric field 
for x,ex in zip(index, field_range): 
  for y,ey in zip(index, field_range):
    for z,ez in zip(index, field_range):
      # Sum up electric field for all of the electrons
      for electron in electrons:
        if (not (sqrt(ex**2 + ey**2) < num_circles and ez==0)):
          electric_fields[x][y][z] += electron.getElectricFieldAt(ex,ey,ez)

      E_Field = electric_fields[x][y][z]
      arrow_pos = vector(ex,ey,ez)
      a = arrow(pos=arrow_pos, axis=E_Field*scale)

# Bug in vpython for macos threading
while True: continue

