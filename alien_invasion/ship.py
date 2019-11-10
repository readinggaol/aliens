import pygame

class Ship:
	"""class to manage the ship"""
	
	def __init__(self, ai_game):
		"""Initialize ship and starting position"""
		self.screen = ai_game.screen
		self.screen_rect = ai_game.screen.get_rect()
		
	#load image and get rect
	self.image = pygame.image.load(
