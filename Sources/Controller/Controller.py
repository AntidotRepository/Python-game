# !/usr/bin/python3.7
# -*- coding: utf-8 -*-

from Model.Car import Car
from Model.Obstacle import Obstacle
from View.View import View
# from View.View import ChangerWidget
import pygame
import random


WIN_WIDTH = 750
WIN_HEIGHT = 400

CAR_WIDTH = 73
CAR_HEIGHT = 73


class Controller:
    def __init__(self):
        print("Create controller")
        self.car = Car(CAR_WIDTH, CAR_HEIGHT)
        self.car.myPos.addCallback(self.carPosChanged)
        self.obstacles = list()
        self.view1 = View(WIN_WIDTH, WIN_HEIGHT)
        for i in range(0, 4):
            posX = random.randrange(0, WIN_WIDTH)
            posY = 0
            width = random.randrange(40, 200)
            height = random.randrange(40, 200)
            obs = Obstacle(i, posX, posY, width, height)
            self.view1.add_obstacle(posX, posY, width, height)
            obs.myPos.addCallback(self.obsPosChanged)
            obs.set_pos(posX, posY, width, height)
            self.obstacles.append(obs)

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
                    if event.key == pygame.K_ESCAPE:
                        crashed = True

                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT or \
                            event.key == pygame.K_RIGHT:
                        x_change = 0

            for an_obs in self.obstacles:
                an_obs.move(0, 1, 0, WIN_WIDTH, 0, 1000)
            self.car.move(x_change, 0, 0, WIN_WIDTH, 0, WIN_HEIGHT)
            self.view1.update()

        pygame.quit()
        quit()

    def carPosChanged(self, posXY):
        self.view1.setCarPos(posXY[0], posXY[1])

    def obsPosChanged(self, xywh):
        self.view1.setObsPos(xywh[0], xywh[1], xywh[2], xywh[3], xywh[4])
