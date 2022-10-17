import pygame
import math
class Ray :
	def __init__(self,pos,target_x,target_y,screen):
		self.cord = pygame.math.Vector2(pos)
		self.dir = pygame.math.Vector2(self.cord.x , self.cord.y - 10)
		self.target_x = target_x
		self.target_y = target_y
		
				
	def check( self,wall):
		x1 = wall.x.x
		y1 = wall.x.y
		x2 = wall.y.x
		y2 = wall.y.y
		
		x3 = self.cord.x
		y3 = self.cord.y
		x4 = self.target_x
		y4 = self.target_y
		
		
		den = (x1 - x2)*(y3 - y4) - (y1 - y2)*(x3 - x4)
		
		if(den == 0):
			return 
		t = ((x1-x3)*(y3 - y4) - (y1-y3)*(x3-x4))/den
		u = -((x1-x2)*(y1-y3)-(y1-y2)*(x1-x3))/den
		
		if (t > 0 and t<1 and u >0):
			pt = pygame.math.Vector2()
			pt.x = x1 + t*(x2 - x1)
			pt.y = y1 + t*(y2 - y1)
			return pt

	def show(self,screen):
		line_color = (255,255,255)
		pygame.draw.line(screen,line_color,(self.cord.x , self.cord.y ),(self.target_x , self.target_y),1)
