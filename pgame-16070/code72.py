# Pemrograman Game Praktikum 7
# latihan code 7.1 : PyGame

import pygame, sys
from pygame.locals import *

pygame.init()

DISPLAYSURF = pygame.display.set_mode((700, 500))

pygame.display.set_caption('NAMA SAYA : IIN TARNO')

while True: # main game loop
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
		sys.exit()
		pygame.display.update()