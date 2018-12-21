import Tkinter as tk

WIN_WIDTH = 750
WIN_HEIGHT = 400


class View(tk.Toplevel):
    def __init__(self, master):
        tk.Toplevel.__init__(self, master)
        self.protocol('WM_DELETE_WINDOW', self.master.destroy)
        self.can = tk.Canvas(self,
                             width=WIN_WIDTH,
                             height=WIN_HEIGHT)
        self.can.pack()

    def drawBuddy(self, data):
        for elem in data:
            self.can.create_line(elem.pt1[0] * 50, elem.pt1[1] * 50, elem.pt2[0] * 50, elem.pt2[1] * 50)
            self.can.update()
        # self.can.create_arc(WIN_WIDTH / 2, WIN_HEIGHT / 2, 0, 0,
        #                     width="10", extent=30)
        self.can.update()
