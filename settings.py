import pygame
import os
import sys

class Settings():
	"""Store all setting for Battleship"""
	def __init__(self):

		def resource_path( relative):
			if hasattr(sys, "_MEIPASS"):
				return os.path.join(sys._MEIPASS, relative)
			return os.path.join(relative)

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

		self.sound_of_miss = pygame.mixer.Sound(resource_path(os.path.join('sound', 'miss1.wav')))
		self.sound_of_hit = pygame.mixer.Sound(resource_path(os.path.join('sound', 'explosion.wav')))

		self.four_deck_image = pygame.image.load(resource_path(os.path.join('images', '4deck.bmp')))
		#Make pixels of exact color transparent
		#self.four_deck_image.set_colorkey((255, 255, 255))
		self.three_deck_image = pygame.image.load(resource_path(os.path.join('images', '3deck.bmp')))
		self.two_deck_image = pygame.image.load(resource_path(os.path.join('images', '2deck.bmp')))
		self.one_deck_image = pygame.image.load(resource_path(os.path.join('images', '1deck.bmp')))





		"""Dictionary of button's settings"""
		# Firs  - x position, second - y position, third - button's layout, fourth - size, fifth - amount of ships, sixth - width of button
		self.buttons_settings = {'Four-deck:':[600, 20, self.four_deck_image, 4, 2, 160, 'Battleship'],
								'Three-deck:':[600, 60, self.three_deck_image, 3, 4, 120, 'Cruiser'],
								'Two-deck:':[600, 100, self.two_deck_image, 2, 6, 80, 'Submarine'],
								'One-deck:':[600, 140, self.one_deck_image, 1, 8, 40, 'Destroyer']}

		#First - size of the ship, second - direction of srawing, third and fourth - x and y coordinate, other - fileds of current ship
		self.ships = [[], []] #First list - ai's ships, second - player's


		self.end_game = 0

		self.end_msg = ('You Won!', 'You Lost!')



		


		

