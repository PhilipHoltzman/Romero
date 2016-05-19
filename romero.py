import pygame
import time
import random

# boiler plate for all pygame calls
pygame.init()
pygame.mixer.init()

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

# game UI/OS icon
icon = pygame.image.load('icon.png')
pygame.display.set_icon(icon)

#snakehead
rhead = pygame.image.load('head.png')

#cig images
cig1 = pygame.image.load('cig1.png')
cig2 = pygame.image.load('cig2.png')
cig3 = pygame.image.load('cig3.png')
cig4 = pygame.image.load('cig4.png')


# UI images

playButton = pygame.image.load('playB.png')
playButtonMod = pygame.image.load('playBmod.png')
controlButton = pygame.image.load('controlsB.png')
controlButtonMod = pygame.image.load('controlsBmod.png')
quitButton = pygame.image.load('quitB.png')
quitButtonMod = pygame.image.load('quitBmod.png')


# background image for splash
lvlBG = pygame.image.load('lvlBG.png')
splashBG = pygame.image.load('splashBG.png')
gameover = pygame.image.load('gameover.png')
titleScreen = pygame.image.load('title.png')



# loading sounds
slug = pygame.mixer.Sound('slug.ogg')
scream = pygame.mixer.Sound('scream.ogg')



#thickness of cigarette 
cigThickness = 24

#player block size
block_size = 16



FPS = 25

# setting starting player direction
direction = "up"


clock = pygame.time.Clock()


# font variables
smallFont = pygame.font.SysFont("comicsansms", 25)
medFont = pygame.font.SysFont("comicsansms", 50)
largeFont = pygame.font.SysFont("comicsansms", 80)


def splash():

	splash = True

	slug.play()

	while splash:


		for event in pygame.event.get():
			# if player closes window it quits
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
			# press c down and end intro..
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_c:
					splash = False
				if event.key == pygame.K_q:
					pygame.quit()
					quit()

		# display bg image			
		gameDisplay.blit(splashBG, (0,0))
		pygame.display.update()
		clock.tick(10)

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

		cursor = pygame.mouse.get_pos()
		click = pygame.mouse.get_pressed()


		gameDisplay.blit(titleScreen, (0,0))

		# play button display
		
		if 406  < cursor[0] < 598 and 425  < cursor[1] < 469:
			gameDisplay.blit(playButtonMod, (406,425))
			if click[0] == 1:
				print('play')
				intro = False
		else:
			gameDisplay.blit(playButton, (406,425))
			
		# control button display
		if 404  < cursor[0] < 604 and 488  < cursor[1] < 516:
			gameDisplay.blit(controlButtonMod, (404,488))
			if click[0] == 1:
				print('controls')
		else:
			gameDisplay.blit(controlButton, (404,488))

		# quit button
		if 628  < cursor[0] < 752 and 397  < cursor[1] < 524:
			gameDisplay.blit(quitButtonMod, (628,397))
			if click[0] == 1:
				print('quit')
				pygame.quit()
				quit()
		else:
			gameDisplay.blit(quitButton, (628,397))
			
		
		pygame.display.update()
		clock.tick(10)

def score(score):
	text = smallFont.render("Score: " + str(score), True, turquoise1)
	gameDisplay.blit(text, [0,0])



def randItemGen():
	randCigX = round(random.randrange(0, display_width - cigThickness)) # / 10.0)   * 10.0
	randCigY = round(random.randrange(0, display_height - cigThickness)) # / 10.0)  * 10.0
	return randCigX, randCigY



# the snakemero move logic
def snakemero(block_size, snakeList):

	if direction == "right":
		head = pygame.transform.rotate(rhead,270)

	if direction == "left":
		head = pygame.transform.rotate(rhead,90)

	if direction == "up":
		head = rhead

	if direction == "down":
		head = pygame.transform.rotate(rhead,180)

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


	pygame.mixer.music.stop()
	pygame.mixer.music.load("axyPlay.ogg")
	pygame.mixer.music.play(-1,0.0)

	global direction

	gameExit = False
	gameOver = False

	lead_x = display_width / 2
	lead_y = display_height / 2

	lead_x_change = 0
	lead_y_change = 0

	snakeList = []
	snakeLength = 1

	randCigX, randCigY = randItemGen()
	
	while not gameExit:

		while gameOver == True:
			gameDisplay.blit(gameover, (0,0))
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
			pygame.mixer.music.stop()
			scream.play()
			gameOver = True



		lead_x += lead_x_change
		lead_y += lead_y_change


		# background is black
		gameDisplay.blit(lvlBG, (0,0))

		

		#pygame.draw.rect(gameDisplay,turquoise1,[randCigX,randCigY,cigThickness,cigThickness])
		gameDisplay.blit(cig1, (randCigX, randCigY))
		
		snakeHead = []
		snakeHead.append(lead_x)
		snakeHead.append(lead_y)
		snakeList.append(snakeHead)

		if len(snakeList) > snakeLength:
			del snakeList[0]

		# if we are hitting our own snakemero
		for eachSegment in snakeList[:-1]:
			if eachSegment == snakeHead:
				pygame.mixer.music.stop()
				scream.play()
				gameOver = True

		snakemero(block_size, snakeList)

		score(snakeLength-1)
		
		pygame.display.update()


		
##		if lead_x >= randCigX and lead_x <= randCigX + cigThickness:
##			if lead_y >= randCigY and lead_y <= randCigY + cigThickness:
##				print('pufffffff')
##				snakeLength += 1
##				randCigX = round(random.randrange(0, display_width - block_size)) # / 10.0)   * 10.0
##				randCigY = round(random.randrange(0, display_height - block_size)) # / 10.0)  * 10.0
		

		
		if lead_x > randCigX and lead_x < randCigX + cigThickness or lead_x + block_size > randCigX and lead_x + block_size < randCigX + cigThickness:
			
			if lead_y > randCigY and lead_y < randCigY + cigThickness:
				snakeLength += 1
				randCigX, randCigY = randItemGen()

			elif lead_y + block_size > randCigY and lead_y + block_size < randCigY + cigThickness:
				snakeLength += 1
				rrandCigX, randCigY = randItemGen()



		clock.tick(FPS)

	pygame.quit()
	quit()
# function call zone


splash()
pygame.mixer.music.load("axyMenu.ogg")
pygame.mixer.music.play(-1,0.0)
game_intro()
gameLoop()








