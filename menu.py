import pygame
import os
import sys
from pygame.locals import *


class Menu:
	def __init__(self):
		self.white  =  (255, 255, 255)
		self.logo_position = [150,0]
		self.black = (  0,   0,  0 )
		self.DISPLAYSURF = pygame.display.set_mode((1000, 500))


	def get_image(self,path):
		_image_library = {}
		image = _image_library.get(path)
		if image == None:
			canonicalized_path = path.replace('/', os.sep).replace('\\', os.sep)
			image = pygame.image.load(canonicalized_path)
			_image_library[path] = image
		return image

	def print_string(self):
		font = pygame.font.Font(None, 50)
		text1 = font.render("Press Space To Start", 1, self.black)
		text1pos = text1.get_rect()
		text1pos.centerx = self.DISPLAYSURF.get_rect().centerx
		text1pos.centery = self.DISPLAYSURF.get_rect().centery
		self.DISPLAYSURF.blit(text1, (0,300))	

	def startMenu(self):
		
		pygame.init()
		#DISPLAYSURF = pygame.display.set_mode((1000, 500))
		self.print_string()
		start = False
		while start == False:


			self.DISPLAYSURF.fill(self.white)
			self.DISPLAYSURF.blit(self.get_image('superMarioPic.jpg'), self.logo_position )
			self.print_string()
			for event in pygame.event.get(): # event handling loop
				if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
					pygame.quit()
					sys.exit()
				if event.type == KEYDOWN:
					if event.key == K_SPACE:
						start =True

						


			pygame.display.flip()