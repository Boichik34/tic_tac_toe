import pygame


class Board:

    def create_window(self):
        pygame.init()
        clock = pygame.time.Clock()
        backfone = pygame.image.load('pictures/peakpx (2).jpg')
        screen = pygame.display.set_mode((700, 700))  # моё окно. его размер
        pygame.display.set_caption("tic tac toe")  # устанавливаем название
        pygame.display.set_icon(pygame.image.load("pictures/icon.png"))  # устанавливаем икону(подгрузка изоброжения)
        myfont = pygame.font.Font('fonts/YoungSerif-Regular.ttf', 50)  # добавляем шрифт
        text = myfont.render('one player', True, ('Red'))
        text_2 = myfont.render('two player', True, ('Red'))
        text_3 = myfont.render('wwwww', True, ('Red'))
        text_shadow = text.get_rect(topleft=(200, 20))
        text_shadow_2 = text_2.get_rect(topleft=(200, 600))

        nevixod = True
        while nevixod:
            screen.blit(backfone, (0, 0))  # создаем в окне фигуру "square"
            screen.blit(text, text_shadow)
            screen.blit(text_2, text_shadow_2)
            mouse = pygame.mouse.get_pos()
            if text_shadow.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
                screen.blit(text_3, (200, 300))

            pygame.display.update()  # обновляем окно
            for event in pygame.event.get():  # проверяет на событие
                if event.type == pygame.QUIT:  # если событие = выход
                    pygame.quit()  # выход
                    nevixod = False



a = Board
a.create_window(a)