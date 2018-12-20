# !/usr/bin/python2.7
# -*- coding: utf-8 -*-
# from View.GameView import GameView


# class Controller:
#     test = None

#     def __init__(self):
#         self.test = "Hello"
#         GV = GameView()

#     def func(self):
#         print self.test

##Some points to mention...
##
##The model knows nothing about the view or the controller.
##The view knows nothing about the controller or the model.
##The controller understands both the model and the view.
##
##The model uses observables, essentially when important data is changed,
##any interested listener gets notified through a callback mechanism.
##
##The following opens up two windows, one that reports how much money you
##have, and one that has two buttons, one to add money and one to remove
##money.
##
##The important thing is that the controller is set up to monitor changes
##in the model.  In this case the controller notices that you clicked a
##button and modifies the money in the model which then sends out a
##message that it has changed.  The controller notices this and updates
##the widgets.
##
##The cool thing is that anything modifying the model will notify the
##controller.  In this case it is the controller modifying the model, but it
##could be anything else, even another controller off in the distance
##looking at something else.
##
##The main idea is that you give a controller the model and view that it
##needs, but the model's can be shared between controllers so that when
##the model is updated, all associated views are updated. -Brian Kelley
##
## following is a Tkinter approximation of the original example.

from Model.Model import Model
from View.View import View
# from View.View import ChangerWidget


class Controller:
    def __init__(self, root):
        self.model = Model()
    #    self.model.myMoney.addCallback(self.MoneyChanged)
        self.view1 = View(root)
        # self.view2 = ChangerWidget(self.view1)
        # self.view2.addButton.config(command=self.AddMoney)
        # self.view2.removeButton.config(command=self.RemoveMoney)
    #    self.MoneyChanged(self.model.myMoney.get())

    # def AddMoney(self):
    #     self.model.addMoney(10)

    # def RemoveMoney(self):
    #     self.model.removeMoney(10)

    # def MoneyChanged(self, money):
    #     self.view1.SetMoney(money)
