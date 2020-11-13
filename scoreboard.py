import pygame.font

class Scoreboard():
	"""A class to report scoring information"""

	def __init__(self, bs_settings, screen):
		"""Initialize scorekeeping attributes"""
		self.screen = screen
		self.screen_rect = screen.get_rect()
		self.bs_settings = bs_settings
		self.status = self.bs_settings.status

		

		#Font settings for scoring information
		self.text_color = (30, 30, 30)
		self.font = pygame.font.SysFont(None, 24)

		# Prepare the initial score image
		self.prep_score(self.phase)

	def prep_score(self, phase):
		"""Turn score into a render image"""
		score_str = str(self.status[self.phase])
		self.score_image = self.font.render(score_str, True, self.text_color,
			self.bs_settings.bg_color)

		#Dispaly the score at the top right of the screen
		self.score_rect = self.score_image.get_rect()
		self.score_rect.centerx = self.screen_rect.centerx
		self.score_rect.y = self.screen_rect.bottom - 48

	def show_status(self):
		"""Draw score to the screen"""
		self.screen.blit(self.score_image, self.score_rect)
