from Observable import Observable


class Car:
    def __init__(self, width, height):
        self.myPos = Observable(0)
        self.posX = 0
        self.posY = 0
        self.width = width
        self.height = height
        self.speed = 5

    def set_pos(self, x, y):
        self.posX = x
        self.posY = y
        self.myPos.set((self.posX, self.posY))

    def move(self, x, y, minX, maxX, minY, maxY):
        self.posX += self.speed * x
        if self.posX < minX:
            self.posX = minX
        if self.posX > (maxX - self.width):
            self.posX = maxX - self.width
        self.posY += self.speed * y
        if self.posY < minY:
            self.posY = minY
        if self.posY > (maxY - self.height):
            self.posY = (maxY - self.height)
        self.myPos.set((self.posX, self.posY))
