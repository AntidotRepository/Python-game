# !/usr/bin/python3.7
# -*- coding: utf-8 -*-

from Model.Car import Car
from View.View import View
# from View.View import ChangerWidget
import pygame


WIN_WIDTH = 750
WIN_HEIGHT = 400

CAR_WIDTH = 73
CAR_HEIGHT = 73


class Controller:
    def __init__(self):
        print("Create controller")
        self.car = Car(CAR_WIDTH, CAR_HEIGHT)
        self.car.myPos.addCallback(self.carPosChanged)
        self.view1 = View(WIN_WIDTH, WIN_HEIGHT)

        self.car.set_pos(WIN_WIDTH / 2, WIN_HEIGHT * 0.7)
        crashed = False
        x_change = 0

        while not crashed:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    crashed = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        x_change = -1
                    if event.key == pygame.K_RIGHT:
                        x_change = 1

                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT or \
                            event.key == pygame.K_RIGHT:
                        x_change = 0

            self.car.move(x_change, 0, 0, WIN_WIDTH, 0, WIN_HEIGHT)
            self.view1.update()

        pygame.quit()
        quit()

    def carPosChanged(self, posXY):
        self.view1.setCarPos(posXY[0], posXY[1])
