import pygame
import game



def main():
    global CLOCK
    global SCREEN
    GAME = game.Game()
    while True:
        GAME.create_game()


if __name__ == '__main__':
    main()