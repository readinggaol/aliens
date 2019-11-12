import pygame

class Ship:
	"""class to manage the ship"""
	
	def __init__(self, ai_game):
		"""Initialize ship and starting position"""
		self.screen = ai_game.screen
		self.screen_rect = ai_game.screen.get_rect()
		self.settings = ai_game.settings
		
		#load image and get rect
		self.image = pygame.image.load('images/rocket.bmp')
		self.rect = self.image.get_rect()

		self.rect.midbottom = self.screen_rect.midbottom

		#store decimal value for the ship's horizontal position
		self.x = float(self.rect.x)

		#movement flag
		self.moving_right = False
		self.moving_left = False

	def update(self):
		"""Update the ship's position based on the movement flag."""
		#update ship's x value, not the rext
		if self.moving_right and self.rect.right < self.screen_rect.right:
			self.x += self.settings.ship_speed
		if self.moving_left and self.rect.left > 0:
			self.x -= self.settings.ship_speed



		#update rect object from self.x
		self.rect.x = self.x

	def blitme(self):
		"""Draw the ship at its current location"""
		self.screen.blit(self.image, self.rect)

