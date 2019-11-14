class Settings():
	"""Class for calibrating settings"""
	
	def __init__(self):
		"""Initialize settings"""
		#Screen settings
		self.screen_width = 900
		self.screen_height = 600
		self.bg_color = (105, 95, 69)

		#ship speed
		self.ship_speed = 1.5

		#bullet settings
		self.bullet_speed = 1.0
		self.bullet_width = 3
		self.bullet_height = 15
		self.bullet_color = (60, 60, 60)
		self.bullets_allowed = 3

		#alien settings
		self.alien_speed = 1.0
		self.fleet_drop_speed = 10
		#fleet_direction of 1 represents right; -1 represents left
		self.fleet_direction = 1
