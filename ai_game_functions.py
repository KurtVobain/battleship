import random

import pygame

import game_functions as gf


def draw_ai_ship(bs_settings, screen, ai_fields, buttons):

	for i in range(4):
		#Initioalize verification var 'a' to track correct amount of ai's ships
		a = buttons[i].amount_of_ships
		while buttons[i].amount_of_ships != a/2:
			#Random position of ai's "point" and direction of the ship 
			mouse_x, mouse_y = random.randint(1,479), random.randint(1,479)
			bs_settings.direction_of_ship_drawing *= random.randrange(-1, 1, 2)
			#Draw ai's ships 
			gf.draw_ship(bs_settings, screen, ai_fields, buttons, i, mouse_x, mouse_y)
	#Return direction to the stock value
	bs_settings.direction_of_ship_drawing = 1 

def ai_shoot_action(bs_settings, screen, fields, ai_fields):
	mouse_x, mouse_y = random.randint(781,1260), random.randint(1,479)
	gf.shoot_action(bs_settings, screen, fields, mouse_x, mouse_y)
	#bs_settings.order = 1



