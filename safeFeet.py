# Adventure 4: safeFeet.py

# From the book: "Adventures in Minecraft"
# written by David Whale and Martin O'Hanlon, Wiley, 2014
# http://eu.wiley.com/WileyCDA/WileyTitle/productCd-111894691X.html
#
# This program works out if your feet are safe or not.
# If you are in the air or in water, your feet are not safe.

# Import necessary modules
import mcpi.minecraft as minecraft
import mcpi.block as block
import time

# Connect to the Minecraft game
mc = minecraft.Minecraft.create()

#

# Spieleschleife
while True:  
  time.sleep(0.5)
  x,y,z = mc.player.getTilePos()
  y=y-1
  b = mc.getBlock(x,y,z)  
  if b == block.AIR.id or b == block.WATER_STATIONARY.id or b == block.WATER_FLOWING.id:
    mc.setBlock(pos.x, pos.y-1, pos.z, block.GLASS.id)
 
# END
  
