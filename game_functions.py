import pygame
import sys
from time import sleep
from pygame.sprite import Group

from field import Field
from button import Button

def check_events(bs_settings, screen, fields, ai_fields, buttons):
    """Respond to keypresses and mouse ivents"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_mousedown_events(bs_settings, screen, fields, ai_fields, buttons,  mouse_x, mouse_y)
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


def check_mousedown_events(bs_settings, screen, fields, ai_fields, buttons, mouse_x, mouse_y):
    """Check collide of point and one of the buttons. Work only if player's ships can be placed"""
    if buttons[0].amount_of_ships+buttons[1].amount_of_ships+buttons[2].amount_of_ships+buttons[3].amount_of_ships > 0:
        point_and_button_collision(bs_settings, screen, fields, buttons, mouse_x, mouse_y)
    #Make shoot action if all player's ans ai's ships are on the field
    elif buttons[0].amount_of_ships+buttons[1].amount_of_ships+buttons[2].amount_of_ships+buttons[3].amount_of_ships == 0:
        shoot_action(bs_settings, screen, ai_fields, mouse_x, mouse_y)
        bs_settings.phase = 1


        
    
        


def shoot_action(bs_settings, screen, ai_fields, mouse_x, mouse_y):
    for m in range(10):
        for j in range(10):
            for one_ship in bs_settings.ships:
                """Delete empty lists from ships' list"""
                if not one_ship:
                    bs_settings.ships.remove(one_ship)

                """Check if point collide with field and the field is in ships list"""
                if ai_fields[m][j].rect.collidepoint(mouse_x, mouse_y) and ai_fields[m][j] in one_ship and ai_fields[m][j].status == 2: 
                    #Play hit sound
                    bs_settings.sound_of_hit.play()
                    ai_fields[m][j].status = 3
                    ai_fields[m][j].field_color = (0, 0, 0)
                    ai_fields[m][j].border_thickness = 0

                    #Remove filed from ship
                    one_ship.remove(ai_fields[m][j])
                    #If ship has no fileds execute surround_ship function
                    if len(one_ship) == 4:
                        surround_ship(bs_settings, screen, ai_fields, one_ship[0], one_ship[1], one_ship[3], one_ship[2], 5, (252,0,13))

                #If field is not in ships list activate 'miss' actions
                elif ai_fields[m][j].rect.collidepoint(mouse_x, mouse_y) and (ai_fields[m][j].status == 0 or ai_fields[m][j].status == 1 ):
                    #Play miss sound
                    bs_settings.sound_of_miss.play()

                    ai_fields[m][j].status = 3
                    ai_fields[m][j].field_color = (252, 0, 13)
                    ai_fields[m][j].border_thickness = 5
                    #Order changes
                    bs_settings.order *= -1


def point_and_button_collision(bs_settings, screen, fields, buttons, mouse_x, mouse_y):
    for i in range(4):
        if buttons[i].rect.collidepoint(mouse_x, mouse_y):
            #Change flag to track it's condition
            buttons[i].activated_flag *= -1
            buttons[i].button_color = (255, 0, 0)
            #Set other buttons flags to -1, cause only one button per time can be active
            for j in range(1, 4):
                buttons[i-j].activated_flag = -1
                buttons[i-j].button_color = (0, 255, 0)
            print('activated_flag = ', buttons[i].activated_flag)
        #Check and call function to draw ship 
        if buttons[i].activated_flag == 1 and buttons[i].amount_of_ships > 0:
            border_thickness = 0
            color = (255, 239, 0)
            draw_ship(bs_settings, screen, fields, buttons, i, mouse_x, mouse_y, color, border_thickness)



def draw_ship(bs_settings, screen, fields, buttons, i, mouse_x, mouse_y, color=(0,0,0), border_thickness=1):
    #The list store fields of one ship and list itself store in ships from settings.py
    new_ship = []

    for m in range(10):
        for j in range(10):    
            """Check collide of point and one cage of the field and check if cage is already used"""
            if fields[m][j].rect.collidepoint(mouse_x, mouse_y) and fields[m][j].status == 0:
                fields[m][j].field_color = color #(154, 152, 152)
                fields[m][j].border_thickness = border_thickness 
                # Status = 2 means the field is drawn by ship
                fields[m][j].status = 2
               

                check_of_the_free_space(bs_settings, screen, fields, buttons, i, j, m)

                """Add necessary cages for the first cliccked cage to complete ship"""
                if bs_settings.permission == 1 and bs_settings.direction_of_ship_drawing == 1:
                    #Append to the list ship's size
                    new_ship.append(buttons[i].ship_size)
                    #Append to the list direction of the drawling of the ship
                    new_ship.append(bs_settings.direction_of_ship_drawing)
                    #Append to the list coordinates of the firs ship's field
                    new_ship.append(m)
                    new_ship.append(j)
                    #Append to the list field of the ship
                    new_ship.append(fields[m][j])

                    for k in range(1, buttons[i].ship_size):
                        fields[m][j+k].field_color = color 
                        fields[m][j+k].border_thickness = border_thickness 
                        fields[m][j+k].status = 2
                        #Append to the list field of the ship
                        new_ship.append(fields[m][j+k])

                     
                elif bs_settings.permission == 1 and bs_settings.direction_of_ship_drawing == -1:
                    #Append to the list ship's size
                    new_ship.append(buttons[i].ship_size)
                    #Append to the list direction of the drawling of the ship
                    new_ship.append(bs_settings.direction_of_ship_drawing)
                    #Append to the ships list coordinates of the firs ship's field
                    new_ship.append(m)
                    new_ship.append(j)
                    #Append to the list field of the ship
                    new_ship.append(fields[m][j])
                    
                    for k in range(1, buttons[i].ship_size):
                        fields[m+k][j].field_color = color 
                        fields[m+k][j].border_thickness = border_thickness
                        fields[m+k][j].status = 2
                        #Append to the list field of the ship
                        new_ship.append(fields[m+k][j])

                    
                

                """Surround ship for escaping collisions"""
                if bs_settings.permission == 1:
                    surround_ship(bs_settings, screen, fields, buttons[i].ship_size, bs_settings.direction_of_ship_drawing, j, m)

                
                buttons[i].amount_of_ships -= 1
                bs_settings.permission = 0
    #Append to the ships list size and fields of new ship 
    bs_settings.ships.append(new_ship)

