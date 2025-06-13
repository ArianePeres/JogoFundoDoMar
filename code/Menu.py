#!/usr/bin/python
# -*- coding: utf-8 -*-
from operator import truediv

import pygame.image
from pygame.font import Font
from pygame.rect import Rect
from pygame.surface import Surface

from Const import WIN_WIDTH, COLOR_PINK, MENU_OPTION, COLOR_SALMON


def convert_alpha():
    pass


class Menu:
    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load('./asset/orig.png')
        self.rect = self.surf.get_rect(left=0, top=0)

    def run(self, ):
        pygame.mixer_music.load('./asset/menu.wav')
        pygame.mixer_music.play(-1)
        while True:
            self.window.blit(source=self.surf, dest=self.rect)
            self.menu_text(50, "AVENTURA", COLOR_PINK, ((WIN_WIDTH / 2), 70))
            self.menu_text(50, "SUBMARINA", COLOR_PINK, ((WIN_WIDTH / 2), 120))

            for i in range(len(MENU_OPTION)):
                self.menu_text(20, MENU_OPTION[i], COLOR_SALMON, ((WIN_WIDTH / 2), 200 + 25 * i))

            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()  # fecha janela
                    quit()  # encerra a inicialização do pygame

    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)
