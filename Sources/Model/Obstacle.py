from Observable import Observable


class Obstacle:
    def __init__(self, idx, x, y, w, h):
        self.myPos = Observable(0)
        self.idx = idx
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.speed = 5

    def set_pos(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.myPos.set((self.idx, self.x, self.y, self.w, self.h))

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
        self.myPos.set((self.x, self.y, self.w, self.h))
