# Hier lernt Python die Minecraft-Befehle
from mcpi.minecraft import Minecraft
import mcpi.block as block


# Hier lernt Python z.B time.sleep()
import time

# Hier verbinden wir uns mit dem Minecraft-Spiel
mc = Minecraft.create()
mc.postToChat("Hello world")

# Hier beginnt die Spieleschleife
while True:
  x,y,z = mc.player.getPos()
  x = x-1
  mc.setBlock(x,y,z,block.FLOWER_YELLOW)
  time.sleep(1)
  
