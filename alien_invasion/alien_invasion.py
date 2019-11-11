import sys
import pygame

from settings import Settings
from ship import Ship

class alienInvasion:
	"""Big class to manage game assets and behavior"""
	
	def __init__(self):
		"""Initialize game and create resources"""
		pygame.init
		self.settings = Settings()
		self.screen = pygame.display.set_mode((self.settings.screen_width,self.settings.screen_height))
		pygame.display.set_caption("Alien Wreckfest")

		self.ship = Ship(self)
		
	def run_game(self):
		"""Start main loop"""
		while True:
			self._check_events()
			self.ship.update()
			self._update_screen()

	def _check_events(self):
		"""Respond to keypresses and mouse events."""
		for event in pygame.event.get():
				if event.type == pygame.QUIT:
					sys.exit()
				elif event.type == pygame.KEYDOWN:
					if event.key == pygame.K_RIGHT:
						self.ship.moving_right = True
					elif event.type == pygame.KEYDOWN:
						if event.key == pygame.K_LEFT:
							self.ship.moving_left = True

				elif event.type == pygame.KEYUP:
					if event.key == pygame.K_RIGHT:
						self.ship.moving_right = False	
					elif event.type == pygame.KEYUP:
						if event.key == pygame.K_LEFT:
							self.ship.moving_left = False

	def _update_screen(self):
		"""Update images on the screen and flip to the new screen"""
		self.screen.fill(self.settings.bg_color)
		self.ship.blitme()
			
		#draw new screen
		pygame.display.flip()

if __name__ == '__main__':
	#make instance of game and go
	ai = alienInvasion()
	ai.run_game()
