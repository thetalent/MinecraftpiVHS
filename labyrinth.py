# Hier lernt Python die Minecraft-Befehle
from mcpi.minecraft import Minecraft
import mcpi.block as block


# Hier lernt Python z.B time.sleep()
import time


maze = open("/home/pi/maze",'r')



# Hier verbinden wir uns mit dem Minecraft-Spiel
mc = Minecraft.create()
mc.postToChat("Hello world")
mc.player.setting("autojump", False)
x,y,z = mc.player.getTilePos()

x = x+1
xa,ya,za = x,y,z
mc.setBlocks(x,y-5,z,x+100,y+5,z+100,block.AIR.id)
y= y -1
mc.setBlocks(x,y,z,x+100,y,z+100,block.GRASS.id)

x,y,z = xa,ya,za  

time.sleep(5)
 
for row in maze:
    for col in row:
        for i in range(3):
            if col == 'x':
                mc.setBlock(x,y+i,z,block.WOOL.id,i)                        
            else:
                mc.setBlock(x,y+i,z,block.AIR.id)
        x = x+1
    x = xa
    z = z+1


mc.postToChat("Labyrinth gebaut")

 

# Hier beginnt die Spieleschleife
#while True:
#  pass




