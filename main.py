import pygame

pygame.init()

screen = pygame.display.set_mode((1000, 700)) # моё окно. его размер
pygame.display.set_caption("tic tac toe")
pygame.display.set_icon(pygame.image.load("pictures/icon.png"))
square = pygame.Surface((200, 300))
square.fill('Green')

vixod = True
while vixod:
    screen.fill('White')
    screen.blit(square, (100,100))
    pygame.display.update()
    pygame.draw.circle(square, 'Blue', (100, 100), 50)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            vixod = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                screen.fill((237, 7, 19))

