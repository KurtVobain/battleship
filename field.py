import pygame
from pygame.sprite import Sprite

class Field(Sprite):
	def __init__(self, bs_settings, screen):
		"""Initialize field attributes."""
		super(Field, self).__init__()
		self.screen = screen
		self.screen_rect = screen.get_rect()

		# Set  the dimensions and properties of the field
		self.width, self.height = 48, 48
		self.field_color = (0, 0, 0)
		self.border_thickness = 1
		#Show current statis of the field. 0 is empty, 1 is can't be drawn, 2 is drawn by a ship. 3 is shooted
		self.status = 0

		# Build the field's rect object and center it
		self.rect = pygame.Rect(0, 0, self.width, self.height)
		self.rect.y = self.screen_rect.top
		self.rect.x = 780
		
		self.surf = pygame.Surface((200, 150))

	def draw_field(self):
		# Draw field
		pygame.draw.rect(self.screen, self.field_color, self.rect, self.border_thickness)
		# self.screen.fill(self.field_color)
		# self.screen.blit(self.rect, (50,25))

	
		







# #Making surface(rect) to be drawn
# surf = pygame.Surface((48, 48))
# #Fill it by current color
# surf.fill((12,166,205))
# #Draw surface
# screen.blit(surf, (100,210))
