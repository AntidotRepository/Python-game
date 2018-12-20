import Tkinter as tk

WIN_WIDTH = 750
WIN_HEIGHT = 400


class View(tk.Toplevel):
    def __init__(self, master):
        tk.Toplevel.__init__(self, master)
        self.protocol('WM_DELETE_WINDOW', self.master.destroy)
        can = tk.Canvas(self,
                        width=WIN_WIDTH,
                        height=WIN_HEIGHT)
        can.create_arc(WIN_WIDTH / 2, WIN_HEIGHT / 2, 0, 0,
                       width="10", extent=30)
        can.pack()
