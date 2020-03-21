from Observable import Observable


class Car:
    def __init__(self):
        self.myPos = Observable(0)
        self.posX = 0
        self.posY = 0
        self.speed = 5

    def set_pos(self, x, y):
        self.posX = x
        self.posY = y
        self.myPos.set((self.posX, self.posY))

    def move(self, x, y):
        self.posX += self.speed * x
        self.posY += self.speed * y
        self.myPos.set((self.posX, self.posY))
