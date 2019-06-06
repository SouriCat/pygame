import pygame, sys
from pygame.locals import *
pygame.init()


win_width = 1000
win_height = 700
win_width_boundary = win_width
win_height_boundary = win_height - 100

win = pygame.display.set_mode((win_width, win_height))
pygame.display.set_caption("Mon premier jeu")
#########   Keys bind   ###########


#########   Images load   ###########
width_tile = 100
height_tile = 100

tile_hud1 = (pygame.image.load('tiles_HUD1.png'), False)
tile_hud2 = (pygame.image.load('tiles_HUD2.png'), False)
tile_hud3 = (pygame.image.load('tiles_HUD3.png'), False)
tile_hud4 = (pygame.image.load('tiles_HUD4.png'), False)
             
tile_grass = (pygame.image.load('tiles-grass.png'), True)
tile_wood = (pygame.image.load('tiles_woods1.png'), True)
tile_wall = (pygame.image.load('tiles-wall.jpg'), False)
tile_tree1 = (pygame.image.load('tiles-grass_tree1.png'), False)
tile_tree2 = (pygame.image.load('tiles_tree2.png'), False)

tile_door1close = (pygame.image.load('tiles_door1_1.png'), False)
tile_door1open = (pygame.image.load('tiles_door1_2.png'), True)

character = pygame.image.load('standing.png')
arrow_right = pygame.image.load('arrow_right.png')
hole_ladder = pygame.image.load('hole_with_ladder.png')


golden_key = pygame.image.load('item_golden_key.png')
blue_bomb = pygame.image.load('item_bomb_blue.png')
orange_bomb = pygame.image.load('item_bomb_orange.png')
green_bomb = pygame.image.load('item_bomb_green.png')

#RECT_character = character.get_rect()
#print ( "voici le rectangle du personnage" ,RECT_character)


def get_rect(x, y, width, height):
#    print ("i made a pygame rect with :", x, y, width, height)
    return pygame.Rect(x, y, width, height)
