import pygame
import math
from ray import Ray
class particle(Ray):
	def __init__(self,screen):
		x, y = pygame.mouse.get_pos()
		self.pos = pygame.math.Vector2((x,y))
		self.screen = screen
		self.rayarr = []
	def create(self):
		for i in range(0,360,10):
			
			target_x = self.pos.x - math.sin(i)*10
			target_y = self.pos.y + math.cos(i)*10
			self.rayarr.append(Ray(self.pos,target_x,target_y,self.screen))
						
		return self.rayarr
            
		
	def look(self,wallarr ):
		line_color = (255,255,255)
		for ray in self.rayarr:
			closest = None
			record = math.inf
			for wall in wallarr:
				pt = ray.check(wall)
				if(pt):
					d = math.dist(self.pos , pt)
					if (d<record):
						record = d
						closest = pt
			if(closest):
				pygame.draw.line(self.screen,line_color,(self.pos.x , self.pos.y ),(closest.x , closest.y),1)
					

