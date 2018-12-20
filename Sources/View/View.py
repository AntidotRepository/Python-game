import Tkinter as tk


class View(tk.Toplevel):
    def __init__(self, master):
        tk.Toplevel.__init__(self, master)
        self.protocol('WM_DELETE_WINDOW', self.master.destroy)
        can = tk.Canvas(self,
                        width=250,
                        height=140)
        can.create_line(125, 70, 0, 0, fill="black", width="10")
        can.pack()
