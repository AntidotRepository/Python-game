# !/usr/bin/python2.7
# -*- coding: utf-8 -*-
from Controller.Controller import Controller
import Tkinter as tk

if __name__ == '__main__':
    root = tk.Tk()
    root.withdraw()
    app = Controller(root)
    root.mainloop()
