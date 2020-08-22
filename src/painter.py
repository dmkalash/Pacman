# -*- coding: utf-8 -*-
import pygame
from vector import Vector


class Painter():
    surface = None

    @staticmethod
    def init(surface):
        Painter.surface = surface

    @staticmethod
    def draw(*args):
        """Draw object
        Attributes:

            """
        if len(args) == 1:
            image, rect = args[0]
        elif len(args) == 2:
            image, rect = args[0], args[1]
        else:
            image = None
            rect = None
        rect -= Vector(image.get_rect().size) / 2
        Painter.surface.blit(image, rect.get())

    @staticmethod
    def fill_screen(color=pygame.Color('black')):
        # type: (pygame.Color) -> None
        """Fill screen with color"""
        Painter.surface.fill(color)
