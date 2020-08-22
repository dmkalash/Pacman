# -*- coding: utf-8 -*-
import pygame
from painter import Painter
from game import Game
from tab import MainMenu
from input import Input


class PygameWrapper(object):
    """Wrapper class for pygame"""

    def __init__(self):
        pygame.init()
        self.exit = False
        self.framerate = 60
        self.delta_time = 0
        self.clock = pygame.time.Clock()
        self.main_menu = MainMenu(self)
        self.game = Game(self)
        self.current_tab = self.game
        self.screen = pygame.display.set_mode(
            self.current_tab.get_size().floor().get())
        Painter.init(self.screen)

    def start(self):
        """start main loop"""
        while not Input.exit:
            self.screen = pygame.display.set_mode(
                self.current_tab.get_size().floor().get())
            Painter.fill_screen()
            self.delta_time = self.clock.tick(self.framerate) / 1000.0
            Input.update()
            self.current_tab.update()
            self.current_tab.draw()
            pygame.display.update()

    def set_current_tab(self, tab):
        pass
