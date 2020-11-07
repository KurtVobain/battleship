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
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, bs_settings)
        # elif event.type == pygame.MOUSEMOTION:
        #     check_mousemotion_events(event, bs_settings, screen, fields, buttons)
            

def check_mousemotion_events(event, bs_settings, screen, fields, buttons):
    x, y = event.pos
    for i in range(10):
        for j in range(10):
            for k in range(4):
                if (( x in range(fields[i][j].rect.x, fields[i][j].rect.x+48)) and (y in range(fields[i][j].rect.y, fields[i][j].rect.y+48))
                 and buttons[k].activated_flag == 1 and buttons[k].amount_of_ships > 0 and fields[i][j].status == 0):
                    fields[i][j].field_color = (128, 100, 71)
                    fields[i][j].border_thickness = 0
            # if fields[i][j].status == 0:
            #     fields[i][j].field_color = (0, 0, 0)
            #     fields[i][j].border_thickness = 1
                



def check_keydown_events(event, bs_settings):
    """Change direction_of_ship_drawing if 'Q' has been pressed"""
    if event.key == pygame.K_q:
        bs_settings.direction_of_ship_drawing *= -1


def check_mousedown_events(bs_settings, screen, fields, buttons, mouse_x, mouse_y):
    """Check collide of point and one of the buttons"""
    for i in range(4):
        if buttons[i].rect.collidepoint(mouse_x, mouse_y):
            #Change flag to track it's condition
            buttons[i].activated_flag *= -1
            #Set other buttons flags to -1, cause only one button per time can be active
            buttons[i-1].activated_flag = -1
            buttons[i-2].activated_flag = -1
            buttons[i-3].activated_flag = -1
            print('activated_flag = ', buttons[i].activated_flag)
        #Check and call function to draw ship 
        if buttons[i].activated_flag == 1 and buttons[i].amount_of_ships > 0:
            draw_ship(bs_settings, screen, fields, buttons, i, mouse_x, mouse_y)
            


def draw_ship(bs_settings, screen, fields, buttons, i, mouse_x, mouse_y):
    #bs_settings.permission = 0
    for m in range(10):
        for j in range(10):    
            fields[m][j].rect.collidepoint(mouse_x, mouse_y)
            """Check collide of point and one cage of the field and check if cage is already used"""
            if fields[m][j].rect.collidepoint(mouse_x, mouse_y) and fields[m][j].status == 0:
                fields[m][j].field_color = (255, 10, 143)
                fields[m][j].border_thickness = 0
                # Status = 2 means the field is drawn
                fields[m][j].status = 2

                check_of_the_free_space(bs_settings, screen, fields, buttons, i, j, m)

                """Add necessary cages for the first cliccked cage to complete ship"""
                if bs_settings.permission == 1 and bs_settings.direction_of_ship_drawing == 1:
                    for k in range(1, buttons[i].ship_size):
                        fields[m][j+k].field_color = (255, 10, 143)
                        fields[m][j+k].border_thickness = 0
                        fields[m][j+k].status = 2
                elif bs_settings.permission == 1 and bs_settings.direction_of_ship_drawing == -1:
                    for k in range(1, buttons[i].ship_size):
                        fields[m+k][j].field_color = (255, 10, 143)
                        fields[m+k][j].border_thickness = 0
                        fields[m+k][j].status = 2

                buttons[i].amount_of_ships -= 1
                bs_settings.permission = 0
                
def check_of_the_free_space(bs_settings, screen, fields, buttons, i, j, m):
    """Check if cages have alredy occupied. If it so cancel previous 'If' action"""
    if bs_settings.direction_of_ship_drawing == 1:
        for k in range(1, buttons[i].ship_size):
            if fields[m][j+k].status != 0:
                fields[m][j].field_color = (0, 0, 0)
                fields[m][j].border_thickness = 1
                fields[m][j].status = 0
                buttons[i].amount_of_ships += 1
                bs_settings.permission = 0
                break  
            else:
                bs_settings.permission = 1

    elif bs_settings.direction_of_ship_drawing == -1:
        for k in range(1, buttons[i].ship_size):
            if fields[m+k][j].status != 0:
                fields[m][j].field_color = (0, 0, 0)
                fields[m][j].border_thickness = 1
                fields[m][j].status = 0
                buttons[i].amount_of_ships += 1
                bs_settings.permission = 0
                break  
            else:
                bs_settings.permission = 1





def update_screen(bs_settings, screen, fields, ai_fields, buttons):
    #Redraw the screen during each pass thruogh the loop
    screen.fill(bs_settings.bg_color)
    
    #Draw player's field
    for i in fields:
        for one_field in i:
            one_field.draw_field()
    #Draw ai's field
    for one_field in ai_fields.sprites():
        one_field.draw_field()
    #Draw buttons
    for one_button in buttons:
        one_button.draw_button()
    

    #Make the most recently drawn visible
    pygame.display.flip()


#Make an list of player's field
def create_game_field_1(bs_settings, screen, fields):
    for i in range(10):
        fields.append([])
        for j in range(10):
            new_field = Field(bs_settings, screen)
            new_field.rect.y += 48 * i
            new_field.rect.x += 48 * j
            fields[i].append(new_field)


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
    buttons = []

    four_ship_button = Button(bs_settings, screen)
    four_ship_button.rect.x = 550
    four_ship_button.rect.y = 20
    four_ship_button.msg = "Battleship"
    four_ship_button.ship_size = 4
    four_ship_button.amount_of_ships = 1
    buttons.append(four_ship_button)

    three_ship_button = Button(bs_settings, screen)
    three_ship_button.rect.x = 550
    three_ship_button.rect.y = 60
    three_ship_button.msg = "Cruiser"
    three_ship_button.ship_size = 3
    three_ship_button.amount_of_ships = 2
    buttons.append(three_ship_button)


    two_ship_button = Button(bs_settings, screen)
    two_ship_button.rect.x = 550
    two_ship_button.rect.y = 100
    two_ship_button.msg = "Submarine"
    two_ship_button.ship_size = 2
    two_ship_button.amount_of_ships = 3
    buttons.append(two_ship_button)

    one_ship_button = Button(bs_settings, screen)
    one_ship_button.rect.x = 550
    one_ship_button.rect.y = 140
    one_ship_button.msg = "Destroyer"
    one_ship_button.ship_size = 1
    one_ship_button.amount_of_ships = 4
    buttons.append(one_ship_button)

    return buttons
            
            
            
            
    