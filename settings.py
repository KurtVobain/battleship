import pygame
import os

class Settings():
	"""Store all setting for Battleship"""
	def __init__(self):
		#Screen settings
		self.screen_width = 1260
		self.screen_height = 480
		self.bg_color = (0, 255, 255)
		#Allow to complete ship
		self.permission = 0
		#Which way, horizontally(1) or vertically(-1) ship should be drawn
		self.direction_of_ship_drawing = 1
		#Order of a move. 1 - player, -1 - ai
		self.order = 1
		#Draw status of the game
		self.status = ['Place your ships on the right field', 'Make a shoot to the left field', 'Enemy is shooting']

		self.sound_of_miss = pygame.mixer.Sound(os.path.join(os.path.abspath('sound'),'miss1.wav'))
		self.sound_of_hit = pygame.mixer.Sound(os.path.join(os.path.abspath('sound'),'explosion.wav'))


		

