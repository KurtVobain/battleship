import pygame.font
from pygame.sprite import Sprite
import os
import sys

class Button(Sprite):
	def __init__(self, bs_settings, screen):
		super(Button, self).__init__()
		"""Initialize button attributes."""
		self.screen = screen
		self.screen_rect = screen.get_rect()

		self.activated_flag = -1
		#Define size of ship player can place
		self.ship_size = 0
		#Define amount of ships player can place
		self.amount_of_ships = 0


	def get_image(self, deck_image):
		self.image = deck_image
		self.scale_button(2)

		self.rect = self.image.get_rect()

		#Rotate image in horizontal way
		self.rotated_image = pygame.transform.rotate(self.image, 90)
		#Redefine a new rect through the old one
		self.rect = self.rotated_image.get_rect(center=self.rect.center)


	def scale_button(self, argument):
		"""Change size of the button"""
		self.image = pygame.transform.scale(self.image, (self.image.get_width()//argument , self.image.get_height()//argument))
		

	def blitme(self):
		"""Draw the button at its current location"""
		self.screen.blit(self.rotated_image, self.rect)
		self.screen.blit(self.textimage, self.text_rect)



	def prep_text(self, msg):
		def resource_path( relative):
			if hasattr(sys, "_MEIPASS"):
				return os.path.join(sys._MEIPASS, relative)
			return os.path.join(relative)

		self.font = pygame.font.Font(resource_path(os.path.join('images', 'freesansbold.ttf')), 15)
		self.textimage = self.font.render(str(msg), True,
							(30, 30, 30))

		self.text_rect = self.textimage.get_rect()
		self.text_rect.centery = self.rect.centery 
		self.text_rect.left = self.rect.left - 100



