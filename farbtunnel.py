# Hier lernt Python die Minecraft-Befehle
from mcpi.minecraft import Minecraft

# Hier lernt Python Button
from gpiozero import Button

# Hier lernt Python z.B time.sleep()
import time

mc = Minecraft.create()
mc.postToChat("Hello world")

x,y,z = mc.player.getPos()
x = x+1


for j in range(50):
    farbe = j
    for i in range(5):
        x = x + 1
        mc.setBlock(x,y,z,35, farbe)
    for i in range(4):
        z = z + 1
        mc.setBlock(x,y,z,35, farbe)
    for i in range(5):
        x = x - 1
        mc.setBlock(x,y,z,35, farbe)
    for i in range(4):
        z = z - 1
        mc.setBlock(x,y,z,35, farbe)
    y = y + 1
    
    
        

