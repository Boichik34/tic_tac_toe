import pygame
import buttons
import player
import board

Board = board.Board()
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
            PLAYER_1 = player.Player(player, 'Mario')
            PLAYER_2 = player.Player(player, 'Luigi')
            PLAYER_1.player_icon = None
            PLAYER_2.player_icon = None


            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and text_shadow_2.collidepoint(mouse):
                    PLAYER_1.player_icon = self.chose_icon()
                    print(PLAYER_1.player_icon)
                    PLAYER_2.player_icon = self.chose_icon_2()
                    print(PLAYER_2.player_icon)
                    self.start_game(PLAYER_1, PLAYER_2)

                # проверяет на событие
                if event.type == pygame.QUIT:  # если событие = выход
                    pygame.quit()  # выход
                    nevixod = False
            pygame.display.update()  # обновляем окно
    def chose_icon(self):
        pygame.init()
        myfont = pygame.font.Font('fonts/YoungSerif-Regular.ttf', 50)
        icon_c1 = pygame.image.load('pictures/c1.png').convert_alpha()
        icon_c2 = pygame.image.load('pictures/c2.png').convert_alpha()
        icon_c3 = pygame.image.load('pictures/c3.png').convert_alpha()
        icon_c4 = pygame.image.load('pictures/c4.png').convert_alpha()
        icon_c5 = pygame.image.load('pictures/c5.png').convert_alpha()
        icon_c6 = pygame.image.load('pictures/c6.png').convert_alpha()
        icon_c7 = pygame.image.load('pictures/c7.png').convert_alpha()
        icon_c8 = pygame.image.load('pictures/c8.png').convert_alpha()
        icon_c9 = pygame.image.load('pictures/c9.png').convert_alpha()
        backefone = pygame.image.load('pictures/peakpx (4).jpg')
        text_icon = myfont.render('Player 1 choose an icon', True, 'Red')
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
            self.screen.blit(text_icon, (50, 5))
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
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and icon_1_shadow.collidepoint(mouse):
                    return icon_c1
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and icon_2_shadow.collidepoint(mouse):
                    return icon_c2
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and icon_3_shadow.collidepoint(mouse):
                    return icon_c3
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and icon_4_shadow.collidepoint(mouse):
                    return icon_c4
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and icon_5_shadow.collidepoint(mouse):
                    return icon_c5
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and icon_6_shadow.collidepoint(mouse):
                    return icon_c6
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and icon_7_shadow.collidepoint(mouse):
                    return icon_c7
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and icon_8_shadow.collidepoint(mouse):
                    return icon_c8
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and icon_9_shadow.collidepoint(mouse):
                    return icon_c9
                if event.type == pygame.QUIT:
                    pygame.quit()
                    r = False

    def chose_icon_2(self):
        pygame.init()
        myfont = pygame.font.Font('fonts/YoungSerif-Regular.ttf', 50)
        text_icon = myfont.render('Player 2 choose an icon', True, 'Red')
        icon_n1 = pygame.image.load('pictures/r1.png').convert_alpha()
        icon_n2 = pygame.image.load('pictures/r2.png').convert_alpha()
        icon_n3 = pygame.image.load('pictures/r3.png').convert_alpha()
        icon_n4 = pygame.image.load('pictures/r4.png').convert_alpha()
        icon_n5 = pygame.image.load('pictures/r5.png').convert_alpha()
        icon_n6 = pygame.image.load('pictures/r6.png').convert_alpha()
        icon_n7 = pygame.image.load('pictures/r7.png').convert_alpha()
        icon_n8 = pygame.image.load('pictures/r8.png').convert_alpha()
        icon_n9 = pygame.image.load('pictures/r9.png').convert_alpha()
        backefone = pygame.image.load('pictures/peakpx (4).jpg')
        icon_1_shadow = icon_n1.get_rect(topleft=(58, 140))
        icon_2_shadow = icon_n2.get_rect(topleft=(58, 340))
        icon_3_shadow = icon_n3.get_rect(topleft=(58, 540))
        icon_4_shadow = icon_n4.get_rect(topleft=(286, 140))
        icon_5_shadow = icon_n5.get_rect(topleft=(286, 340))
        icon_6_shadow = icon_n6.get_rect(topleft=(286, 540))
        icon_7_shadow = icon_n7.get_rect(topleft=(514, 140))
        icon_8_shadow = icon_n8.get_rect(topleft=(514, 340))
        icon_9_shadow = icon_n9.get_rect(topleft=(514, 540))

        r = True
        while r:

            self.screen.blit(backefone, (0, 0))
            self.screen.blit(text_icon, (50, 5))
            self.screen.blit(icon_n1, icon_1_shadow)
            self.screen.blit(icon_n2, icon_2_shadow)
            self.screen.blit(icon_n3, icon_3_shadow)
            self.screen.blit(icon_n4, icon_4_shadow)
            self.screen.blit(icon_n5, icon_5_shadow)
            self.screen.blit(icon_n6, icon_6_shadow)
            self.screen.blit(icon_n7, icon_7_shadow)
            self.screen.blit(icon_n8, icon_8_shadow)
            self.screen.blit(icon_n9, icon_9_shadow)
            pygame.display.update()
            mouse = pygame.mouse.get_pos()
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and icon_1_shadow.collidepoint(mouse):
                    return icon_n1
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and icon_2_shadow.collidepoint(mouse):
                    return icon_n2
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and icon_3_shadow.collidepoint(mouse):
                    return icon_n3
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and icon_4_shadow.collidepoint(mouse):
                    return icon_n4
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and icon_5_shadow.collidepoint(mouse):
                    return icon_n5
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and icon_6_shadow.collidepoint(mouse):
                    return icon_n6
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and icon_7_shadow.collidepoint(mouse):
                    return icon_n7
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and icon_8_shadow.collidepoint(mouse):
                    return icon_n8
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and icon_9_shadow.collidepoint(mouse):
                    return icon_n9
                if event.type == pygame.QUIT:
                    pygame.quit()
                    r = False

    def start_game(self, player_1, player_2):

        board.Board.create_window()

        # pygame.init()
        # icon_1 = player_1.player_icon
        # icon_2 = player_2.player_icon
        # square = pygame.Surface((220, 220))
        # square.fill('White')
        # square_shadow_1 = square.get_rect(topleft=(15, 15))
        # square_shadow_2 = square.get_rect(topleft=(245, 15))
        # square_shadow_3 = square.get_rect(topleft=(475, 15))
        # square_shadow_4 = square.get_rect(topleft=(15, 245))
        # square_shadow_5 = square.get_rect(topleft=(245, 245))
        # square_shadow_6 = square.get_rect(topeft=(475, 245))
        # square_shadow_7 = square.get_rect(toplleft=(15, 475))
        # square_shadow_8 = square.get_rect(topleft=(245, 475))
        # square_shadow_9 = square.get_rect(topleft=(475, 475))
        # while True:
        #     self.screen.fill('Black')
        #     self.screen.blit(icon_1, (20, 30))
        #     self.screen.blit(icon_2, (40, 330))
        #     self.screen.blit(square, (15, 15))
        #     self.screen.blit(square, (245, 15))
        #     self.screen.blit(square, (475, 15))
        #     self.screen.blit(square, (15, 245))
        #     self.screen.blit(square, (245, 245))
        #     self.screen.blit(square, (475, 245))
        #     self.screen.blit(square, (15, 475))
        #     self.screen.blit(square, (245, 475))
        #     self.screen.blit(square, (475, 475))
        #     self.screen.blit(icon_1, (56, 56))
        #     self.screen.blit(icon_2, (286, 286))
        pygame.display.update()







        # game = Game
# game.create_game(game)