import pygame
import sys
import os
from time import sleep
from pygame.sprite import Group

import game_functions as gf
import ai_game_functions as ai_gf

from field import Field
from settings import Settings
from layout import Layout

#from play_button import Button

if getattr(sys, 'frozen', False):
    os.chdir(sys._MEIPASS)


def run_game():
    pygame.init()

    FPS = pygame.time.Clock()
    
    bs_settings = Settings()
    screen = pygame.display.set_mode((bs_settings.screen_width, bs_settings.screen_height))
    pygame.display.set_caption('Battleship')
    #Make the Play button
    #play_button = Button(bs_settings, screen, "Play")
    #Initialize player's field list
    fields = []
    gf.create_game_field_1(bs_settings, screen, fields)
    #Initialize ai's field group
    ai_fields = []
    gf.create_game_field_2(bs_settings, screen, ai_fields)

    
    buttons = gf.create_buttons(bs_settings, screen)
    ai_gf.draw_ai_ship(bs_settings, screen, ai_fields, buttons)

    layout = Layout(bs_settings, screen, '') 
    

    

    # Start the main loop for the game
    while True:
        gf.end_game_check(bs_settings, screen, buttons, layout)
        #Player's turn
        if bs_settings.order == 1:
            gf.check_events(bs_settings, screen, fields, ai_fields, buttons)
        #AI's turn
        elif bs_settings.order == -1:
            ai_gf.ai_shoot_action(bs_settings, screen, fields,  ai_fields)
        gf.update_screen(bs_settings, screen, fields, ai_fields, buttons, layout)
        #Make FPS = 15
        FPS.tick(15)
    	

      
        
           
run_game()

input()