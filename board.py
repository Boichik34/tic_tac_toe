import pygame
import game
import player

class Board:


    def create_window():
        Game = game.Game()
        pygame.init()

        # icon_1 = player_1.player_icon
        # icon_2 = player_2.player_icon
        square = pygame.Surface((220, 220))
        square.fill('White')
        square_shadow_1 = square.get_rect(topleft=(15, 15))
        square_shadow_2 = square.get_rect(topleft=(245, 15))
        square_shadow_3 = square.get_rect(topleft=(475, 15))
        square_shadow_4 = square.get_rect(topleft=(15, 245))
        square_shadow_5 = square.get_rect(topleft=(245, 245))
        square_shadow_6 = square.get_rect(topleft=(475, 245))
        square_shadow_7 = square.get_rect(topleft=(15, 475))
        square_shadow_8 = square.get_rect(topleft=(245, 475))
        square_shadow_9 = square.get_rect(topleft=(475, 475))

        while True:
            Game.screen.fill('Black')
            Game.screen.blit(square, (15, 15))
            Game.screen.blit(square, (245, 15))
            Game.screen.blit(square, (475, 15))
            Game.screen.blit(square, (15, 245))
            Game.screen.blit(square, (245, 245))
            Game.screen.blit(square, (475, 245))
            Game.screen.blit(square, (15, 475))
            Game.screen.blit(square, (245, 475))
            Game.screen.blit(square, (475, 475))
            # Game.screen.blit(icon_1, (56, 56))
            # Game.screen.blit(icon_2, (286, 286))
            pygame.display.update()




