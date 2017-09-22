import os
import pygame, sys, random
import random
from pygame.locals import *
from menu import Menu





green    =(  0,204,  0  )
white   = (255, 255,255 )
black   = (  0,   0,  0 )
blue    = (  0,   0, 255)
red     = (255,   0,   0)


bordercolor = green
boxcolor    = white
losecolor = green
groundcolor = black


marioRightUpPosition = [0,0]
marioRightDownPosition  = [0,0]
marioLeftDownPosition = [0,0]
marioDownPosition = [[0,0],[0,0]]
boxLeftPosition = []
boxUpPosition  = []
box = []

drawmushroomtrue = True

boxPosition    = [[800,218]]
marioPosition  = [100,200]
_image_library = {}
addmushroomPosition = 0
def lose ():
	global marioscore
	marioscore = 0
def addmushroom():
	global multiplescore,addmushroomPosition
	if multiplescore >= 500:
		addmushroomPosition = addmushroomPosition +1
		boxPosition.append([800 + addmushroomPosition*50,218])
		multiplescore = 0
def boxmove():
	global marioscore,boxPosition,multiplescore
	length = len(boxPosition)
	for i in range (0, length):
		boxPosition[i][0] = boxPosition[i][0]-20
		if boxPosition[i][0] <= 0:
			boxPosition[i][0] = 800 + i*50

			
def drawbox():
	global box
	length = len(boxPosition)
	for i in range (0,length):
		left , top = boxPosition[i][0],boxPosition[i][1]
		box.insert(i, pygame.draw.rect(DISPLAYSURF, boxcolor, (left , top , 50, 50)))
		pygame.draw.rect(DISPLAYSURF, boxcolor, (left , top , 50, 50))
		
def drawborder():
	pygame.draw.line(DISPLAYSURF, bordercolor, [100,200], [100,267], 5)
	pygame.draw.line(DISPLAYSURF, bordercolor, [154,267], [100,267], 5)
	pygame.draw.line(DISPLAYSURF, bordercolor, [154,267], [154,200], 5)
	pygame.draw.line(DISPLAYSURF, bordercolor, [100,200], [154,200], 5)


def get_image(path):
	global _image_library
	image = _image_library.get(path)
	if image == None:
		canonicalized_path = path.replace('/', os.sep).replace('\\', os.sep)
		image = pygame.image.load(canonicalized_path)
		_image_library[path] = image
	return image
 

def main():
	global changeimage,DISPLAYSURF,notjump,marioPosition,boxPosition,firetrue,marioscore,multiplescore,addmushroomPosition,jump,changeimageloop 
	pygame.init()
	DISPLAYSURF = pygame.display.set_mode((1000, 500))
	jump = None
	clock = pygame.time.Clock()
	changeimageloop = 1
	changeimage = True
	notjump = True
	firetrue = False
	marioscore = 0
	multiplescore = 0
	addmushroomPosition = 0
	while True:
		DISPLAYSURF.fill((255, 255, 255))
		drawborder()
		drawground()
		for event in pygame.event.get(): # event handling loop
			if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
				pygame.quit()
				sys.exit()
			if event.type == KEYDOWN:
				if event.key == K_SPACE:
					firetrue = True
				"""if event.key == K_DOWN:
				
					print marioRightPosition
					print boxLeftPosition"""
			"""if event.type == KEYDOWN:
				if event.key == K_UP:
					marioPosition[1] = marioPosition[1]-20
				if event.key == K_DOWN:	
					marioPosition[1] = marioPosition[1]-20
				if event.key == K_RIGHT:
					marioPosition[0] = marioPosition[0]+10
				if event.key == K_LEF					print marioPosition"""

		keys = pygame.key.get_pressed()  #checking pressed keys

		"""if keys[pygame.K_UP]:
			marioPosition[1] = marioPosition[1]-10
		if keys[pygame.K_DOWN]:
			marioPosition[1] = marioPosition[1]+10"""
		
		if keys[pygame.K_UP]:
			jump = True
			changeimage = False


		if jump :
			if changeimageloop <= 4:
				marioPosition[1] = marioPosition[1]-20
				changeimageloop  = changeimageloop + 1
				notjump = False
			elif changeimageloop > 4 and changeimageloop <= 7:
				marioPosition[1] = marioPosition[1]-10
				changeimageloop  = changeimageloop +1
			elif changeimageloop > 7 and changeimageloop <= 10:
				marioPosition[1] = marioPosition[1]-5
				changeimageloop  = changeimageloop +1
			elif changeimageloop > 10 and changeimageloop <= 13:
				marioPosition[1] = marioPosition[1]+5
				changeimageloop  = changeimageloop +1
			elif changeimageloop > 13 and changeimageloop <= 16:
				marioPosition[1] = marioPosition[1]+10
				changeimageloop  = changeimageloop +1
			elif changeimageloop > 16 and changeimageloop <= 20:
				marioPosition[1] = marioPosition[1]+20
				changeimageloop  = changeimageloop +1
			elif changeimageloop  ==  21:
				changeimageloop = 1 
				jump = False
				notjump = True
				changeimage = True
			

		if notjump :
			if keys[pygame.K_RIGHT]:
				marioPosition[0] = marioPosition[0]+10
				last_move = "right"
				if changeimage:
					changeimage = False
				else:
					changeimage = True
			
			elif keys[pygame.K_LEFT]:
				marioPosition[0] = marioPosition[0]-10
				last_move = "left"
				if changeimage:
					changeimage = False
				else:
					changeimage = True
			else:
				last_move = "stop"
			pygame.time.delay(50)
		else:
			'''if keys[pygame.K_RIGHT]:
				marioPosition[0] = marioPosition[0]+10

			if keys[pygame.K_LEFT]:
				marioPosition[0] = marioPosition[0]-10'''
			if last_move == "right":
				marioPosition[0] = marioPosition[0]+10
			elif last_move == "left":
				marioPosition[0] = marioPosition[0]-10
                
                                
			pygame.time.delay(50)

		wheremario()
		boxmove()

		
		
		runimage()
		drawbox()
		drawmushroom()


		tread()
		
		
		score()
		addmushroom()
		pygame.display.flip()
		clock.tick(60)
