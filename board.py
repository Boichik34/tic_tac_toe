import pygame
import game
import player



class Board:
    def __init__(self, square=None,
                 square_shadow_1=None,
                 square_shadow_2=None,
                 square_shadow_3=None,
                 square_shadow_4=None,
                 square_shadow_5=None,
                 square_shadow_6=None,
                 square_shadow_7=None,
                 square_shadow_8=None,
                 square_shadow_9=None
                 ):
        self.square = pygame.Surface((220, 220))
        self.square_shadow_1 = self.square.get_rect(topleft=(10, 10))
        self.square_shadow_2 = self.square.get_rect(topleft=(240, 10))
        self.square_shadow_3 = self.square.get_rect(topleft=(470, 10))
        self.square_shadow_4 = self.square.get_rect(topleft=(10, 240))
        self.square_shadow_5 = self.square.get_rect(topleft=(240, 240))
        self.square_shadow_6 = self.square.get_rect(topleft=(470, 240))
        self.square_shadow_7 = self.square.get_rect(topleft=(10, 470))
        self.square_shadow_8 = self.square.get_rect(topleft=(240, 470))
        self.square_shadow_9 = self.square.get_rect(topleft=(470, 470))



    def create_window(self):
        Game = game.Game()
        pygame.init()
        self.square.fill('White')
        Game.screen.fill('Black')
        Game.screen.blit(self.square, (10, 10))
        Game.screen.blit(self.square, (240, 10))
        Game.screen.blit(self.square, (470, 10))
        Game.screen.blit(self.square, (10, 240))
        Game.screen.blit(self.square, (240, 240))
        Game.screen.blit(self.square, (470, 240))
        Game.screen.blit(self.square, (10, 470))
        Game.screen.blit(self.square, (240, 470))
        Game.screen.blit(self.square, (470, 470))
        # Game.screen.blit(icon_1, (56, 56))
        # Game.screen.blit(icon_2, (286, 286))
        pygame.time.delay(20)
        pygame.display.update()
        #while True:
        # icon_1 = player_1.player_icon
        # icon_2 = player_2.player_icon


    def draw_icon(self, lst, lst2, lst3):
        Game = game.Game()
        self.create_window()
        for el,x, y in zip(lst, lst2, lst3):
            Game.screen.blit(el, (x + 41, y + 41))




