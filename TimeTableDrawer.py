from PIL import Image, ImageDraw
import math
class TimeTable:
	def __init__(self,rot=0,size=1080,color=(255,255,255)):
		self.img = Image.new("RGB",(size,size),"black")
		self.size = size
		self.rot = rot
		self.color = color
		self.drawCircle()
		
	def drawCircle(self):
		draw = ImageDraw.Draw(self.img)
		draw.ellipse((20,20,self.size-20,self.size-20),
		                       outline=self.color)
		
	def drawLine(self,xy0,xy1):
		draw = ImageDraw.Draw(self.img)
		draw.line((xy0[0],xy0[1],xy1[0],xy1[1]),fill=self.color)
		
	def setColor(self,color):
		self.color = color
		
	def fillLines(self,dotTable,dotCount,multiplier):
		if dotTable==[]:
			return
		k = 0
		while k<multiplier:
			for i in range(len(dotTable)):
				self.drawLine(dotTable[i],
				     dotTable[int(i*multiplier)%dotCount])
			k += 1
			
	def calculateDots(self,dotCount,rot):
		if dotCount == 0:
			return []
		dotTable = []
		r = self.size/2 - 20
		angle = (2*math.pi)/dotCount
		rot = rot * (math.pi/180)
		for i in range(dotCount):
			dotX = r*math.cos(angle*i+rot) + self.size/2
			dotY = r*math.sin(angle*i+rot) + self.size/2
			dotTable.append((dotX,dotY))
		return dotTable
		
	def createTable(self,dotCount,mult,rot = 0):
		dots = self.calculateDots(dotCount,rot)
		self.fillLines(dots,dotCount,mult)
		
	def clear(self):
		self.img = Image.new("RGB",(self.size,self.size),"black")
		
	def save(self,name = "lastTable.png"):
		self.img.save(name)
		
if __name__ == "__main__":
	t = TimeTable(rot=180,size=2160,color=(0,255,255))
	t.createTable(200,2)
	t.save()