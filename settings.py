import pygame
import os

class Settings():
	"""Store all setting for Battleship"""
	def __init__(self):
		#Screen settings
		self.screen_width = 1260
		self.screen_height = 480
		self.bg_color = (0, 255, 255)

		self.fourcages_ship = 1
		self.threecages_ship = 2
		self.twocages_ship = 3
		self.onecage_ship = 4

		

