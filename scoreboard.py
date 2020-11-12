import pygame.font

class Scoreboard():
	"""A class to report scoring information"""

	def __init__(self, bs_settings, screen, stats):
		"""Initialize scorekeeping attributes"""
		self.screen = screen
		self.screen_rect = screen.get_rect()
		self.bs_settings = bs_settings
		self.stats = 0

		#Font settings for scoring information
		self.text_color = (30, 30, 30)
		self.font = pygame.font.SysFont(None, 48)

		# Prepare the initial score image
		self.prep_score()

	def prep_score(self):
		"""Turn score into a render image"""
		score_str = str(self.stats.score)
		self.score_image = self.font.render(score_str, True, self.text_color,
			self.bs_settings.bg_colour)

		#Dispaly the score at the top right of the screen
		self.score_rect = self.score_image.get_rect()
		self.score_rect.right = self.screen_rect.right - 20
		self.score_rect.top = 20

	def show_score(self):
		"""Draw score to the screen"""
		self.screen.blit(self.score_image, self.score_rect)
