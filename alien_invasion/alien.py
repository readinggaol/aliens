import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
	"""Intitialize the alien and set its starting location"""
	def __init__(self, ai_game):
		"""make an alien and set up its position"""
		super().__init__()
		self.screen = ai_game.screen

		#Load the image and set rect
		self.image = pygame.image.load('images/alien.bmp')
		self.rect = self.image.get_rect()

		#Start each alien at the top of the screen
		self.rect.x = self.rect.width
		self.rect.y = self.rect.height

		#Store exact horizontal position
		self.x = float(self.rect.x)