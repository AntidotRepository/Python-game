import pygame


class View():
    def __init__(self, view_width, view_height):
        print("Create View")
        pygame.init()
        self.carX = 0
        self.carY = 0

        self.gameDisplay = pygame.display.set_mode((view_width, view_height))
        pygame.display.set_caption('Learn AI')
        self.clock = pygame.time.Clock()
        self.carImg = pygame.image.load('racecar.png')
        self.setTimer("00:00:00")

    def setCarPos(self, x, y):
        self.carX = x
        self.carY = y

    def setTimer(self, string):
        black = (0, 0, 0)
        font = pygame.font.Font('freesansbold.ttf', 30)
        self.timerSurf = font.render(string, True, black)
        self.timerRect = self.timerSurf.get_rect()
        self.timerRect.topleft = (10, 10)

    def update(self):
        white = (255, 255, 255)
        self.gameDisplay.fill(white)
        self.gameDisplay.blit(self.carImg, (self.carX, self.carY))
        self.gameDisplay.blit(self.timerSurf, self.timerRect)
        pygame.display.update()
        self.clock.tick(60)
