from PIL import Image
import time
try:
	img=Image.open("baseimage.jpeg","r")
	k=img.load()
except:
	print("File not found or broken")
	exit(1)
WIDTH, HEIGTH=img.size
LEVEL=75 #effect level
BLACK, WHITE=(0,0,0), (255,255,255)
for i in range(WIDTH):
	for j in range(HEIGTH):
		c=k[i,j]
		if c[0]<LEVEL and c[1]<LEVEL and c[2]<LEVEL:
			k[i,j]=BLACK
		else:
			k[i,j]=WHITE
img.save(time.strftime("%d-%m-%Y_%H:%M:%S")+".jpg")
print("New Image Saved!")
