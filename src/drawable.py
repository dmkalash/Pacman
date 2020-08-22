# -*- coding: utf-8 -*-
from vector import Vector
from painter import Painter


class Drawable(object):
    """Represents object that can be drawn by Painter class"""

    def __init__(self, position=None, image=None):
        """
        :type position: Vector
        :type image: pygame.Surface
        """
        if position == None:
            position = Vector()
        self.position = position
        self.image = image

    def set_position(self, position):
        # type: (Vector) -> None
        """Set position vector"""
        self.position = position.floor()

    def get_position(self):
        # type: () -> Vector
        """Return position vector"""
        return self.position

    def set_image(self, image):
        # type: (pygame.surface) -> None
        """Set image
        :type image: pygame.surface"""
        self.image = image

    def get_image(self):
        # type: () -> pygame.surface
        """Return image"""
        return self.image

    def get_size(self):
        # type: () -> Vector
        """Return size vector of image"""
        return Vector(self.image.get_rect().size)

    def get_image_rect(self):
        # type: () -> (Image, Vector)
        """Return image and tuple of x and y positions"""
        return self.image, self.position

    def draw(self):
        # type: () -> None
        Painter.draw(self.get_image_rect())
