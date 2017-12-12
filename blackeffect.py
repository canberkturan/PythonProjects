from PIL import Image
import time
try:
    img=Image.open("baseimage.jpg","r")
except:
	print("File not found or broken")
	exit(1)
WIDTH, HEIGTH=img.size
LEVEL=60 #effect level
BLACK, WHITE=(0,0,0), (255,255,255)
for i in range(WIDTH):
	for j in range(HEIGTH):
		k=img.getpixel((i,j))
		print("{0}x{1}".format(i,j),end=" \r")
		if k[0]<LEVEL and k[1]<LEVEL and k[2]<LEVEL:
			img.putpixel((i,j),BLACK)
		else:
			img.putpixel((i,j),WHITE)
img.save(time.strftime("%d-%m-%Y_%H:%M:%S")+".jpg")
