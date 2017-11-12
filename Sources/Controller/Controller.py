# !/usr/bin/python2.7
# -*- coding: utf-8 -*-
from View.GameView import GameView


class Controller:
    test = None

    def __init__(self):
        self.test = "Hello"
        GV = GameView()

    def func(self):
        print self.test
