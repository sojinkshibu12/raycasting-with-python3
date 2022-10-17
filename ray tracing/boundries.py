
import pygame
class boundries:
	def __init__(self,x1,x2,y1,y2):
		self.x = pygame.math.Vector2(x1,x2)
		self.y = pygame.math.Vector2(y1,y2)
		
	def draw(self, screen):
		line_color = (255,255,255)
		pygame.draw.line(screen,line_color, (self.x.x, self.x.y), (self.y.x, self.y.y),1)
