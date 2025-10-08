#! python3
#
# Surface area of a cone
# Find the surface area of a cone given the height and the radius.
# You will need to ask the user to enter in both variables, and will 
# need to use the Pythagorean relationship to find the slant height. 
# (2 points)
#
# Inputs:
# height, radius
#
# Outputs:
# surface area
#
# Test output
# r = 3
# h = 5
# sa = 83.2297607912
# the formula for As is (pi*(r**2)) + (pi*r*s)
# s sqrrt(r**2+h**2)

import math
r = float(input("whats the value of the radius"))
h = float(input("whats the height of your cone"))
s = float((r**2)+(h**2))**(1/2)
As = (math.pi*(r**2)) + (math.pi*r*s)
print(f" The As of your cone is  {As}")

