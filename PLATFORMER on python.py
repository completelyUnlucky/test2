import pygame
pygame.init()

WIDTH = 1000
HEIGHT = 800
speed = 100
x = 500
y = 400



sc = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('ну шо дядь Толик, будем стричься???')

bg = pygame.image.load('травка.png')
hero = pygame.image.load('Валера.png')

pygame.display.update()

run = True
while(run):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    press = pygame.key.get_pressed()
         if press[pygame.K_LEFT]:
            x -= speed
        elif press[pygame.K_RIGHT]:
            x += speed

    sc.blit(bg, (0, 0))
    sc.blit(hero, (x, y))
    pygame.display.update()

pygame.quit()
#
# rect_x = 50
# rect_y = 50
#
# # -------- Основной цикл программы -----------
# while done == False:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             done = True
#
#     screen.fill(black)
#
#     # Нарисовать прямоугольник
#     pygame.draw.rect(screen, white, [rect_x, rect_y, 50, 50])
#
#     # Подвинуть начальную точку прямоугольника
#     rect_x += 5
#     rect_y += 5
