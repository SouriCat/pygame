import pygame
import random
from pygame.locals import *
pygame.init()

largeur_ecran = 600
hauteur_ecran = 500
taille_des_carres = 50
nombre_case_hauteur = 11
nombre_case_largeur = 9

VERTJAUNE = (173,255,47)
VERT = (0,128,0)

fenetre = pygame.display.set_mode((largeur_ecran, hauteur_ecran))
pygame.display.set_caption("Le jeu du serpent collaboratif")


matrice = [[ 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
           [ 1, 2, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1],
           [ 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1],
           [ 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
           [ 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1],
           [ 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1],
           [ 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
           [ 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
           [ 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1],
           [ 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]


def get_rect(x, y, width, height):
    return pygame.Rect(x, y, width, height)

def move_green():
    moved = False
    keys = pygame.key.get_pressed()   
    position_x_vert = position_vert[0]
    position_y_vert = position_vert[1]
#    print (position_x_vert, position_y_vert)
    position_x_vert_int = int(position_x_vert)
    position_y_vert_int = int(position_y_vert)
#    print (position_x_vert_int, position_y_vert_int)
#    print ("")

    if keys[pygame.K_UP] and position_x_vert_int > 0:
        if not keys[pygame.K_LEFT] and not keys[pygame.K_RIGHT]:
            if matrice[position_x_vert_int - 1][position_y_vert_int] == 0:
                matrice[position_vert[0] - 1][position_vert[1]] = 2
                matrice[position_vert[0]][position_vert[1]] = 3
                position_vert[0] -= 1
                moved = True

    if keys[pygame.K_DOWN] and position_x_vert_int < 9:
        if not keys[pygame.K_LEFT] and not keys[pygame.K_RIGHT]:
            if matrice[position_x_vert_int + 1][position_y_vert_int] == 0:
                matrice[position_vert[0] + 1][position_vert[1]] = 2
                matrice[position_vert[0]][position_vert[1]] = 3
                position_vert[0] += 1
                moved = True
        
    if keys[pygame.K_LEFT] and position_y_vert_int > 0 :
        if not keys[pygame.K_UP] and not keys[pygame.K_DOWN]:
            if matrice[position_x_vert_int][position_y_vert_int - 1] == 0:
                matrice[position_vert[0]][position_vert[1] - 1] = 2
                matrice[position_vert[0]][position_vert[1]] = 3
                position_vert[1] -= 1
                moved = True
                
    if keys[pygame.K_RIGHT] and position_y_vert_int < 11:
        if not keys[pygame.K_UP] and not keys[pygame.K_DOWN]:
            if matrice[position_x_vert_int][position_y_vert_int + 1] == 0:   
                matrice[position_vert[0]][position_vert[1] + 1] = 2
                matrice[position_vert[0]][position_vert[1]] = 3
                position_vert[1] += 1
                moved = True
                
    return moved


def create_matrice(matrice):
    ligne_increment = 0
    for ligne in matrice:        
        element_increment = 0
        for element in ligne:  
            position_x_element = element_increment*taille_des_carres
            position_y_element = ligne_increment*taille_des_carres
            pygame.draw.rect(fenetre, (255, 255, 255),get_rect(position_x_element, position_y_element, taille_des_carres, taille_des_carres), 2)
            
### Parfait pour apprendre les conditions
            if element == 0 :
                pygame.draw.rect(fenetre, (0,0,0),get_rect(position_x_element + 2, position_y_element + 2, taille_des_carres - 3, taille_des_carres - 3))
            if element == 1 :
                pygame.draw.rect(fenetre, (255, 255, 255),get_rect(position_x_element, position_y_element, taille_des_carres, taille_des_carres))
            if element == 2 :
                pygame.draw.rect(fenetre, VERTJAUNE,get_rect(position_x_element, position_y_element, taille_des_carres, taille_des_carres))
            if element == 3 :
                pygame.draw.rect(fenetre, VERTJAUNE,get_rect(position_x_element, position_y_element, taille_des_carres, taille_des_carres))
  
            element_increment += 1
        element_increment = 0       
        ligne_increment += 1
    pygame.display.update()

def dessiner_la_queue(matrice, taille_queue):
    ligne_increment = 0
    for ligne in matrice:
        element_increment = 0
        for element in ligne:  
            if element >= 3 :
                matrice[ligne_increment][element_increment] += 1
                if matrice[ligne_increment][element_increment] > taille_queue:
                    matrice[ligne_increment][element_increment] = 0
  
            element_increment += 1
        element_increment = 0       
        ligne_increment += 1


    
def donne_image_d_un_fruit():
    pomme = pygame.image.load('pomme.png')
    banane = pygame.image.load('banane.png')
    cerise = pygame.image.load('cerise.png')
    image_fruit = pomme
    randomisator = random.randint(0, 2)
    if randomisator == 0 :
        image_fruit = pygame.image.load('pomme.png')
    if randomisator == 1 :
        image_fruit = pygame.image.load('banane.png')
    if randomisator == 2 :
        image_fruit = pygame.image.load('cerise.png')
    return image_fruit


def create_fruit(fruit):
    displayed = False
    while displayed == False:
        position_fruit[0] = random.randint(1,nombre_case_largeur)
        position_fruit[1] = random.randint(0,nombre_case_hauteur)
        if matrice[position_fruit[0]][position_fruit[1]] == 0 :
            print (position_fruit[0], position_fruit[1])
            fenetre.blit(fruit, (position_fruit[1] * 50, position_fruit[0] * 50))
            pygame.display.update()
            displayed = True
    return displayed

def display_fruit():
    fenetre.blit(fruit, (position_fruit[1] * 50, position_fruit[0] * 50))

def eat_fruit():
    fruit_displayed = True
    if position_fruit[0] == position_vert[0] and position_fruit[1] == position_vert[1]:
        fruit_displayed = False 
    return fruit_displayed

position_vert = [1, 1]
position_fruit = [1, 1]
create_matrice(matrice)
fruit_displayed = False
run = True
ca_joue = True
taille_queue = 2
while run:
    pygame.time.delay(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT :
            run = False
            
    if ca_joue :
        moved = False      
        moved = move_green()
        if moved :
            dessiner_la_queue(matrice, taille_queue)
        
        create_matrice(matrice)
        if fruit_displayed == False:
            fruit = donne_image_d_un_fruit()
            fruit_displayed = create_fruit(fruit)
            taille_queue += 1
        
        fruit_displayed = eat_fruit()
        if matrice[position_fruit[0]][position_fruit[1]] == 0 :
            display_fruit()

        vert1 = position_vert[0]  
        horiz2 = position_vert[1]
        pygame.display.update()
        print (position_vert[1], position_vert[0])
        if not matrice[vert1 - 1][position_vert[1]] == 0:
            print ("etape 2")
            if not matrice[vert1 + 1][position_vert[1]] == 0:
                print ("etape 3")
                if not matrice[position_vert[0]][horiz2 - 1] == 0:
                    print ("etape 4")
                    if not matrice[position_vert[0]][horiz2 + 1] == 0:
                        pygame.time.delay(3000)
                        ca_joue = False

    else :
        pygame.time.delay(100)
        fenetre.fill((VERTJAUNE))
        
        font= pygame.font.Font(None, 60)
        text = font.render("Game oveR",1,(0,0,0))
        fenetre.blit(text, (180, 200))
        
        font= pygame.font.Font(None, 40)
        message2 ="Your score is : " + str(taille_queue - 3)
        text2 = font.render(message2,1,(0,0,0))
        fenetre.blit(text2, (185, 250))
        pygame.display.update()
        pygame.time.delay(3000)
        run = False
pygame.quit()
