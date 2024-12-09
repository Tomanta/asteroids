# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *

def game_loop(screen):
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        screen.fill(pygame.Color(0,0,0))
        pygame.display.flip()


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    game_loop(screen)


if __name__ == "__main__":
    main()