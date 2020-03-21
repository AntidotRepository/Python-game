from Observable import Observable


class Car:
    def __init__(self, w, h):
        self.myPos = Observable(0)
        self.x = 0
        self.y = 0
        self.w = w
        self.h = h
        self.speed = 5

    def set_pos(self, x, y):
        self.x = x
        self.y = y
        self.myPos.set((self.x, self.y))

    def move(self, x, y, minX, maxX, minY, maxY):
        self.x += self.speed * x
        if self.x < minX:
            self.x = minX
        if self.x > (maxX - self.w):
            self.x = maxX - self.w
        self.y += self.speed * y
        if self.y < minY:
            self.y = minY
        if self.y > (maxY - self.h):
            self.y = (maxY - self.h)
        self.myPos.set((self.x, self.y))
