import pygame

pygame.init()
fenetre = pygame.display.set_mode((600, 500))
pygame.display.set_caption("LA GRILLE")

matrice = [[ 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 0],
           [ 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
           [ 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1],
           [ 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
           [ 1, 0, 0, 0, 1, 0, 2, 0, 0, 0, 0, 0],
           [ 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1],
           [ 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
           [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
           [ 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1],
           [ 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0]]


def get_rect(x, y, width, height):
    return pygame.Rect(x, y, width, height)
def create_matrice():
          
##            position_x_element = element_increment*50
##            position_y_element = ligne_increment*50
##            pygame.draw.rect(fenetre, (255, 255, 255),get_rect(position_x_element, position_y_element, 50, 50), 2)
            
##            if element == 0 :
##                pygame.draw.rect(fenetre, (0,0,0),get_rect(position_x_element + 2, position_y_element + 2, 50 - 3, 50 - 3))
##            if element == 1 :
##                pygame.draw.rect(fenetre, (255, 255, 255),get_rect(position_x_element, position_y_element, 50, 50))
##            if element == 2 :
##                pygame.draw.rect(fenetre, (255,255,0),get_rect(position_x_element, position_y_element, 50, 50))



    pygame.display.update()

create_matrice()
