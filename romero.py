import pygame
import time
import random

# boiler plate for all pygame calls
pygame.init()

# pallette for the game 
turquoise1 = (0,245,255)
turquoise2 = (0,229,238)
turquoise3 = (0,197,205)
turquoise4 = (0,134,139)
romeroColor = (189,173,184)
black = (0,0,0)
white = (255,255,255)

 # play area generated or res
display_width = 800
display_height = 600
 
# create the display or "Canvas" and title screen 
gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Snakemero')


icon = pygame.image.load('icon.png')
pygame.display.set_icon(icon)


img = pygame.image.load('head.png')


block_size = 16
FPS = 25

direction = "up"


clock = pygame.time.Clock()

smallFont = pygame.font.SysFont("comicsansms", 25)
medFont = pygame.font.SysFont("comicsansms", 50)
largeFont = pygame.font.SysFont("comicsansms", 80)


def game_intro():

	intro = True

	while intro:


		for event in pygame.event.get():
			# if player closes window it quits
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
			# press c down and end intro..
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_c:
					intro = False
				if event.key == pygame.K_q:
					pygame.quit()
					quit()


		gameDisplay.fill(black)
		message_to_screen("Welcome to Snakemero",
							romeroColor,
							-100,
							"large")

		message_to_screen(".. the more you smoke and collect the longer you get.. ",
							romeroColor,
							-70,)

		message_to_screen(" The objective is to smoke cigarettes and collect Modafinil for later use",
							romeroColor,
							-30)
		pygame.display.update()
		clock.tick(10)





# the snakemero move screen
def snakemero(block_size, snakeList):

	if direction == "right":
		head = pygame.transform.rotate(img,270)

	if direction == "left":
		head = pygame.transform.rotate(img,90)

	if direction == "up":
		head = img

	if direction == "down":
		head = pygame.transform.rotate(img,180)

	gameDisplay.blit(head, (snakeList[-1][0], snakeList[-1][1]))

	for XnY in snakeList[:-1]:
		pygame.draw.rect(gameDisplay,romeroColor,[XnY[0],XnY[1],block_size,block_size])

# redundant text object passthrough
def text_objects(text, color, size):
	if size == "small":
		textSurface = smallFont.render(text,True, color)
	elif size == "medium":
		textSurface = medFont.render(text,True, color)
	elif size == "large":
		textSurface = largeFont.render(text,True, color)
	return textSurface, textSurface.get_rect()


def message_to_screen(msg,color,y_displace = 0, size = "small"):
	textSurf, textRect = text_objects(msg, color, size)
	textRect.center = (display_width / 2), (display_height / 2) + y_displace
	gameDisplay.blit(textSurf,textRect)



# main gameloop
def gameLoop():

	global direction

	gameExit = False
	gameOver = False

	lead_x = display_width / 2
	lead_y = display_height / 2

	lead_x_change = 0
	lead_y_change = 0

	snakeList = []
	snakeLength = 1

	randCigX = round(random.randrange(0, display_width - block_size)) # / 10.0) * 10.0
	randCigY = round(random.randrange(0, display_height - block_size)) # / 10.0) * 10.0

	
	while not gameExit:

		while gameOver == True:
			gameDisplay.fill(black)
			message_to_screen('Game Over', turquoise1, -50, size = "large")
			message_to_screen('Press C to play again or Q to quit.. ', romeroColor, 50, size = "medium")
			pygame.display.update()

			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					gameExit = True
					gameOver = False
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
					direction = "left"
					lead_x_change = -block_size
					lead_y_change = 0
				elif event.key == pygame.K_RIGHT:
					direction = "right"
					lead_x_change = block_size
					lead_y_change = 0

				# y axis movement
				elif event.key == pygame.K_UP:
					direction = "up"
					lead_y_change = -block_size
					lead_x_change = 0
				elif event.key == pygame.K_DOWN:
					direction = "down"
					lead_y_change = block_size
					lead_x_change = 0

		# Stop code for non endless moving mode
		#	if event.type == pygame.KEYUP:
		#		if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
		#			lead_x_change = 0
		#	if event.type == pygame.KEYUP:
		#		if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
		#			lead_y_change = 0


		# Logic for border detection
		if lead_x >= display_width or lead_x < 0 or lead_y >= display_height or lead_y <0:
			gameOver = True



		lead_x += lead_x_change
		lead_y += lead_y_change


		# background is black
		gameDisplay.fill(black)

		#thickness of cigarette power-up
		cigThickness = 24

		pygame.draw.rect(gameDisplay,turquoise1,[randCigX,randCigY,cigThickness,cigThickness])
		
		
		snakeHead = []
		snakeHead.append(lead_x)
		snakeHead.append(lead_y)
		snakeList.append(snakeHead)

		if len(snakeList) > snakeLength:
			del snakeList[0]

		# if we are hitting our own snakemero
		for eachSegment in snakeList[:-1]:
			if eachSegment == snakeHead:
				gameOver = True

		snakemero(block_size, snakeList)
		
		pygame.display.update()


		
##		if lead_x >= randCigX and lead_x <= randCigX + cigThickness:
##			if lead_y >= randCigY and lead_y <= randCigY + cigThickness:
##				print('pufffffff')
##				snakeLength += 1
##				randCigX = round(random.randrange(0, display_width - block_size)) # / 10.0)   * 10.0
##				randCigY = round(random.randrange(0, display_height - block_size)) # / 10.0)  * 10.0
		

		# collision detection
		if lead_x > randCigX and lead_x < randCigX + cigThickness or lead_x + block_size > randCigX and lead_x + block_size < randCigX + cigThickness:
			
			if lead_y > randCigY and lead_y < randCigY + cigThickness:
				snakeLength += 1
				randCigX = round(random.randrange(0, display_width - block_size)) # / 10.0)   * 10.0
				randCigY = round(random.randrange(0, display_height - block_size)) # / 10.0)  * 10.0

			elif lead_y + block_size > randCigY and lead_y + block_size < randCigY + cigThickness:
				snakeLength += 1
				randCigX = round(random.randrange(0, display_width - block_size)) # / 10.0)   * 10.0
				randCigY = round(random.randrange(0, display_height - block_size)) # / 10.0)  * 10.0



		clock.tick(FPS)

	pygame.quit()
	quit()

game_intro()
gameLoop()