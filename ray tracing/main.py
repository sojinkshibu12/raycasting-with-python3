import pygame
import random
from boundries import boundries
from ray import Ray
from particle import particle
screen  = pygame.display.set_mode((600,600))
background_color = (0,0,0)


pygame.display.flip()
running = True
#b = boundries(300,100,300,400)
screenrect = pygame.Rect((0,0),(600,600))
wallarr = []

for i in range(6):
	x1 = random.randint(0,600)
	y1 = random.randint(0,600)
	x2 = random.randint(0,600)
	y2 = random.randint(0,600)
	wallarr.append(boundries(x1,x2,y1,y2))
	

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
    screen.fill(background_color)
    player = particle(screen)
    arrayray = player.create()

    for wall in wallarr:
        wall.draw(screen)
    for ray in arrayray:
        ray.show(screen)
	    
    player.look(wallarr)
    pygame.display.update()
