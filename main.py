import pygame
import game

game = game.Game()
def main():
    global CLOCK
    global SCREEN



    while True:
        game.create_game()

    # pygame.init()
    # pygame.init()
    # CLOCK = pygame.time.Clock()
    # backfone = pygame.image.load('pictures/peakpx (2).jpg')
    # SCREEN = pygame.display.set_mode((700, 700))  # моё окно. его размер
    # pygame.display.set_caption("tic tac toe")  # устанавливаем название
    # pygame.display.set_icon(pygame.image.load("pictures/icon.png"))  # устанавливаем икону(подгрузка изоброжения)
    # myfont = pygame.font.Font('fonts/YoungSerif-Regular.ttf', 49)  # добавляем шрифт

#while nevixod:

    # screen.blit(backfone, (0, 0))  # создаем в окне фигуру "square"
    # # pygame.draw.circle(square, 'Blue', (100, 100), 50)  # рисуем круг(где, цвет, расположение, размер)
    # # screen.blit(text, [x, y])  # рисуем тексе
    # # square.blit(picture, [50,40]) # рисуем картинку в square
    # # x += 1
    # # y += 1
    # # if y == 700:
    # #     x = 0
    # #     y = 0
    #
    # pygame.display.update()   # обновляем окно
    # for event in pygame.event.get(): # проверяет на событие
    #     if event.type == pygame.QUIT: # если событие = выход
    #         pygame.quit()              # выход
    #         nevixod = False
    #     elif event.type == pygame.KEYDOWN:  # проверяет на событие нажатие кнопки
    #         if event.key == pygame.K_a:      # на нажатие а
    #             screen.fill((237, 7, 19))    # окрашиваем в другой цвет

    #clock.tick(100)


if __name__ == '__main__':
    main()