#############################################
#########    Données du joueur     ##########
#############################################
class player(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 12
        self.hitbox = self.x + 16, self.y + 15, 32, 48
    def draw (self, win):
#        self.hitbox = character.get_rect()
        self.hitbox = self.x + 16, self.y + 15, 32, 48
#        pygame.draw.rect(win, (255,255,0), self.hitbox,2)
        win.blit(character, (self.x, self.y))
#        print ("j'ai afficher le personnage")
    def draw_in_hud(self):
        win.blit(character, (15, 610))
#        print ("j'ai afficher le personnage dans l'HUD")
#############################################
######       Données du terrain       #######
#############################################
# 0 = grass // 11 = wall // 12 tree1 // 96 HUD1carré // 97 HUD2 //98 HUD3 //99 HUD4 //
tiles_1 = [[12,12, 0,12,12, 0, 0, 0, 0, 0],
           [ 0, 0, 0, 0,12, 0, 0, 0,12, 0],
           [ 0, 0, 0, 0, 0,12, 0, 0,12,12],
           [ 0,12,11,70,11,11,11, 0,12,12],
           [ 0, 0,11, 1, 1, 1,11, 0, 0, 0],
           [ 0, 0,11, 1, 1, 1, 1, 0, 0, 0],
           [96,97,98,98,98,98,98,98,99,96]]

tiles_2 = [[12,12,12,12,12,12,12, 0, 0, 0],
           [ 0, 0, 0, 0, 0,12, 0, 0,12, 0],
           [ 0, 0,13,13,12,12, 0, 0,12, 0],
           [ 0,12,11,11,11,11,11,12,12, 0],
           [ 0, 0,11, 1, 1, 1,11,12, 0, 0],
           [ 0, 0, 1, 1, 1, 1, 1, 0, 0, 0],
           [96,97,98,98,98,98,98,98,99,96]]

tiles_3 = [[ 1, 1, 1,11,11, 1, 1, 1, 1, 1],
           [ 1, 1, 1,11, 1, 1, 1, 1,11, 1],
           [ 1, 1, 1, 1,11,11,11,11, 1, 1],
           [11,11, 1,11, 1,11, 1, 1, 1, 1],
           [11, 1, 1, 1, 1,11, 1, 1,11, 1],
           [11, 1, 1, 1, 1, 1, 1, 1, 1, 1],
           [96,97,98,98,98,98,98,98,99,96]]


class field(object):
    def create_matrice(tiles):
        line_increment = 0
        for line in tiles:        
            tile_increment = 0
            for tile in line:
    ##           tiles[line_increment][tile_increment] = tile_increment*100 , line_increment*100  
                x_tile = tile_increment*100
                y_tile = line_increment*100
                
                win.blit(tile_grass[0], (x_tile,y_tile))
                
                tile_increment += 1
            tile_increment = 0       
            line_increment += 1
        pygame.display.update()

    def change_tile(matrice, new_tile, id_tile):
        line_increment = 0
        for line in matrice:        
            tile_increment = 0
            for tile in line:
    ##           tiles[line_increment][tile_increment] = tile_increment*100 , line_increment*100  
                x_tile = tile_increment*100
                y_tile = line_increment*100            
                if tile == id_tile:
                    win.blit(new_tile[0], (x_tile, y_tile))

                tile_increment += 1
            tile_increment = 0       
            line_increment += 1
        pygame.display.update()
             
    def draw_tiles_of_field (tiles_nb):
        # 0 = grass // 11 = wall // 12 = tree1
        field.change_tile(tiles_nb, tile_grass, 0)
        field.change_tile(tiles_nb, tile_wood, 1)
        field.change_tile(tiles_nb, tile_wall, 11)
        field.change_tile(tiles_nb, tile_tree1, 12)
        field.change_tile(tiles_nb, tile_tree2, 13)
        
        # 70 = door1Close // 71 = door1Open 
        field.change_tile(tiles_nb, tile_door1close, 70)
        field.change_tile(tiles_nb, tile_door1open, 71)
        # 96 = HUD square // 97 = HUD left // 98 = HUD mid // 99 = HUD right
        field.change_tile(tiles_nb, tile_hud1, 96)
        field.change_tile(tiles_nb, tile_hud2, 97)
        field.change_tile(tiles_nb, tile_hud3, 98)
        field.change_tile(tiles_nb, tile_hud4, 99)
        

    def get_picture_background():
        
#        rect_for_game_display_update = get_rect( 0, 0, 1000, 600)
        pict_background_saved = pygame.display.get_surface()
        pict_background_saved = pict_background_saved.copy()
#        win.blit(pict_background_saved, (10, 10))
#        pygame.display.update()
        
        return pict_background_saved

    def get_close_picture_background(pict_background, rect_player_large):
        
        close_picture_background = pict_background.subsurface(rect_player_large)
        free_close_picture_background = close_picture_background.copy()
        
#        win.blit(free_close_picture_background, (100, 100))
#        pygame.display.update()
        
        return free_close_picture_background
    

    def get_close_player_rect(man):
        large_background_player = get_rect(man.hitbox[0] - man.vel, man.hitbox[1] - man.vel, man.hitbox[2] + man.vel*2, man.hitbox[3] + man.vel*2)

#        pygame.draw.rect(win, (255,255,0), large_background_player,2)
#        pygame.display.update()
        
        return large_background_player       
    
##        print("Ligne",line_increment, line)
    

        

    
#############################################
##########     Gestion des murs   ###########
#############################################
    
class wall(object):
    def __init__(self, pos_x_tile, pos_y_tile):
        walls.append((pos_x_tile, pos_y_tile, 100, 100))

    def add_to_a_wall_list(matrice):
        walls = []
        line_increment = 0
        for line in matrice:
            tile_increment = 0
            for tile in line:
                if tile >= 10 or tile == 71:
                    x_tile = tile_increment*100
                    y_tile = line_increment*100
                    wall(x_tile, y_tile)
                    
                tile_increment += 1
            tile_increment = 0
            line_increment += 1
      
    def test_collide_wall():
        to_return = 0
        Rect_player = get_rect(man.hitbox[0], man.hitbox[1], man.hitbox[2], man.hitbox[3])
        for element in walls:
            Rect_Tile =get_rect(element[0], element[1], element[2], element[3])  
            if Rect_Tile.colliderect(Rect_player):
                to_return = 1
                print ("vous touchez un mur !", element[0], element[1])
                break
            else:
                to_return = 0
#        print ("Dans fonction collide_wall", to_return)
        return to_return

    def delete_wall(pos_x_wall, pos_y_wall):
        index_wall2 = 0
        found = False
        while index_wall2 < len(walls) and found == False :
            if walls[index_wall2][0] == pos_x_wall and walls[index_wall2][0] == pos_y_wall:
                walls.remove(walls[index_wall2])               
                found = True
                index_wall2 -= 1 
            index_wall2 += 1
            
## Plus de tiles ici : https://www.deviantart.com/phyromatical/art/Tons-of-Tileset-3-10-Gaia-Trees-486095492 


#############################################
######       Gestion des items        #######
#############################################

class Item(pygame.sprite.Sprite):
    def __init__(self,item_name, item_picture, item_x, item_y, item_width, item_height):
        pygame.sprite.Sprite.__init__(self)
        self.name = item_name
        self.image = item_picture
        self.rect = self.image.get_rect()
        self.rect.x = item_x
        self.rect.y = item_y
        self.rect.width = item_width
        self.rect.height = item_height
        self.never_touched = True

    # Item.player_touch_item(item)
    def player_touch_item (self):
        player_touching_item = False
        Rect_player = get_rect(man.hitbox[0], man.hitbox[1], man.hitbox[2], man.hitbox[3])
        Rect_item = get_rect(self.rect.x, self.rect.y, self.rect.width, self.rect.height)
        if self.never_touched == True:
            if Rect_item.colliderect(Rect_player):
                self.never_touched = False
                player_touching_item = True
        return player_touching_item
          
    def delete_item_from_map(self, items_map):
        items_map.remove(self)
        sprite_list = items_map.sprites()

        # Effacement de la clef sur l'ecran (a exporter dans la class "Item")
        rect_item =get_rect(self.rect.x, self.rect.y, self.rect.width, self.rect.height)
        freed_close_picture_background = field.get_close_picture_background(pict_background, rect_item)
        win.blit(freed_close_picture_background, (self.rect.x, self.rect.y))

############### Gestion de l'inventaire           
    def add_item_in_inventory(self):
        features = [self.name, self.image, self.rect.x, self.rect.y, self.rect.width, self.rect.height, self.never_touched]
        Inventory.append(features)

#        
    def change_item_in_inventory(current_index_inventory):
        inventory_lenght = len(Inventory)
        if inventory_lenght <= 0 :
            current_index_inventory[0] = -1
            win.blit(tile_hud1[0], (900, 600))
            pygame.display.update()
            print ("Votre inventaire est vide")
            
        elif inventory_lenght == 1:
            current_index_inventory[0] = 0
            win.blit(tile_hud1[0], (900, 600))
            win.blit(Inventory[0][1], (920, 620))
            pygame.display.update()        
            print ("Vous n'avez qu'un item dans la liste, vous ne pouvez pas passer au suivant.")                
        else:
            index_to_display = current_index_inventory[0] + 1
            item_index_max = inventory_lenght - 1
 
            if current_index_inventory[0] < item_index_max:
                current_index_inventory[0] += 1
                win.blit(tile_hud1[0], (900, 600))
                win.blit(Inventory[index_to_display][1], (920, 620))
                pygame.display.update()
                print ("Voici l'index de l'item affiché", index_to_display)
                
            else:
                current_index_inventory[0] = 0
                win.blit(tile_hud1[0], (900, 600))
                win.blit(Inventory[0][1], (920, 620))
                pygame.display.update()
                print ("L'inventaire à été remis a zero")

#                
    def get_name_of_an_index_in_inventory(index):
        name_of_index = "L'inventaire est vide"
        if len(Inventory) >= 1:
            incremental = 0
            for item in Inventory :
                if incremental == index :
                    name_of_index = item[0]
                incremental += 1
        return name_of_index

#
    def search_item_in_inventory(item_name):
        result = "not_found" ## Means that the item is not in the inventory
        incremental = 0
        for item in Inventory :
            if item[0] == item_name:
                result = Item.get_name_of_an_index_in_inventory(index_of_inventory[0])
            incremental += 1
        return result
    
    def is_item_selected(item_name):
        item_selected = False
        result = Item.search_item_in_inventory(item_name)
        if result == item_name:
#            print ("Je vois ", item_name, " dans l'inventaire")
            item_selected = True
        return item_selected
    
############### Gestion de l'utilisation des bombes
    
    def display_a_bomb(bomb_image):
        rect_player = get_rect(man.hitbox[0], man.hitbox[1], man.hitbox[2], man.hitbox[3])
        bomb_x = rect_player[0]
        bomb_y = rect_player[1]

        keys = pygame.key.get_pressed()
        
        timer = 0
        
        while timer < 100 :
 #           print ("in timer", timer)
            if keys[pygame.K_LEFT]:
                bomb_x = rect_player[0] - rect_player[2] - man.vel * 2
                bomb_y = rect_player[1]
                if bomb_x > 0:
                    print ("affiche la bombe a gauche")
                    win.blit(bomb_image, (bomb_x, bomb_y))
                    Item.delete_other_displayed_bomb("left")
                    pygame.display.update()   
                timer = 100 
                
            if keys[pygame.K_RIGHT]:
                rect_player.center
                bomb_x = rect_player[0] + rect_player[2] + man.vel
                bomb_y = rect_player[1]
                bomb_x_test = bomb_x + 50
                if bomb_x_test < win_width_boundary :
                    print ("affiche la bombe a droite")
                    win.blit(bomb_image, (bomb_x, bomb_y))
                    Item.delete_other_displayed_bomb("right")
                    pygame.display.update()               
                timer = 100
                
            if keys[pygame.K_UP]:
                bomb_x = rect_player[0] 
                bomb_y = rect_player[1] - rect_player[3] - man.vel * 2
                if bomb_y > 0:
                    print ("affiche la bombe en haut")
                    print (bomb_x)
                    print (man.vel)
                    win.blit(bomb_image, (bomb_x, bomb_y))
                    Item.delete_other_displayed_bomb("top")
                    pygame.display.update()   
                timer = 100
                
            if keys[pygame.K_DOWN]:
                bomb_x = rect_player[0] 
                bomb_y = rect_player[1] + rect_player[3] + man.vel
                bomb_y_test = bomb_y + 50
                if bomb_y_test < win_height_boundary:
                    print ("affiche la bombe en bas")
                    win.blit(bomb_image, (bomb_x, bomb_y))
                    Item.delete_other_displayed_bomb("bottom")
                    pygame.display.update()   
                timer = 100
            timer += 1
            
    def delete_other_displayed_bomb(pos_bomb_to_display):
        rect_player = get_rect(man.hitbox[0], man.hitbox[1], man.hitbox[2], man.hitbox[3])
        x_rect_bomb_left = rect_player[0] - rect_player[2] - man.vel * 2
        y_rect_bomb_left = rect_player[1]
        x_rect_bomb_right = rect_player[0] + rect_player[2] + man.vel
        y_rect_bomb_right = rect_player[1]
        x_rect_bomb_top = rect_player[0]
        y_rect_bomb_top = rect_player[1] - rect_player[3] - man.vel * 2
        x_rect_bomb_bottom = rect_player[0]
        y_rect_bomb_bottom = rect_player[1] + rect_player[3] + man.vel
        
        rect_bomb_left = get_rect(x_rect_bomb_left, y_rect_bomb_left, 50, 50)
        rect_bomb_right = get_rect(x_rect_bomb_right, y_rect_bomb_right, 50, 50)  
        rect_bomb_top = get_rect(x_rect_bomb_top, y_rect_bomb_top, 50, 50)
        rect_bomb_bottom = get_rect(x_rect_bomb_bottom, y_rect_bomb_bottom, 50, 50)
              
##        pygame.draw.rect(win, (255,255,0), rect_bomb_left,2)
##        pygame.draw.rect(win, (255,255,0), rect_bomb_right,2)
##        pygame.draw.rect(win, (255,255,0), rect_bomb_top,2)
##        pygame.draw.rect(win, (255,255,0), rect_bomb_bottom,2)
        
        display_rect_bomb_left = False
        if x_rect_bomb_left > man.vel and x_rect_bomb_left < win_width_boundary - man.vel:
            if y_rect_bomb_left >  man.vel and y_rect_bomb_left < win_height_boundary - man.vel:
                bombs_background_pict_left = field.get_close_picture_background(pict_background, rect_bomb_left)
                display_rect_bomb_left = True
                
        display_rect_bomb_right = False
        right_side_rect_bomb_right = x_rect_bomb_right + 51
        if right_side_rect_bomb_right > man.vel and right_side_rect_bomb_right < win_width_boundary - man.vel :
            if right_side_rect_bomb_right >  man.vel and right_side_rect_bomb_right < win_height_boundary - man.vel:
                pygame.draw.rect(win, (255,255,0), rect_bomb_right,2)
                bombs_background_pict_right = field.get_close_picture_background(pict_background, rect_bomb_right)
                display_rect_bomb_right = True

        display_rect_bomb_top = False
        if x_rect_bomb_top > man.vel and x_rect_bomb_top < win_width_boundary - man.vel :
            if y_rect_bomb_top >  man.vel and y_rect_bomb_top < win_height_boundary - man.vel:
                bombs_background_pict_top = field.get_close_picture_background(pict_background, rect_bomb_top)
                display_rect_bomb_top = True

        display_rect_bomb_bottom = False
        bottom_side_rect_bomb_bottom = x_rect_bomb_bottom + 51
        if bottom_side_rect_bomb_bottom > man.vel and bottom_side_rect_bomb_bottom < win_width_boundary - man.vel:
            if bottom_side_rect_bomb_bottom >  man.vel and bottom_side_rect_bomb_bottom < win_height_boundary - man.vel:
                bombs_background_pict_bottom = field.get_close_picture_background(pict_background, rect_bomb_bottom)
                display_rect_bomb_bottom = True        

        if pos_bomb_to_display == "left" :
            if display_rect_bomb_right :
                win.blit(bombs_background_pict_right,(x_rect_bomb_right, y_rect_bomb_right))
            if display_rect_bomb_top :
                win.blit(bombs_background_pict_top,(x_rect_bomb_top, y_rect_bomb_top))
            if display_rect_bomb_bottom :
                win.blit(bombs_background_pict_bottom,(x_rect_bomb_bottom, y_rect_bomb_bottom))
        if pos_bomb_to_display == "right" :
            if display_rect_bomb_left :
                win.blit(bombs_background_pict_left,(x_rect_bomb_left, y_rect_bomb_left))
            if display_rect_bomb_top :
                win.blit(bombs_background_pict_top,(x_rect_bomb_top, y_rect_bomb_top))
            if display_rect_bomb_bottom :
                win.blit(bombs_background_pict_bottom,(x_rect_bomb_bottom, y_rect_bomb_bottom))
        if pos_bomb_to_display == "top" :
            if display_rect_bomb_left :
                win.blit(bombs_background_pict_left,(x_rect_bomb_left, y_rect_bomb_left))
            if display_rect_bomb_right :
                win.blit(bombs_background_pict_right,(x_rect_bomb_right, y_rect_bomb_right))
            if display_rect_bomb_bottom :
                win.blit(bombs_background_pict_bottom,(x_rect_bomb_bottom, y_rect_bomb_bottom))
        if pos_bomb_to_display == "bottom" :
            if display_rect_bomb_left :
                win.blit(bombs_background_pict_left,(x_rect_bomb_left, y_rect_bomb_left))
            if display_rect_bomb_right :
                win.blit(bombs_background_pict_right,(x_rect_bomb_right, y_rect_bomb_right))
            if display_rect_bomb_top :
                win.blit(bombs_background_pict_top,(x_rect_bomb_top, y_rect_bomb_top))
    
##############################################
######    Affichage du fond d'écran     ######
##############################################
class display(object):         
    def redraw_game_windows():
        rect_display_player = field.get_close_player_rect(man)
        pygame.display.update()
        close_picture_background_player = field.get_close_picture_background(pict_background, rect_display_player)

        win.blit(close_picture_background_player, (man.hitbox[0] - man.vel, man.hitbox[1] - man.vel))
        man.draw(win)
        
        pygame.display.update()
     
    def display_box_inventory():
        if index_of_inventory[0] >= 0 :
            win.blit(tile_hud1[0], (900, 600))
            win.blit(Inventory[index_of_inventory[0]][1], (920, 620))
            pygame.display.update()
     

##############################################
   ####          MAINLOOP          ########
####################   #######################
    
# print (walls)
field.create_matrice(tiles_1)
Inventory = []
index_of_inventory = [-1] #index of current item
load_map_1 = True
first_time_map_load = True
load_map_2 = False
first_time_map2_load = True
load_map_3 = False
first_time_map3_load = True

run = True
while run:
    pygame.time.delay(20)
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
#        print ("event detwin_height_boundaryected", event)
        if event.type == pygame.QUIT :
            run = False
        if event.type == pygame.KEYUP and event.key == K_ESCAPE:    
            run = False
            
        if event.type == pygame.KEYUP and event.key == K_x:
            Item.change_item_in_inventory(index_of_inventory)

#        if event.type == pygame.KEYDOWN and event.key == K_b:
        if keys[pygame.K_b] :
            Item.display_a_bomb(green_bomb)
            print ("vous avez appuyé sur b")

####################"###########################
####################"###########################
###############    MAP  1   ####################
# pygame.draw.rect(win, (255,255,0), rectangle,2)

    if load_map_1 == True:      
        field.draw_tiles_of_field(tiles_1)        
        win.blit (arrow_right, ( 920, 120))
        
   
        if first_time_map_load == True:
            man = player(100, 100, 64,64)
        
            items_map_1 = pygame.sprite.Group()
            golden_key_sprite = Item("golden_key", golden_key, 150, 550, 50, 50)
            items_map_1.add(golden_key_sprite)

            rect_door1 = get_rect(300, 300, 100, 100)
            pos_door1 = False
            
            first_time_map_load = False
            
##        for sprite_map_1 in items_map_1:
##            if sprite_map_1.never_touched == True:
##                print ("")
##                print ("je vais afficher ",sprite_map_1.name)
        
        pict_background = field.get_picture_background()
        rect_display_player = field.get_close_player_rect(man)     
        close_picture_background_player = field.get_close_picture_background(pict_background, rect_display_player)

        items_map_1.draw(win)        
        display.display_box_inventory()         # Affichage de l'item dans la case inventaire
        
        walls = []
        wall.add_to_a_wall_list(tiles_1)
        
        man.draw(win)
        man.draw_in_hud()
        pygame.display.update()

        
        map_number = 1
        load_map_1 = False

        
    if map_number == 1 :
        rect_arrow_next_map = get_rect(920, 135,75,49)
        rect_player = get_rect(man.hitbox[0], man.hitbox[1], man.hitbox[2], man.hitbox[3])
        
        for item in items_map_1:
            if Item.player_touch_item(item):
                Item.add_item_in_inventory(item)
                Item.delete_item_from_map(item, items_map_1)
                display.redraw_game_windows()

        
        if rect_door1.colliderect(rect_player):
            if Item.is_item_selected("golden_key") or pos_door1 == True:
                wall.delete_wall(300, 300)
                if pos_door1 == False:
                    tiles_1[3][3] = 71
                    load_map_1 = True
                    pos_door1 = True
                
       
##        pygame.draw.rect(win, (255,255,0), golden_key_sprite,2)
##        pygame.display.update()

      
        if rect_arrow_next_map.colliderect(rect_player):
            man.x = 100
            man.y = 100
            load_map_2 = True

####################"###########################
####################"###########################
###############    MAP  2   ####################

    if load_map_2 == True :  
        field.draw_tiles_of_field(tiles_2)
        win.blit(arrow_right, (20, 120))
        win.blit(hole_ladder, (430, 70))
        
        if first_time_map2_load == True:
            man = player(100, 100, 64,64)
            
            items_map_2 = pygame.sprite.Group()
#            blue_bomb_sprite = Item("blue_bomb", blue_bomb, 200, 0, 50, 50)
#            orange_bomb_sprite = Item("orange_bomb", orange_bomb, 300, 100, 50, 50)
            green_bomb_sprite = Item("green_bomb", green_bomb, 600, 250, 50, 50)
            items_map_2.add(green_bomb_sprite)
            first_time_map2_load = False
            
       
        pict_background = field.get_picture_background()
        rect_display_player = field.get_close_player_rect(man)     
        close_picture_background_player = field.get_close_picture_background(pict_background, rect_display_player)

        items_map_2.draw(win)        
        display.display_box_inventory()
        
        walls = []
        wall.add_to_a_wall_list(tiles_2)

        man.draw(win)
        man.draw_in_hud()
        pygame.display.update()

        map_number = 2
        load_map_2 = False

    if map_number == 2 :
        rect_arrow_previous_map = get_rect(20, 135,75,49)
        rect_hole_next_map = get_rect(485, 100, 10, 20)
        rect_player = get_rect(man.hitbox[0], man.hitbox[1], man.hitbox[2], man.hitbox[3])


        for item in items_map_2:
            if Item.player_touch_item(item):
                Item.add_item_in_inventory(item)
                Item.delete_item_from_map(item, items_map_2)
                display.redraw_game_windows()

        
        if rect_arrow_previous_map.colliderect(rect_player):
            man.x = 900
            man.y = 20
            load_map_1 = True
        if rect_hole_next_map.colliderect(rect_player):
            man.x = 510
            man.y = 100
            load_map_3 = True


####################"###########################
####################"###########################
###############    MAP  3   ####################

    if load_map_3 == True :  
        field.draw_tiles_of_field(tiles_3)
        win.blit(hole_ladder, (380, 90))
        
        if first_time_map3_load == True:
            man = player(510, 100, 64,64)
            
            items_map_3 = pygame.sprite.Group()
#            blue_bomb_sprite = Item("blue_bomb", blue_bomb, 200, 0, 50, 50)
            orange_bomb_sprite = Item("orange_bomb", orange_bomb, 100, 100, 50, 50)
            items_map_3.add(orange_bomb_sprite)
            first_time_map3_load = False
            
        
        pict_background = field.get_picture_background()
        rect_display_player = field.get_close_player_rect(man)     
        close_picture_background_player = field.get_close_picture_background(pict_background, rect_display_player)

        items_map_3.draw(win)        
        display.display_box_inventory()
        
        walls = []
        wall.add_to_a_wall_list(tiles_3)

        man.draw(win)
        man.draw_in_hud()
        pygame.display.update()

        map_number = 3
        load_map_3 = False

    if map_number == 3 :
        rect_hole_previous_map = get_rect(415, 120, 10, 20)
        rect_player = get_rect(man.hitbox[0], man.hitbox[1], man.hitbox[2], man.hitbox[3])


        for item in items_map_3:
            if Item.player_touch_item(item):
                Item.add_item_in_inventory(item)
                Item.delete_item_from_map(item, items_map_3)
                display.redraw_game_windows()
                
        if rect_hole_previous_map.colliderect(rect_player):
            man.x = 350
            man.y = 110
            load_map_2 = True
            
#        pygame.draw.rect(win, (255,255,0), rect_arrow_next_map,2)
#        pygame.display.update()
        
# Movements with keyboard
    test_collide = wall.test_collide_wall()

    if test_collide == 1:
        man.x = x_old
        man.y = y_old
    x_old = man.x
    y_old = man.y


    if keys[pygame.K_LEFT] and not keys[pygame.K_b]:
        if man.hitbox[0] > man.vel* 2:
            man.x -= man.vel
            display.redraw_game_windows()
    
    if keys[pygame.K_RIGHT] and not keys[pygame.K_b]:
        if man.hitbox[0] + man.hitbox[2] < win_width_boundary - man.vel * 2:
            man.x += man.vel
            display.redraw_game_windows()
            
    if keys[pygame.K_UP] and not keys[pygame.K_b]:
        if man.hitbox[1] > man.vel* 2:
            man.y -= man.vel
            display.redraw_game_windows()

    if keys[pygame.K_DOWN] and not keys[pygame.K_b]:
        if man.hitbox[1] + man.hitbox[3] < win_height_boundary -man.vel:
            man.y += man.vel
            display.redraw_game_windows()
              



  
pygame.quit()
