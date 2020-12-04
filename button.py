import pygame.font
from pygame.sprite import Sprite

class Button(Sprite):
	def __init__(self, ai_settings, screen, width, height):
		super(Button, self).__init__()
		"""Initialize button attributes."""
		self.screen = screen
		self.screen_rect = screen.get_rect()

		# Set  the dimensions and properties of the button
		#self.width, self.height = 160, 20
		self.width, self.height = width, height
		self.button_color = (0, 255, 0)
		self.text_color = (255, 255, 255)
		self.font = pygame.font.SysFont(None, 25)
		self.activated_flag = -1
		self.msg = ""
		#Define size of ship player can place
		self.ship_size = 0
		#Define amount of ships player can place
		self.amount_of_ships = 0


		# Build the button's rect object and center it
		self.rect = pygame.Rect(0, 0, self.width, self.height)
		

	def prep_msg(self):
		"""Turn msg into a render image and center text on the button"""
		self.msg_image = self.font.render(self.msg, True, self.text_color,
			self.button_color)
		self.msg_image_rect = self.msg_image.get_rect()
		self.msg_image_rect.center = self.rect.center

	def draw_button(self):
		# Draw blank button and then draw message
		#self.prep_msg(self.msg)
		self.msg_image = self.font.render(self.msg, True, self.text_color,
			self.button_color)
		self.msg_image_rect = self.msg_image.get_rect()
		self.msg_image_rect.center = self.rect.center
		self.screen.fill(self.button_color, self.rect)
		self.screen.blit(self.msg_image, self.msg_image_rect)
		

