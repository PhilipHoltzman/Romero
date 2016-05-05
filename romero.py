import pygame

pygame.init()

# pallette 
turquoise1 = (0,245,255)
turquoise2 = (0,229,238)
turquoise3 = (0,197,205)
turquoise4 = (0,134,139)
black = (0,0,0)
white = (255,255,255)

gameDisplay = pygame.display.set_mode((800,600))
pygame.display.set_caption('Snakemero')



gameExit = False

lead_x = 300
lead_y = 300
lead_x_change = 0
lead_y_change = 0

clock = pygame.time.Clock()

while not gameExit:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			gameExit = True

		if event.type == pygame.KEYDOWN:
			# x axis movement
			if event.key == pygame.K_LEFT:
				lead_x_change = -6
				lead_y_change = 0
			elif event.key == pygame.K_RIGHT:
				lead_x_change = 6
				lead_y_change = 0

			# y axis movement
			elif event.key == pygame.K_UP:
				lead_y_change = -6
				lead_x_change = 0
			elif event.key == pygame.K_DOWN:
				lead_y_change = 6
				lead_x_change = 0

	# Stop code for non endless moving mode
	#	if event.type == pygame.KEYUP:
	#		if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
	#			lead_x_change = 0
	#	if event.type == pygame.KEYUP:
	#		if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
	#			lead_y_change = 0

	if lead_x >= 800 or lead_x < 0 or lead_y >= 600 or lead_y <0:
		gameExit = True

	lead_x += lead_x_change
	lead_y += lead_y_change


	gameDisplay.fill(black)
	pygame.draw.rect(gameDisplay,turquoise4,[lead_x,lead_y,10,10])
	pygame.display.update()

	clock.tick(15)


pygame.quit()
quit()