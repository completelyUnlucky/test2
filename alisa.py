import pygame, sys
from pygame.locals import *
import time
pygame.init()

screen = pygame.display.set_mode([1280, 720])

image = pygame.image.load('anime.jpg')

TextSettings1 = pygame.font.Font(None, 36)

noTXT = TextSettings1.render('', True, (255, 255, 255))

plotText1 = TextSettings1.render('', True, (255, 255, 255))

plotText2 = TextSettings1.render('', True, (255, 255, 255))

plotText3 = TextSettings1.render('', True, (255, 255, 255))

plotText4 = TextSettings1.render('', True, (255, 255, 255))

plotText5 = TextSettings1.render('Но проснувшись он подумал что устал от такой жизни, он захотел совершить суицид. ', True, (255, 255, 255))

plotText6 = TextSettings1.render('Мысли об этом у него появились давно, но сейчас он уже стоял на краю крыши своего дома. (нажмите 1)', True, (255, 255, 255))

plotTextEnd = TextSettings1.render('ВСЕ! ИГРА КОНЧИЛАСЬ, ОБЯЗАТЕЛЬНО ОЦЕНИТЕ ЕЁ!!!', True, (255, 255, 255))

text1 = TextSettings1.render('он не пойдет в школу (нажми 1 для выбора этого варианта)', True, (255, 255, 255))

text2 = TextSettings1.render('он пойдет в школу (нажми 2 для выбора этого варианта)', True, (255, 255, 255))

text3 = TextSettings1.render('', True, (255, 255, 255))

text4 = TextSettings1.render('', True, (255, 255, 255))
 
# text5 = TextSettings1.render('', True, (255, 255, 255))
#
# text6 = TextSettings1.render('', True, (255, 255, 255))
#
# text7 = TextSettings1.render('', True, (255, 255, 255))
#
# text8 = TextSettings1.render('', True, (255, 255, 255))

# plot_arr  = []
# line = ' '
# plot = open('plot')
#
# while True:
#     tmp = plot.readline()
#     if len(tmp) > 1:
#         line += tmp
#     else:
#         if tmp:
#             plot_arr.append(line)
#             line = ''
#         else:
#             break

# print(*plot_arr)

pygame.display.update()

next_press = False
running = True
while running:
    screen.blit(image, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    key_press = pygame.key.get_pressed()
    if key_press[pygame.K_1]:
        text1 = text3
        plotText1 = plotText3
        pygame.display.flip()
    screen.blit(plotText1, (50, 100))
    screen.blit(text1, (50, 550))
    screen.blit(text2, (50, 600))
    pygame.display.flip()




    if key_press[pygame.K_2]:
        text2 = text4
        plotText1 = plotText3
        pygame.display.flip()
        screen.blit(text3, (50, 550))
        screen.blit(text4, (50, 600))
    pygame.display.flip()

pygame.display.flip()
pygame.quit()

