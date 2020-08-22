# -*- coding: utf-8 -*-
from field import Field
from tab import Tab
from file_manager import FileManager
from moving_unit import Units
from input import Input


class Game(Tab):
    """Tab class that represents logic of a game"""

    def __init__(self, wrapper):
        super(Game, self).__init__(wrapper=wrapper,
                                   background_image=FileManager.get_image_main_menu_background())
        self.score = 0
        self.level = 0
        self.lives = 3
        self.txt_info = "SCORE: {score}   LEVEL: {level}   LIVES: {lives}"
        self.field = Field()
        self.units = Units(self)
        self.next_level()

    def add_score(self, value):
        # type: (int) -> int
        self.score += int(value)
        return self.score

    def next_level(self):
        # type: () -> None
        """Switch to next level"""
        self.level += 1
        self.field.parse(str(self.level) + '_lvl.txt')
        self.units.add_pacman(self.field.get_pacman_spawn())
        self.units.add_blinky(self.field.get_ghosts_spawn())
        self.units.add_pinky(self.field.get_ghosts_spawn())
        self.units.add_inky(self.field.get_ghosts_spawn())
        self.units.add_clyde(self.field.get_ghosts_spawn())

    def get_size(self):
        # type: () -> Vector
        """Return size vector of tab"""
        return self.field.get_size().to_abs()

    def update(self):
        # type: () -> None
        """Update the objects"""
        self.units.pacman.set_direction(Input.key_direction)
        for obj in self.units.get_all():
            obj.move()

    def draw(self):
        # type: () -> None
        """Draw all objects"""
        self.field.draw()
        self.units.draw()
