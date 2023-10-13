import pygame

pygame.init()
clock = pygame.time.Clock()
backfone = pygame.image.load('pictures/peakpx (2).jpg')
screen = pygame.display.set_mode((700, 700))  # моё окно. его размер
pygame.display.set_caption("tic tac toe")  # устанавливаем название
pygame.display.set_icon(pygame.image.load("pictures/icon.png"))  # устанавливаем икону(подгрузка изоброжения)
myfont = pygame.font.Font('fonts/YoungSerif-Regular.ttf', 49)  # добавляем шрифт
# text = myfont.render('tic tac toe', False, 'Red')  # создаем текст
#picture = pygame.image.load('pictures/icons8-кнопка-с-крестиком-96.png') # создаем картинку


nevixod = True
while nevixod:

    screen.blit(backfone, (0, 0))  # создаем в окне фигуру "square"
    # pygame.draw.circle(square, 'Blue', (100, 100), 50)  # рисуем круг(где, цвет, расположение, размер)
    # screen.blit(text, [x, y])  # рисуем тексе
    # square.blit(picture, [50,40]) # рисуем картинку в square
    # x += 1
    # y += 1
    # if y == 700:
    #     x = 0
    #     y = 0

    pygame.display.update()   # обновляем окно
    for event in pygame.event.get(): # проверяет на событие
        if event.type == pygame.QUIT: # если событие = выход
            pygame.quit()              # выход
            nevixod = False
        elif event.type == pygame.KEYDOWN:  # проверяет на событие нажатие кнопки
            if event.key == pygame.K_a:      # на нажатие а
                screen.fill((237, 7, 19))    # окрашиваем в другой цвет

    #clock.tick(100)