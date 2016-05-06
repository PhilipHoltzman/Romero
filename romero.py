import pygame
import time
import random


pygame.init()

# pallette 
turquoise1 = (0,245,255)
turquoise2 = (0,229,238)
turquoise3 = (0,197,205)
turquoise4 = (0,134,139)
black = (0,0,0)
white = (255,255,255)

display_width = 800
display_height = 600

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Snakemero')

block_size = 10
FPS = 30

clock = pygame.time.Clock()

font = pygame.font.SysFont(None, 25)

def message_to_screen(msg,color):
	screen_text = font.render(msg, True, color)
	gameDisplay.blit(screen_text,[display_width / 2,display_height / 2])


def gameLoop():

	gameExit = False
	gameOver = False

	lead_x = display_width / 2
	lead_y = display_height / 2

	lead_x_change = 0
	lead_y_change = 0

	randCigX = random.randrange(0, display_width - block_size)
	randCigY = random.randrange(0, display_height - block_size)
	
	while not gameExit:

		while gameOver == True:
			gameDisplay.fill(black)
			message_to_screen('Game Over, press C to play again, and Q to quit..', turquoise1)
			pygame.display.update()

			for event in pygame.event.get():
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_q:
						gameExit = True
						gameOver = False
					if event.key == pygame.K_c:
						gameLoop()

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				gameExit = True

			if event.type == pygame.KEYDOWN:
				# x axis movement
				if event.key == pygame.K_LEFT:
					lead_x_change = -block_size
					lead_y_change = 0
				elif event.key == pygame.K_RIGHT:
					lead_x_change = block_size
					lead_y_change = 0

				# y axis movement
				elif event.key == pygame.K_UP:
					lead_y_change = -block_size
					lead_x_change = 0
				elif event.key == pygame.K_DOWN:
					lead_y_change = block_size
					lead_x_change = 0

		# Stop code for non endless moving mode
		#	if event.type == pygame.KEYUP:
		#		if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
		#			lead_x_change = 0
		#	if event.type == pygame.KEYUP:
		#		if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
		#			lead_y_change = 0

		if lead_x >= display_width or lead_x < 0 or lead_y >= display_height or lead_y <0:
			gameOver = True

		lead_x += lead_x_change
		lead_y += lead_y_change


		gameDisplay.fill(black)
		pygame.draw.rect(gameDisplay,turquoise1,[randCigX,randCigY,block_size,block_size])
		pygame.draw.rect(gameDisplay,turquoise4,[lead_x,lead_y,block_size,block_size])
		pygame.display.update()

		clock.tick(FPS)

	pygame.quit()
	quit()

gameLoop()