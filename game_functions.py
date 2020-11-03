import pygame
import sys
from time import sleep
from pygame.sprite import Group

from field import Field
from button import Button


def check_events(bs_settings, screen, fields, buttons):
    """Respond to keypresses and mouse ivents"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_mousedown_events(bs_settings, screen, fields, buttons,  mouse_x, mouse_y)
        # elif event.type == pygame.MOUSEMOTION:
        #     x, y = event.pos
        #     if ( x in range(0,48)) and (y in range(0,48)):
        #         print("Hovering over image!")

def check_mousedown_events(bs_settings, screen, fields, buttons, mouse_x, mouse_y):
    """Check collide of point and one of the buttons"""
    for one_button in buttons.sprites():
        if one_button.rect.collidepoint(mouse_x, mouse_y):
            one_button.activated_flag *= -1
            print('activated_flag = ', one_button.activated_flag)

    """Check collide of point and one cage of the field"""
    if bs_settings.fourcages_ship !=0 and bs_settings.threecages_ship !=0 and bs_settings.twocages_ship and bs_settings.twocages_ship !=0 and bs_settings.onecage_ship !=0:
        for one_field in fields.sprites():
            one_field.rect.collidepoint(mouse_x, mouse_y)
            if one_field.rect.collidepoint(mouse_x, mouse_y):
                one_field.field_color = (255, 10, 143)
                one_field.activated_flag = 0
                print('x: ', one_field.rect.x ,'y: ', one_field.rect.y)


def update_screen(bs_settings, screen, fields, ai_fields, buttons):
    #Redraw the screen during each pass thruogh the loop
    screen.fill(bs_settings.bg_color)
    
    #Draw player's field
    for one_field in fields.sprites():
        one_field.draw_field()
    #Draw ai's field
    for one_field in ai_fields.sprites():
        one_field.draw_field()
    #Draw buttons
    for one_button in buttons.sprites():
        one_button.draw_button()
    

    #Make the most recently drawn visible
    pygame.display.flip()


#Make an array of player's field
def create_game_field_1(bs_settings, screen, fields):
    for i in range(10):
        for j in range(10):
            new_field = Field(bs_settings, screen)
            new_field.rect.y += 48 * i
            new_field.rect.x += 48 * j
            fields.add(new_field)


#Make an array of ai's field
def create_game_field_2(bs_settings, screen, ai_fields):
    for i in range(10):
        for j in range(10):
            new_field = Field(bs_settings, screen)
            #Define new coordinates fo ai's field
            new_field.rect.y = 0
            new_field.rect.x = 0
            new_field.rect.y += 48 * i
            new_field.rect.x += 48 * j
            ai_fields.add(new_field)


def create_buttons(bs_settings, screen):
    #Initialize buttons
    buttons = Group()

    four_ship_button = Button(bs_settings, screen)
    four_ship_button.rect.x = 550
    four_ship_button.rect.y = 20
    four_ship_button.msg = "Battleship"
    buttons.add(four_ship_button)

    three_ship_button = Button(bs_settings, screen)
    three_ship_button.rect.x = 550
    three_ship_button.rect.y = 60
    three_ship_button.msg = "Cruiser"
    buttons.add(three_ship_button)


    two_ship_button = Button(bs_settings, screen)
    two_ship_button.rect.x = 550
    two_ship_button.rect.y = 100
    two_ship_button.msg = "Submarine"
    buttons.add(two_ship_button)

    one_ship_button = Button(bs_settings, screen)
    one_ship_button.rect.x = 550
    one_ship_button.rect.y = 140
    one_ship_button.msg = "Destroyer"
    buttons.add(one_ship_button)

    return buttons
            
            
            
            
    