def surround_ship(bs_settings, screen, fields, ship_size, direction_of_ship_drawing, j, m, border_thickness = 1, field_color = (0,0,0)):
    """Surround ship by non-active fileds for ships cant be placed close to each other.
        Function get postion of the first field of the ship, size and direction and surround ship according to them 
    """
    if direction_of_ship_drawing == 1:
        #Surround by x coordinate
        for jteration in range(-1, 2, 2):
            for iteration in range(-1, ship_size+1):
                #try if ship's surronding out of game field
                try:
                    if j+iteration>= 0 and m+jteration >= 0:
                        fields[m+jteration][j+iteration].border_thickness = border_thickness
                        fields[m+jteration][j+iteration].field_color = field_color
                        fields[m+jteration][j+iteration].status = 1
                except IndexError:
                    break
        #Surround by y coordinate
        for iteration in range(-1, ship_size+1, ship_size+1):
            #try if ship's surronding out of game field
            try: 
                if j+iteration>= 0:
                    fields[m][j+iteration].border_thickness = border_thickness
                    fields[m][j+iteration].field_color = field_color
                    fields[m][j+iteration].status = 1
            except IndexError:
                    break

    elif direction_of_ship_drawing == -1:
        #Surround by y coordinate
        for jteration in range(-1, 2, 2):
            for iteration in range(-1, ship_size+1):
                #try if ship's surronding out of game field
                try:
                    if m+iteration >= 0 and j+jteration >= 0:
                        fields[m+iteration][j+jteration].border_thickness = border_thickness
                        fields[m+iteration][j+jteration].field_color = field_color
                        fields[m+iteration][j+jteration].status = 1
                except IndexError:
                    break
        #Surround by x coordinate
        for iteration in range(-1, ship_size+1, ship_size+1):
            #try if ship's surronding out of game field
            try:
                if m+iteration >= 0:
                    fields[m+iteration][j].border_thickness = border_thickness
                    fields[m+iteration][j].field_color = field_color
                    fields[m+iteration][j].status = 1
            except IndexError:
                    break



    
            
def check_of_the_free_space(bs_settings, screen, fields, buttons, i, j, m):
    """Check if cages have alredy occupied. If it so cancel previous 'If' action"""
    if buttons[i].ship_size == 1:
        bs_settings.permission = 1
    #try if ship out of game field
    try:
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
    except IndexError:
        bs_settings.permission = 0
        fields[m][j].field_color = (0, 0, 0)
        fields[m][j].border_thickness = 1
        fields[m][j].status = 0
        buttons[i].amount_of_ships += 1
        bs_settings.permission = 0





def update_screen(bs_settings, screen, fields, ai_fields, buttons):
    #Redraw the screen during each pass thruogh the loop
    screen.fill(bs_settings.bg_color)
    
    #Draw player's field
    for i in fields:
        for one_field in i:
            one_field.draw_field()
    #Draw ai's field
    for j in ai_fields:
        for one_ai_field in j:
            one_ai_field.draw_field()
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
        ai_fields.append([])
        for j in range(10):
            #Define new coordinates for ai's field
            new_field = Field(bs_settings, screen)
            new_field.rect.y = 0
            new_field.rect.x = 0
            new_field.rect.y += 48 * i
            new_field.rect.x += 48 * j
            ai_fields[i].append(new_field)


def create_buttons(bs_settings, screen):
    #Initialize buttons
    buttons = []

    for new_button in bs_settings.buttons_settings.keys():
        value = bs_settings.buttons_settings.get(new_button)\
        #Initialize new Button object
        new_button = Button(bs_settings, screen, value[5],  18)
        """Define unique values of the new button"""
        new_button.rect.centerx = value[0]
        new_button.rect.y = value[1]
        new_button.msg = value[2]
        new_button.ship_size = value[3]
        new_button.amount_of_ships = value[4]
        #Add the new button to buttons list
        buttons.append(new_button)

    return buttons
            
            
            
            
    