import pygame
import sys
import os
from pygame.sprite import Group

import game_functions as gf
import ai_game_functions as ai_gf

from field import Field
from settings import Settings

if getattr(sys, 'frozen', False):
    os.chdir(sys._MEIPASS)


def run_game():
    pygame.init()
    
    bs_settings = Settings()
    screen = pygame.display.set_mode((bs_settings.screen_width, bs_settings.screen_height))
    pygame.display.set_caption('Battleship')
    #Initialize player's field list
    fields = []
    gf.create_game_field_1(bs_settings, screen, fields)
    #Initialize ai's field group
    ai_fields = []
    gf.create_game_field_2(bs_settings, screen, ai_fields)


    buttons = gf.create_buttons(bs_settings, screen)

    ai_gf.draw_ai_ship(bs_settings, screen, ai_fields, buttons) 
    

    

    # Start the main loop for the game
    while True:
    	if bs_settings.order == 1:
    		gf.check_events(bs_settings, screen, fields, ai_fields, buttons)
    	elif bs_settings.order == 0:
    		ai_gf.ai_shoot_action(bs_settings, screen, fields, ai_fields)
    	gf.update_screen(bs_settings, screen, fields, ai_fields, buttons)

      
        
           
run_game()

input()