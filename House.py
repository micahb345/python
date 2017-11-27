from mcpi.minecraft import Minecraft
from mcpi import block
from time import sleep

def init(): 
	# change 192.168.1.13 to 127.0.0.1 or your ip
	mc = Minecraft.create("10.183.4.125", 4711)
	x, y, z = mc.player.getPos()  
	return mc

#main  
def main():
	mc = init()
	#mc.player.setPos(34, 45, 100)
	x, y, z = mc.player.getPos()  
	mc.setBlocks(x-1, y,   z+2, x+11, y+5, z+15, 5)
	mc.setBlock(x-1,  y,   z+1, x+11, y+1, z+12, 0)
	mc.setBlocks(x-1, y+3, z+1, x+11, y+1, z+7,  5)
	mc.setBlock( x-2, y+3, z,   x+11, y+4, z+11,  0)
	mc.setBlock(x+4,  y-2, z-1, x+9,  y+3, z+10, 0)
	mc.setBlocks(x+4, y+1, z+7, x+7,  y+3, z+9, 20)
	mc.setBlock(x+3,  y+4, z+1, x+11, y+3,   z+12, 0)
	mc.postToChat("#WeAreGettingCarried")
	
	for y in range(0, 1):
		
		while True:
			y = 1
	if 0>1:
		y = 1

main()
