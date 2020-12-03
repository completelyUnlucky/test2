import pygame
pygame.init()

class Krug:
    def __init__(self):
        self.direction = 0
        self.x = 250
        self.y = 250
        self.h = 1
        self.speed = 15
        # self.timer.setInterval(20)
        # self.timer =


    def show(self, screen):
        pygame.draw.circle(screen, (0, 200, 0), (self.x, self.y), 40)


class Screen:
    def __init__(self):
        self.screen = pygame.display.set_mode([500, 500])
        self.krug = Krug()


    def show(self):
        self.screen.fill((235, 190, 255))
        self.krug.show(self.screen)

sc = Screen()
running = True
while running:
        for i in pygame.event.get():
            if i.type == pygame.QUIT:
                exit()
            if i.type == pygame.KEYDOWN:
                if i.key == pygame.K_LEFT:
                    sc.krug.x -= 10
                if i.key == pygame.K_RIGHT:
                    sc.krug.x += 10
                if i.key == pygame.K_DOWN:
                    sc.krug.y += 10
                if i.key == pygame.K_UP:
                    sc.krug.y -= 10
        sc.show()

        pygame.display.flip()


pygame.quit()