# -*- coding: utf-8 -*-
from drawable import Drawable
from vector import Vector
from image import Image


class Cell(Drawable):
    """Class that represents a cell on the field"""
    path_to_images = ''

    def __init__(self, type='0', position=Vector(), image=None):
        super(Cell, self).__init__(position=position, image=image)
        self.type = type

    def get_type(self):
        # type: () -> str
        """Return cell type"""
        return self.type

    def set_type(self, type):
        # type: (str) -> None
        """"Set cell type"""
        self.type = str(type)
        path = Cell.path_to_images
        if self.type in ['p', 'g', 't']:
            path = '0.gif'
        else:
            path += self.type + '.gif'
        self.image = Image.get(path)

    def is_passable(self):
        # type: () -> bool
        """"Return if cell is passable"""
        return self.type not in ['w']
