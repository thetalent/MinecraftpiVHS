
# This program senses that a block has been hit.

# Import  modules
import mcpi.minecraft as minecraft
import mcpi.block as block
import time

# Connect to the Minecraft game
mc = minecraft.Minecraft.create()

# Work out the position of the player
x,y,z = mc.player.getTilePos()

# Move the diamond slightly away from the player position
x=x-1

# Build a diamond treasure block
mc.setBlock(x,y,z, block.DIAMOND_BLOCK.id)


  

# Game loop
while True:
  # Run the game loop once every second
  # Don't run it too fast or your computer might crash
  time.sleep(1)
  
  # Check to see if the diamond treasure has been hit
  events = mc.events.pollBlockHits()
  
  # Process each event in turn
  for e in events:
    # Get the coordinate that the hit happened at
    xevent, yevent,zevent  = e.pos
    
    # If the diamond was hit.... just an example
    #if xevent == x and yevent == y and zevent == z:     
     #mc.postToChat("HIT")

# END