def runimage():
	global changeimage,firetrue
	if changeimage == True:
		DISPLAYSURF.blit(get_image('mario.jpg'), marioPosition)
	else:
		DISPLAYSURF.blit(get_image('mario2.jpg'), marioPosition)
def hit():
	global boxPosition
	length = len(boxPosition)
	for i in range (0,length):
		if box[i].collidepoint(marioPosition):
			end()
			lose()
			boxPosition    = [[800,218]]
		if box[i].collidepoint(marioRightDownPosition):
			end()
			lose()
			boxPosition    = [[800,218]]
		if box[i].collidepoint(marioRightUpPosition):
			end()
			lose()
			boxPosition    = [[800,218]]
		if box[i].collidepoint(marioLeftDownPosition):
			end()
			lose()
			boxPosition    = [[800,218]]

def tread():
	global boxPosition,marioscore,multiplescore,jump,changeimage,changeimageloop
	length = len(boxPosition)
	dohit = True
	for i in range (0,length):
		if box[i].collidepoint(marioDownPosition[0]):
			boxPosition[i] = [800,218]
			dohit = False
			marioscore = marioscore +100
			multiplescore   = multiplescore +100
			jump = True
			changeimage = False
			changeimageloop = 3
		if box[i].collidepoint(marioDownPosition[1]):
			boxPosition[i] = [800,218]
			dohit = False
			marioscore = marioscore +100
			multiplescore   = multiplescore +100
			jump = True
			changeimage = False
			changeimageloop = 3
	if dohit:
		hit()

			
"""def wherebox():
	global boxLeftPosition,boxUpPosition
	boxUpPosition =[]
	boxLeftPosition =[]
	for x in range (0,51):
		boxLeftPosition.insert(x, [boxPosition[0],boxPosition[1]+x])
	for y in range (0,51):
		boxUpPosition.insert(y, [boxPosition[0]+y,boxPosition[1]])"""
def wheremario():
	global marioRightUpPosition,marioRightDownPosition,marioLeftDownPosition,marioDownPosition
	
	marioRightUpPosition[0] = marioPosition[0] + 54 
	marioRightUpPosition[1] = marioPosition[1] 

	marioRightDownPosition[0] = marioPosition[0] + 54 
	marioRightDownPosition[1] = marioPosition[1] + 67

	marioLeftDownPosition[0] = marioPosition[0] 
	marioLeftDownPosition[1] = marioPosition[1] +67

	marioDownPosition[0][0] = marioPosition[0] + 1
	marioDownPosition[0][1] = marioPosition[1] +68

	marioDownPosition[1][0] = marioPosition[0] + 53
	marioDownPosition[1][1] = marioPosition[1] +68
	

def end():
	font = pygame.font.Font(None, 100)
	text1 = font.render("You Lose", 1, losecolor)
	text1pos = text1.get_rect()
	text1pos.centerx = DISPLAYSURF.get_rect().centerx
	text1pos.centery = DISPLAYSURF.get_rect().centery
	DISPLAYSURF.blit(text1, [400, 300])
def drawmushroom():
	global drawmushroomtrue
	length = len(boxPosition)
	if drawmushroomtrue == True:
		for i in range(0,length):
			DISPLAYSURF.blit(get_image('badmushroom.jpg'), boxPosition[i])
			drawmushroomtrue = False
	else:
		for i in range(0,length):
			DISPLAYSURF.blit(get_image('badmushroom2.jpg'), boxPosition[i])
			drawmushroomtrue = True
def drawground():
	pygame.draw.line(DISPLAYSURF, groundcolor, [0,272], [1000,272], 5)
def fire():
	DISPLAYSURF.blit(get_image('firemario.jpg'), marioPosition)
def score():
	font = pygame.font.Font(None, 50)
	text1 = font.render("Score:"+str(marioscore), 1, green)
	text1pos = text1.get_rect()
	text1pos.centerx = DISPLAYSURF.get_rect().centerx
	text1pos.centery = DISPLAYSURF.get_rect().centery
	DISPLAYSURF.blit(text1, (0,300))	





if __name__ == '__main__':
	Menu = Menu()
	Menu.startMenu()
	main()
