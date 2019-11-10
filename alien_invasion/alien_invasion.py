import sys
import pygame

from settings import Settings

class alienInvasion:
	"""Big class to manage game assets and behavior"""
	
	def __init__(self):
		"""Initialize game and create resources"""
		pygame.init
		self.settings = Settings()
		self.screen = pygame.display.set_mode((self.settings.screen_width,self.settings.screen_height))
		pygame.display.set_caption("Alien Wreckfest")
		
	def run_game(self):
		"""Start main loop"""
		while True:
			#watch for events
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					sys.exit()
					
			self.screen.fill(self.settings.bg_color)
			
			#draw new screen
			pygame.display.flip()
			
if __name__ == '__main__':
	#make instance of game and go
	ai = alienInvasion()
	ai.run_game()
