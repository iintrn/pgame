import pygame

pygame.init()
screen = pygame.display.set_mode((600, 500))
done = False
warna_bg = (60, 100, 100)

pygame.display.set_caption("Hallo APP")

while not done:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True
		if event.type == pygame.KEYDOWN and \
	event.key == pygame.K_ESCAPE:
			done = True

	screen.fill(warna_bg)
	pygame.draw.line(screen,(22, 198, 12),(0, 0),(300, 300))
	pygame.draw.line(screen,(255, 0, 0),(300, 300),(600, 400))
	pygame.display.flip()