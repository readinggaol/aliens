import pygame

class Ship:
	"""class to manage the ship"""
	
	def __init__(self, ai_game):
		"""Initialize ship and starting position"""
		self.screen = ai_game.screen
		self.screen_rect = ai_game.screen.get_rect()
		
		#load image and get rect
		self.image = pygame.image.load('images/rocket.bmp')
		self.rect = self.image.get_rect()

		self.rect.midbottom = self.screen_rect.midbottom

		#movement flag
		self.moving_right = False
		self.moving_left = False

	def update(self):
		"""Update the ship's position based on the movement flag."""
		if self.moving_right:
			self.rect.x += 1
		if self.moving_left:
			self.rect.x -= 1

	def blitme(self):
		"""Draw the ship at its current location"""
		self.screen.blit(self.image, self.rect)

