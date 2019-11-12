class Settings():
	"""Class for calibrating settings"""
	
	def __init__(self):
		"""Initialize settings"""
		#Screen settings
		self.screen_width = 800
		self.screen_height = 600
		self.bg_color = (105, 95, 69)

		#ship speed
		self.ship_speed = 1.5

		#bullet settings
		self.bullet_speed = 1.0
		self.bullet_width = 3
		self.bullet_height = 15
		self.bullet_color = (60, 60, 60)
