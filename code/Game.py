#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame

from Const import WIN_HEIGTH, WIN_WIDTH
from code.Menu import Menu


class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(WIN_WIDTH, WIN_HEIGTH))

    def run(self):
        while True:
            menu = Menu(self.window)
            menu.run()
            pass


