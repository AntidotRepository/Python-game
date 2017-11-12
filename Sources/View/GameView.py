from Tkinter import *


class GameView:
    can = None
    HEIGHT = 480
    WIDTH = 640
    fen = None

    def draw_circle(x, y, r, color='black'):
        can.create_oval(x - r, y - r, x + r, y + r, outline=color)

    def __init__(self):
        self.fen = Tk()
        self.can = Canvas(self.fen, width=self.WIDTH,
                          height=self.HEIGHT, bg='white')
        self.can.pack(side=TOP)
        self.fen.mainloop()
        pass
