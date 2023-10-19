import pygame
import player
import board
import random

Board = board.Board()
class Game:
    def __init__(self, backfone=None,
                 screen=None,
                 icon_c1=None,
                 icon_c2=None,
                 icon_c3=None,
                 icon_c4=None,
                 icon_c5=None,
                 icon_c6=None,
                 icon_c7=None,
                 icon_c8=None,
                 icon_c9=None,
                 icon_n1=None,
                 icon_n2=None,
                 icon_n3=None,
                 icon_n4=None,
                 icon_n5=None,
                 icon_n6=None,
                 icon_n7=None,
                 icon_n8=None,
                 icon_n9=None
                 ):
        self.backfone = pygame.image.load('pictures/peakpx (2).jpg')
        self.screen = pygame.display.set_mode((700, 700), pygame.RESIZABLE)
        self.icon_c1 = pygame.image.load('pictures/c1.png').convert_alpha()
        self.icon_c2 = pygame.image.load('pictures/c2.png').convert_alpha()
        self.icon_c3 = pygame.image.load('pictures/c3.png').convert_alpha()
        self.icon_c4 = pygame.image.load('pictures/c4.png').convert_alpha()
        self.icon_c5 = pygame.image.load('pictures/c5.png').convert_alpha()
        self.icon_c6 = pygame.image.load('pictures/c6.png').convert_alpha()
        self.icon_c7 = pygame.image.load('pictures/c7.png').convert_alpha()
        self.icon_c8 = pygame.image.load('pictures/c8.png').convert_alpha()
        self.icon_c9 = pygame.image.load('pictures/c9.png').convert_alpha()
        self.icon_n1 = pygame.image.load('pictures/r1.png').convert_alpha()
        self.icon_n2 = pygame.image.load('pictures/r2.png').convert_alpha()
        self.icon_n3 = pygame.image.load('pictures/r3.png').convert_alpha()
        self.icon_n4 = pygame.image.load('pictures/r4.png').convert_alpha()
        self.icon_n5 = pygame.image.load('pictures/r5.png').convert_alpha()
        self.icon_n6 = pygame.image.load('pictures/r6.png').convert_alpha()
        self.icon_n7 = pygame.image.load('pictures/r7.png').convert_alpha()
        self.icon_n8 = pygame.image.load('pictures/r8.png').convert_alpha()
        self.icon_n9 = pygame.image.load('pictures/r9.png').convert_alpha()
        self.icon_rosk = pygame.image.load('pictures/rock.png')
        self.icon_s = pygame.image.load('pictures/s.png')
        self.icon_p = pygame.image.load('pictures/p.png')
        self.rock_shadow = self.icon_rosk.get_rect(topleft=(100, 500))
        self.s_shadow = self.icon_s.get_rect(topleft=(300, 500))
        self.p_shadow = self.icon_p.get_rect(topleft=(500, 500))

    def draw_fone(self):
        pygame.init()
        self.screen.blit(self.backfone, (0, 0))
        myfont = pygame.font.Font('fonts/YoungSerif-Regular.ttf', 64)
        text = myfont.render('let\'s go to', True, 'Red')
        text2 = myfont.render('"Rock Scissors Paper"', True, 'Red')
        text3 = myfont.render('who\'s first', True, 'Red')
        text4 = myfont.render('choose', True, 'Red')

        self.screen.blit(text, (230, 30))
        self.screen.blit(text2, (0, 120))
        self.screen.blit(text3, (190, 210))
        self.screen.blit(text4, (250, 350))
        self.screen.blit(self.icon_rosk, self.rock_shadow)
        self.screen.blit(self.icon_s, self.s_shadow)
        self.screen.blit(self.icon_p, self.p_shadow)

    def create_game(self):

        pygame.init()
        clock = pygame.time.Clock()
        pygame.display.set_caption("tic tac toe")  # устанавливаем название
        pygame.display.set_icon(pygame.image.load("pictures/icon.png"))  # устанавливаем икону(подгрузка изоброжения)
        myfont = pygame.font.Font('fonts/YoungSerif-Regular.ttf', 50)  # добавляем шрифт
        text = myfont.render('one player', True, ('Red'))
        text_2 = myfont.render('two player', True, ('Red'))
        text_shadow = text.get_rect(topleft=(200, 20))
        text_shadow_2 = text_2.get_rect(topleft=(200, 600))
        self.screen.blit(self.backfone, (0, 0))  # создаем в окне фигуру "square"
        self.screen.blit(text, text_shadow)
        self.screen.blit(text_2, text_shadow_2)

        PLAYER_1 = player.Player(player, 'Mario')
        PLAYER_2 = player.Player(player, 'Luigi')
        PLAYER_1.player_icon = None
        PLAYER_2.player_icon = None


        nevixod = True

        while nevixod:
            mouse = pygame.mouse.get_pos()


            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and text_shadow.collidepoint(mouse):
                    PLAYER_1.player_icon = self.chose_icon()
                    queue = queue = self.queueu()
                    self.start_game(PLAYER_1, queue)

                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and text_shadow_2.collidepoint(mouse):
                    PLAYER_1.player_icon = self.chose_icon()
                    PLAYER_2.player_icon = self.chose_icon_2()
                    queue = self.queueu_2()
                    self.start_game(PLAYER_1, queue, PLAYER_2)

                # проверяет на событие
                if event.type == pygame.QUIT:  # если событие = выход
                    pygame.quit()  # выход
                    nevixod = False
            pygame.display.update()  # обновляем окно
            clock.tick(10)
    def chose_icon(self):
        pygame.init()
        clock = pygame.time.Clock()
        myfont = pygame.font.Font('fonts/YoungSerif-Regular.ttf', 50)
        backefone = pygame.image.load('pictures/peakpx (4).jpg')
        text_icon = myfont.render('Player 1 choose an icon', True, 'Red')
        icon_1_shadow = self.icon_c1.get_rect(topleft=(58, 140))
        icon_2_shadow = self.icon_c1.get_rect(topleft=(58, 340))
        icon_3_shadow = self.icon_c1.get_rect(topleft=(58, 540))
        icon_4_shadow = self.icon_c1.get_rect(topleft=(286, 140))
        icon_5_shadow = self.icon_c1.get_rect(topleft=(286, 340))
        icon_6_shadow = self.icon_c1.get_rect(topleft=(286, 540))
        icon_7_shadow = self.icon_c1.get_rect(topleft=(514, 140))
        icon_8_shadow = self.icon_c1.get_rect(topleft=(514, 340))
        icon_9_shadow = self.icon_c1.get_rect(topleft=(514, 540))

        r = True
        while r:

            self.screen.blit(backefone, (0, 0))
            self.screen.blit(text_icon, (50, 5))
            self.screen.blit(self.icon_c1, icon_1_shadow)
            self.screen.blit(self.icon_c2, icon_2_shadow)
            self.screen.blit(self.icon_c3, icon_3_shadow)
            self.screen.blit(self.icon_c4, icon_4_shadow)
            self.screen.blit(self.icon_c5, icon_5_shadow)
            self.screen.blit(self.icon_c6, icon_6_shadow)
            self.screen.blit(self.icon_c7, icon_7_shadow)
            self.screen.blit(self.icon_c8, icon_8_shadow)
            self.screen.blit(self.icon_c9, icon_9_shadow)
            pygame.display.update()
            mouse = pygame.mouse.get_pos()
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and icon_1_shadow.collidepoint(mouse):
                    return self.icon_c1
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and icon_2_shadow.collidepoint(mouse):
                    return self.icon_c2
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and icon_3_shadow.collidepoint(mouse):
                    return self.icon_c3
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and icon_4_shadow.collidepoint(mouse):
                    return self.icon_c4
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and icon_5_shadow.collidepoint(mouse):
                    return self.icon_c5
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and icon_6_shadow.collidepoint(mouse):
                    return self.icon_c6
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and icon_7_shadow.collidepoint(mouse):
                    return self.icon_c7
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and icon_8_shadow.collidepoint(mouse):
                    return self.icon_c8
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and icon_9_shadow.collidepoint(mouse):
                    return self.icon_c9
                if event.type == pygame.QUIT:
                    pygame.quit()
                    r = False
            clock.tick(10)
    def chose_icon_2(self):
        pygame.init()
        clock = pygame.time.Clock()
        myfont = pygame.font.Font('fonts/YoungSerif-Regular.ttf', 50)
        text_icon = myfont.render('Player 2 choose an icon', True, 'Red')

        backefone = pygame.image.load('pictures/peakpx (4).jpg')
        icon_1_shadow = self.icon_n1.get_rect(topleft=(58, 140))
        icon_2_shadow = self.icon_n2.get_rect(topleft=(58, 340))
        icon_3_shadow = self.icon_n3.get_rect(topleft=(58, 540))
        icon_4_shadow = self.icon_n4.get_rect(topleft=(286, 140))
        icon_5_shadow = self.icon_n5.get_rect(topleft=(286, 340))
        icon_6_shadow = self.icon_n6.get_rect(topleft=(286, 540))
        icon_7_shadow = self.icon_n7.get_rect(topleft=(514, 140))
        icon_8_shadow = self.icon_n8.get_rect(topleft=(514, 340))
        icon_9_shadow = self.icon_n9.get_rect(topleft=(514, 540))

        r = True
        while r:

            self.screen.blit(backefone, (0, 0))
            self.screen.blit(text_icon, (50, 5))
            self.screen.blit(self.icon_n1, icon_1_shadow)
            self.screen.blit(self.icon_n2, icon_2_shadow)
            self.screen.blit(self.icon_n3, icon_3_shadow)
            self.screen.blit(self.icon_n4, icon_4_shadow)
            self.screen.blit(self.icon_n5, icon_5_shadow)
            self.screen.blit(self.icon_n6, icon_6_shadow)
            self.screen.blit(self.icon_n7, icon_7_shadow)
            self.screen.blit(self.icon_n8, icon_8_shadow)
            self.screen.blit(self.icon_n9, icon_9_shadow)
            pygame.display.update()
            mouse = pygame.mouse.get_pos()
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and icon_1_shadow.collidepoint(mouse):
                    return self.icon_n1
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and icon_2_shadow.collidepoint(mouse):
                    return self.icon_n2
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and icon_3_shadow.collidepoint(mouse):
                    return self.icon_n3
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and icon_4_shadow.collidepoint(mouse):
                    return self.icon_n4
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and icon_5_shadow.collidepoint(mouse):
                    return self.icon_n5
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and icon_6_shadow.collidepoint(mouse):
                    return self.icon_n6
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and icon_7_shadow.collidepoint(mouse):
                    return self.icon_n7
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and icon_8_shadow.collidepoint(mouse):
                    return self.icon_n8
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and icon_9_shadow.collidepoint(mouse):
                    return self.icon_n9
                if event.type == pygame.QUIT:
                    pygame.quit()
                    r = False
            clock.tick(10)

    def start_game(self, player_1, queue, player_2=None):
        
        board.Board.create_window(Board)
        clock = pygame.time.Clock()
        icon_lst = []
        x_lst = []
        y_lst = []
        shadow_lst = [Board.square_shadow_1,
                      Board.square_shadow_2,
                      Board.square_shadow_3,
                      Board.square_shadow_4,
                      Board.square_shadow_5,
                      Board.square_shadow_6,
                      Board.square_shadow_7,
                      Board.square_shadow_8,
                      Board.square_shadow_9,]
        line_1_lst = []
        line_2_lst = []
        line_3_lst = []
        column_1_lst = []
        column_2_lst = []
        column_3_lst = []
        dig_1_lst = []
        dig_2_lst = []

        r = 9
        while r != 0 :
            random_shadow = None
            if queue:
                if r % 2 == 1:
                    player_icon = player_1.player_icon
                    self.player_isgoing('player_1')

                else:
                    if not player_2:
                        player_icon = self.icon_n2
                        self.player_isgoing('player_2')
                        random_shadow = random.choice(shadow_lst)
                    else:
                        self.player_isgoing('player_2')
                        player_icon = player_2.player_icon

            else:
                if r % 2 == 1:
                    if player_2:
                        self.player_isgoing('player_2')
                        player_icon = player_2.player_icon
                    else:
                        self.player_isgoing('player_2')
                        player_icon = self.icon_n2
                        random_shadow = random.choice(shadow_lst)
                else:
                    self.player_isgoing('player_1')
                    player_icon = player_1.player_icon


            mouse = pygame.mouse.get_pos()
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    if Board.square_shadow_1.collidepoint(mouse) and Board.square_shadow_1 in shadow_lst:
                        x_lst.append(Board.square_shadow_1.x)
                        y_lst.append(Board.square_shadow_1.y)
                        icon_lst.append(player_icon)
                        Board.draw_icon(icon_lst, x_lst, y_lst)
                        shadow_lst.remove(Board.square_shadow_1)
                        line_1_lst.append(player_icon)
                        column_1_lst.append(player_icon)
                        dig_1_lst.append(player_icon)
                        r -= 1
                    if Board.square_shadow_2.collidepoint(mouse) and Board.square_shadow_2 in shadow_lst:
                        x_lst.append(Board.square_shadow_2.x)
                        y_lst.append(Board.square_shadow_2.y)
                        icon_lst.append(player_icon)
                        Board.draw_icon(icon_lst, x_lst, y_lst)
                        shadow_lst.remove(Board.square_shadow_2)
                        line_1_lst.append(player_icon)
                        column_2_lst.append(player_icon)
                        r -= 1
                    if Board.square_shadow_3.collidepoint(mouse) and Board.square_shadow_3 in shadow_lst:
                        x_lst.append(Board.square_shadow_3.x)
                        y_lst.append(Board.square_shadow_3.y)
                        icon_lst.append(player_icon)
                        Board.draw_icon(icon_lst, x_lst, y_lst)
                        shadow_lst.remove(Board.square_shadow_3)
                        line_1_lst.append(player_icon)
                        column_3_lst.append(player_icon)
                        dig_2_lst.append(player_icon)
                        r -= 1
                    if Board.square_shadow_4.collidepoint(mouse) and Board.square_shadow_4 in shadow_lst:
                        x_lst.append(Board.square_shadow_4.x)
                        y_lst.append(Board.square_shadow_4.y)
                        icon_lst.append(player_icon)
                        Board.draw_icon(icon_lst, x_lst, y_lst)
                        shadow_lst.remove(Board.square_shadow_4)
                        line_2_lst.append(player_icon)
                        column_1_lst.append(player_icon)
                        r -= 1
                    if Board.square_shadow_5.collidepoint(mouse) and Board.square_shadow_5 in shadow_lst:
                        x_lst.append(Board.square_shadow_5.x)
                        y_lst.append(Board.square_shadow_5.y)
                        icon_lst.append(player_icon)
                        Board.draw_icon(icon_lst, x_lst, y_lst)
                        shadow_lst.remove(Board.square_shadow_5)
                        line_2_lst.append(player_icon)
                        column_2_lst.append(player_icon)
                        dig_1_lst.append(player_icon)
                        dig_2_lst.append(player_icon)
                        r -= 1
                    if Board.square_shadow_6.collidepoint(mouse) and Board.square_shadow_6 in shadow_lst:
                        x_lst.append(Board.square_shadow_6.x)
                        y_lst.append(Board.square_shadow_6.y)
                        icon_lst.append(player_icon)
                        Board.draw_icon(icon_lst, x_lst, y_lst)
                        shadow_lst.remove(Board.square_shadow_6)
                        line_2_lst.append(player_icon)
                        column_3_lst.append(player_icon)
                        r -= 1
                    if Board.square_shadow_7.collidepoint(mouse) and Board.square_shadow_7 in shadow_lst:
                        x_lst.append(Board.square_shadow_7.x)
                        y_lst.append(Board.square_shadow_7.y)
                        icon_lst.append(player_icon)
                        Board.draw_icon(icon_lst, x_lst, y_lst)
                        shadow_lst.remove(Board.square_shadow_7)
                        line_3_lst.append(player_icon)
                        column_1_lst.append(player_icon)
                        dig_2_lst.append(player_icon)
                        r -= 1
                    if Board.square_shadow_8.collidepoint(mouse) and Board.square_shadow_8 in shadow_lst:
                        x_lst.append(Board.square_shadow_8.x)
                        y_lst.append(Board.square_shadow_8.y)
                        icon_lst.append(player_icon)
                        Board.draw_icon(icon_lst, x_lst, y_lst)
                        shadow_lst.remove(Board.square_shadow_8)
                        line_3_lst.append(player_icon)
                        column_2_lst.append(player_icon)
                        r -= 1
                    if Board.square_shadow_9.collidepoint(mouse) and Board.square_shadow_9 in shadow_lst:
                        x_lst.append(Board.square_shadow_9.x)
                        y_lst.append(Board.square_shadow_9.y)
                        icon_lst.append(player_icon)
                        Board.draw_icon(icon_lst, x_lst, y_lst)
                        shadow_lst.remove(Board.square_shadow_9)
                        line_3_lst.append(player_icon)
                        column_3_lst.append(player_icon)
                        dig_1_lst.append(player_icon)
                        r -= 1
                if event.type == pygame.QUIT:
                    pygame.quit()
                    r = 0
            if random_shadow == Board.square_shadow_1 and Board.square_shadow_1 in shadow_lst:
                x_lst.append(Board.square_shadow_1.x)
                y_lst.append(Board.square_shadow_1.y)
                icon_lst.append(player_icon)
                Board.draw_icon(icon_lst, x_lst, y_lst)
                shadow_lst.remove(Board.square_shadow_1)
                line_1_lst.append(player_icon)
                column_1_lst.append(player_icon)
                dig_1_lst.append(player_icon)
                r -= 1
            if random_shadow == Board.square_shadow_2 and Board.square_shadow_2 in shadow_lst:
                x_lst.append(Board.square_shadow_2.x)
                y_lst.append(Board.square_shadow_2.y)
                icon_lst.append(player_icon)
                Board.draw_icon(icon_lst, x_lst, y_lst)
                shadow_lst.remove(Board.square_shadow_2)
                line_1_lst.append(player_icon)
                column_2_lst.append(player_icon)
                r -= 1
            if random_shadow == Board.square_shadow_3 and Board.square_shadow_3 in shadow_lst:
                x_lst.append(Board.square_shadow_3.x)
                y_lst.append(Board.square_shadow_3.y)
                icon_lst.append(player_icon)
                Board.draw_icon(icon_lst, x_lst, y_lst)
                shadow_lst.remove(Board.square_shadow_3)
                line_1_lst.append(player_icon)
                column_3_lst.append(player_icon)
                dig_2_lst.append(player_icon)
                r -= 1
            if random_shadow == Board.square_shadow_4 and Board.square_shadow_4 in shadow_lst:
                x_lst.append(Board.square_shadow_4.x)
                y_lst.append(Board.square_shadow_4.y)
                icon_lst.append(player_icon)
                Board.draw_icon(icon_lst, x_lst, y_lst)
                shadow_lst.remove(Board.square_shadow_4)
                line_2_lst.append(player_icon)
                column_1_lst.append(player_icon)
                r -= 1
            if random_shadow == Board.square_shadow_5 and Board.square_shadow_5 in shadow_lst:
                x_lst.append(Board.square_shadow_5.x)
                y_lst.append(Board.square_shadow_5.y)
                icon_lst.append(player_icon)
                Board.draw_icon(icon_lst, x_lst, y_lst)
                shadow_lst.remove(Board.square_shadow_5)
                line_2_lst.append(player_icon)
                column_2_lst.append(player_icon)
                dig_1_lst.append(player_icon)
                dig_2_lst.append(player_icon)
                r -= 1
            if random_shadow == Board.square_shadow_6 and Board.square_shadow_6 in shadow_lst:
                x_lst.append(Board.square_shadow_6.x)
                y_lst.append(Board.square_shadow_6.y)
                icon_lst.append(player_icon)
                Board.draw_icon(icon_lst, x_lst, y_lst)
                shadow_lst.remove(Board.square_shadow_6)
                line_2_lst.append(player_icon)
                column_3_lst.append(player_icon)
                r -= 1
            if random_shadow == Board.square_shadow_7 and Board.square_shadow_7 in shadow_lst:
                x_lst.append(Board.square_shadow_7.x)
                y_lst.append(Board.square_shadow_7.y)
                icon_lst.append(player_icon)
                Board.draw_icon(icon_lst, x_lst, y_lst)
                shadow_lst.remove(Board.square_shadow_7)
                line_3_lst.append(player_icon)
                column_1_lst.append(player_icon)
                dig_2_lst.append(player_icon)
                r -= 1
            if random_shadow == Board.square_shadow_8 and Board.square_shadow_8 in shadow_lst:
                x_lst.append(Board.square_shadow_8.x)
                y_lst.append(Board.square_shadow_8.y)
                icon_lst.append(player_icon)
                Board.draw_icon(icon_lst, x_lst, y_lst)
                shadow_lst.remove(Board.square_shadow_8)
                line_3_lst.append(player_icon)
                column_2_lst.append(player_icon)
                r -= 1
            if random_shadow == Board.square_shadow_9 and Board.square_shadow_9 in shadow_lst:
                x_lst.append(Board.square_shadow_9.x)
                y_lst.append(Board.square_shadow_9.y)
                icon_lst.append(player_icon)
                Board.draw_icon(icon_lst, x_lst, y_lst)
                shadow_lst.remove(Board.square_shadow_9)
                line_3_lst.append(player_icon)
                column_3_lst.append(player_icon)
                dig_1_lst.append(player_icon)
                r -= 1
            if r < 5:
                lst_lst = [line_1_lst, line_2_lst, line_3_lst, column_1_lst, column_2_lst, column_3_lst, dig_1_lst, dig_2_lst]
                if self.check_list(lst_lst):
                    self.result('you win')
            if r == 0:
                self.result('draw')
            pygame.display.update()
            clock.tick(10)

    def queueu(self):
        pygame.init()
        myfont = pygame.font.Font('fonts/YoungSerif-Regular.ttf', 50)
        text = myfont.render('your choice', True, 'Red')
        text2 = myfont.render('my choice', True, 'Red')
        icon_lst = [self.icon_rosk, self.icon_s, self.icon_p]
        self.draw_fone()
        pygame.display.update()
        player_choice = None
        r = True
        while r:
            mouse = pygame.mouse.get_pos()
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    if self.rock_shadow.collidepoint(mouse):
                        player_choice = self.icon_rosk
                        icon_lst.remove(self.icon_rosk)
                    if self.s_shadow.collidepoint(mouse):
                        player_choice = self.icon_s
                        icon_lst.remove(self.icon_s)
                    if self.p_shadow.collidepoint(mouse):
                        player_choice = self.icon_p
                        icon_lst.remove(self.icon_p)
                if event.type == pygame.QUIT:
                    pygame.quit()
                    r = False
            if player_choice:
                self.screen.blit(self.backfone, (0, 0))
                self.screen.blit(text, (70, 250))
                self.screen.blit(player_choice, (130, 330))
                self.screen.blit(text2, (400, 250))
                random_choice = random.choice(icon_lst)
                self.screen.blit(random_choice, (530, 330))
                pygame.display.update()
                pygame.time.delay(3000)
                if player_choice == self.icon_rosk:
                    if random_choice == self.icon_s:
                        self.who_going('first')
                        pygame.display.update()
                        pygame.time.delay(3000)
                        return True
                    else:
                        self.who_going('second')
                        pygame.display.update()
                        pygame.time.delay(3000)
                        return False
                if player_choice == self.icon_s:
                    if random_choice == self.icon_p:
                        self.who_going('first')
                        pygame.display.update()
                        pygame.time.delay(3000)
                        return True
                    else:
                        self.who_going('second')
                        pygame.display.update()
                        pygame.time.delay(3000)
                        return False
                if player_choice == self.icon_p:
                    if random_choice == self.icon_rosk:
                        self.who_going('first')
                        pygame.display.update()
                        pygame.time.delay(3000)
                        return True
                    else:
                        self.who_going('second')
                        pygame.display.update()
                        pygame.time.delay(3000)
                        return False

    def queueu_2(self):
        lst = ['player 1', 'player 2']
        number = random.choice(lst)
        pygame.init()
        self.screen.blit(self.backfone, (0, 0))
        myfont = pygame.font.Font('fonts/YoungSerif-Regular.ttf', 60)
        text = myfont.render(f'{number} is going first', True, 'Red')
        self.screen.blit(text, (60, 300))
        pygame.display.update()
        pygame.time.delay(2000)
        if number == 'player 1':
            return True
        else:
            return False

    def who_going(self, number):
        pygame.init()
        self.screen.blit(self.backfone, (0, 0))
        myfont = pygame.font.Font('fonts/YoungSerif-Regular.ttf', 60)
        text = myfont.render(f'you are going {number}', True, 'Red')
        self.screen.blit(text, (60, 300))

    def player_isgoing(self, number):
        pygame.init()
        myfont = pygame.font.Font('fonts/YoungSerif-Regular.ttf', 160)
        text = myfont.render(number, True, 'Red')
        text.set_alpha(5)
        self.screen.blit(text, (10, 170))
        pygame.display.update()

    def check_list(self, lst):

        for el in lst:
            if len(el) == 3:
                if self.check_lst2(el):
                    return True

        return False
    def check_lst2(self, lst):

        for i in range(len(lst)):
            if lst[0] != lst[1]:
                return False
            elif lst[0] == lst[2]:
                return True
            else:
                return False

    def result(self, result):
        pygame.init()
        myfont = pygame.font.Font('fonts/YoungSerif-Regular.ttf', 130)
        text = myfont.render(result, True, 'Red')
        self.screen.blit(text, (90, 50))
        text2 = myfont.render('try again?', True, 'Red')
        text_yes = myfont.render('yes', True, 'Blue')
        text_no = myfont.render('no', True, 'Blue')
        shadow_text_yes = text_yes.get_rect(topleft=(50, 470))
        shadow_text_no = text_no.get_rect(topleft=(500, 470))
        self.screen.blit(text2, (15, 250))
        self.screen.blit(text_yes, shadow_text_yes)
        self.screen.blit(text_no, shadow_text_no)
        pygame.display.update()
        r = True
        while r:
            mouse = pygame.mouse.get_pos()
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    if shadow_text_yes.collidepoint(mouse):
                        self.create_game()
                    if shadow_text_no.collidepoint(mouse):
                        pygame.quit()
                        r = False
                if event.type == pygame.QUIT:
                    pygame.quit()
                    r = False
