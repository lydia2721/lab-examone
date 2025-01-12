# Question number 4a
import pygame
import os
WIDTH, HEIGHT = 400,500
pygame.display.set_caption("Quit")


def main():
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run  = False
        
    pygame.quit()


if __name__ == "__main__":
    main()
 
 