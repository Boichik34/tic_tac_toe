import pygame
import buttons
import player

class Game:
    def __init__(self, backfone=None, screen=None):
        self.backfone = pygame.image.load('pictures/peakpx (2).jpg')
        self.screen = pygame.display.set_mode((700, 700))  # моё окно. его размер

    def create_game(self):
        pygame.init()
        pygame.display.set_caption("tic tac toe")  # устанавливаем название
        pygame.display.set_icon(pygame.image.load("pictures/icon.png"))  # устанавливаем икону(подгрузка изоброжения)
        myfont = pygame.font.Font('fonts/YoungSerif-Regular.ttf', 50)  # добавляем шрифт
        text = myfont.render('one player', True, ('Red'))
        text_2 = myfont.render('two player', True, ('Red'))
        text_shadow = text.get_rect(topleft=(200, 20))
        text_shadow_2 = text_2.get_rect(topleft=(200, 600))



        nevixod = True

        while nevixod:
            self.screen.blit(self.backfone, (0, 0))  # создаем в окне фигуру "square"
            self.screen.blit(text, text_shadow)
            self.screen.blit(text_2, text_shadow_2)
            mouse = pygame.mouse.get_pos()
            if text_shadow.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
                PLAYER_1 = player.Player(player, 'Mario')
                PLAYER_1.player_icon = self.chose_icon()
                print(PLAYER_1.player_icon)
                self.start_game(PLAYER_1)

            #elif text_shadow_2.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:

            for event in pygame.event.get():  # проверяет на событие
                if event.type == pygame.QUIT:  # если событие = выход
                    pygame.quit()  # выход
                    nevixod = False
            pygame.display.update()  # обновляем окно
    def chose_icon(self):
        pygame.init()
        icon_c1 = pygame.image.load('pictures/c1.png').convert_alpha()
        myfont = pygame.font.Font('fonts/YoungSerif-Regular.ttf', 70)
        icon_c2 = pygame.image.load('pictures/c2.png').convert_alpha()
        icon_c3 = pygame.image.load('pictures/c3.png').convert_alpha()
        icon_c4 = pygame.image.load('pictures/c4.png').convert_alpha()
        icon_c5 = pygame.image.load('pictures/c5.png').convert_alpha()
        icon_c6 = pygame.image.load('pictures/c6.png').convert_alpha()
        icon_c7 = pygame.image.load('pictures/c7.png').convert_alpha()
        icon_c8 = pygame.image.load('pictures/c8.png').convert_alpha()
        icon_c9 = pygame.image.load('pictures/c9.png').convert_alpha()
        backefone = pygame.image.load('pictures/peakpx (4).jpg')
        text_icon = myfont.render('choose an icon', True, 'Red')
        icon_1_shadow = icon_c1.get_rect(topleft=(58, 140))
        icon_2_shadow = icon_c1.get_rect(topleft=(58, 340))
        icon_3_shadow = icon_c1.get_rect(topleft=(58, 540))
        icon_4_shadow = icon_c1.get_rect(topleft=(286, 140))
        icon_5_shadow = icon_c1.get_rect(topleft=(286, 340))
        icon_6_shadow = icon_c1.get_rect(topleft=(286, 540))
        icon_7_shadow = icon_c1.get_rect(topleft=(514, 140))
        icon_8_shadow = icon_c1.get_rect(topleft=(514, 340))
        icon_9_shadow = icon_c1.get_rect(topleft=(514, 540))

        r = True
        while r:

            self.screen.blit(backefone, (0, 0))
            self.screen.blit(text_icon, (110, 5))
            self.screen.blit(icon_c1, icon_1_shadow)
            self.screen.blit(icon_c2, icon_2_shadow)
            self.screen.blit(icon_c3, icon_3_shadow)
            self.screen.blit(icon_c4, icon_4_shadow)
            self.screen.blit(icon_c5, icon_5_shadow)
            self.screen.blit(icon_c6, icon_6_shadow)
            self.screen.blit(icon_c7, icon_7_shadow)
            self.screen.blit(icon_c8, icon_8_shadow)
            self.screen.blit(icon_c9, icon_9_shadow)
            pygame.display.update()
            mouse = pygame.mouse.get_pos()
            if icon_1_shadow.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
                self.screen.blit(icon_c4, (0, 0))
                return icon_c1

            for event in pygame.event.get():  # проверяет на событие
                if event.type == pygame.QUIT:  # если событие = выход
                    pygame.quit()  # выход
                    r = False

    def start_game(self, player_):
        pygame.init()
        icon = player_.player_icon
        while True:

            self.screen.fill('White')
            self.screen.blit(icon, (20, 30))
            pygame.display.update()






        # game = Game
# game.create_game(game)