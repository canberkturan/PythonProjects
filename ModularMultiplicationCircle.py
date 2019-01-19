from PIL import Image, ImageDraw
import math

"""
   Before Run:
       -Install PIL(pillow) library -> pip3 install pillow
"""


class TimeTable:
	def __init__(self, rot=0, size=1080, bg=(0, 0, 0),
							color=(255, 255, 255), padding=20):
		self.img = Image.new("RGB", (size, size), bg) # empty image
		self.size = size #image size
		self.rot = rot #rotate (degree)
		self.bg = bg #background of image -> (r,g,b) 0-255
		self.color = color #color of lines -> (r,g,b) 0-255
		self.padding = padding #padding the circle from frame
		self.drawCircle() #draw a empty circle
		
	def drawCircle(self):
		"""
		This function draws an empty circle with initial
		parameters
		"""
		draw = ImageDraw.Draw(self.img)
		draw.ellipse((self.padding, self.padding,
			self.size - self.padding, self.size - self.padding),outline=self.color)
		
	def drawLine(self, xy0, xy1):
		"""
		This function draws a line with
		xy0 ->(X-start, Y-start) 
		xy1 ->(X-end, Y-end)
		parameters must be tuple or list type
		"""
		draw = ImageDraw.Draw(self.img)
		draw.line((xy0[0], xy0[1], xy1[0], xy1[1]), fill=self.color)
		
	def fillLines(self, dotTable, dotCount, multiplier):
		"""
		This function calls drawLine function 
		to draw with every dots and their calculated dots
		"""
		if dotTable is None:
			return False

		for i in range(len(dotTable)):
			self.drawLine(dotTable[i], dotTable[int(i * multiplier) % dotCount])
		return True

	def calculateDots(self, dotCount):
		"""
		This function calculates dots around the circle
		"""
		if dotCount == 0:
			return None

		dotTable = [] 
		r = self.size / 2 - self.padding # radius
		angle = (2 * math.pi) / dotCount # angle between two dots
		rot = self.rot * (math.pi / 180) # degree to radians
		
		for i in range(dotCount):
			dotX = r*math.cos(angle*i+rot) + self.size/2
			dotY = r*math.sin(angle*i+rot) + self.size/2
			dotTable.append((dotX,dotY))
		return dotTable
		
	def createTable(self, dotCount, mult):
		"""
		This function calls calculateDots and fillLines, and
		prints an exit message
		dotCount -> takes a value how many dots will be around the circle
		multiplier -> takes a value that will be multiply with indexes of dots
		"""
		dots = self.calculateDots(dotCount)
		exit_code = self.fillLines(dots, dotCount, mult)
		exit_message = "Success!" if exit_code else "Fail!"
		print(exit_message)

	def clear(self):
		"""
		This function clears the image
		"""
		self.img = Image.new("RGB", (self.size, self.size), self.bg)

	def save(self, path = "lastTable.png"):
		"""
		This function saves the image with path parameter
		"""
		self.img.save(path)

if __name__ == "__main__":
	t = TimeTable(rot=180, size=2160, color=(200, 0, 0),bg=(255, 255, 255))
	t.createTable(300, 2)
	t.save()
	    
	    
	    
