class Settings:
	'''A class to store all the settings for the game alien invasion.'''

	def __init__(self):
		"""initialize the game's settings."""

		#screen settings
		self.screen_width = 1200
		self.screen_height = 600 #800
		self.bg_color = (230,230,230)

		#ship settings
		self.ship_speed = 1.5