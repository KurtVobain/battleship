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
		#Order of a move. 1 - player, 0 - ai
		self.order = 1

		

