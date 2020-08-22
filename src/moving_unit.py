# -*- coding: utf-8 -*-
from drawable import Drawable
from vector import (Vector, Direction)
from image import Image


class MovingUnit(Drawable):
    def __init__(self, game, spawn_cell=None):
        if spawn_cell == None:
            spawn_cell = Vector()
        super(MovingUnit, self).__init__(
            position=spawn_cell.to_abs().cell_center())
        self.spawn_cell = spawn_cell
        self.speed = 200
        self.game = game
        self.buffer_position = self.position
        self.buffer_direction = Direction.ZERO
        self.direction = Direction.ZERO

    def set_speed(self, speed):
        """Set speed of unit"""
        self.speed = speed

    def get_speed(self):
        """Return speed of unit"""
        return self.speed

    def move(self):
        """Move unit towards its direction or changing direction"""
        if self.buffer_direction != Direction.ZERO:
            if self.buffer_direction != self.direction and self.game.field.get_cell(
                            self.position.to_rel() + self.buffer_direction).is_passable():
                if self.buffer_direction == -self.direction:
                    self.direction = self.buffer_direction
                elif (self.direction in [Direction.DOWN,
                                         Direction.RIGHT] and self.buffer_position <= self.position.cell_center() <= self.position) or (
                                self.direction in [Direction.UP,
                                                   Direction.LEFT] and self.position <= self.position.cell_center() <= self.buffer_position) or self.direction == Direction.ZERO:
                    self.direction = self.buffer_direction
                    self.position = self.position.cell_center()
            if self.game.field.get_cell(
                            self.position.to_rel() + self.direction).is_passable():
                self.set_position(
                    self.position + self.direction * self.speed *
                    self.game.wrapper.delta_time)
            else:
                if self.direction in [Direction.UP, Direction.LEFT]:
                    self.set_position(max(self.position.cell_center(),
                                          self.position + self.direction * self.speed * self.game.wrapper.delta_time))
                if self.direction in [Direction.DOWN, Direction.RIGHT]:
                    self.set_position(min(self.position.cell_center(),
                                          self.position + self.direction * self.speed * self.game.wrapper.delta_time))

    def get_direction(self):
        """Return direction of unit"""
        return self.direction

    def set_direction(self, buffer_direction):
        """Set direction of unit"""
        if buffer_direction != self.buffer_direction:
            self.buffer_direction = buffer_direction
            self.buffer_position = self.position
            # + image change

    def set_spawn_cell(self, vector):
        self.spawn_cell = vector
        super(MovingUnit, self).set_position(self.spawn_cell.to_abs().cell_center())


class Pacman(MovingUnit):
    def __init__(self, game, spawn_cell=None):
        if spawn_cell == None:
            spawn_cell = Vector()
        super(Pacman, self).__init__(game=game, spawn_cell=spawn_cell)
        self.image = Image.get('../resrc/pacman/Big_Pacman_Up.gif')

    def move(self):
        # self.image=Image.get('../resrc/') #set image
        cur_cell = self.game.field.get_cell(self.position.to_rel())
        if cur_cell.get_type() == 's':
            self.game.add_score(10)
            self.game.field.get_cell(self.position.to_rel()).set_type('0')
            # self.game.field.
        elif cur_cell.get_type() == 'e':
            self.game.add_score(50)
            self.game.field.get_cell(self.position.to_rel()).set_type('0')

        super(Pacman, self).move()


class Ghost(MovingUnit):
    def __init__(self, game, spawn_cell=None):
        if spawn_cell == None:
            spawn_cell = Vector()
        super(Ghost, self).__init__(game=game, spawn_cell=spawn_cell)
        self.destination = Vector()
        self.set_random_direction()
        self.status = 0

    def move(self):
        dirs = self.game.field.get_cell_directions(self.position.to_rel())
        if len(dirs) == 1:
            self.set_direction(dirs[0])
        elif len(dirs) == 2:
            self.set_direction(dirs[0] if dirs[1] == -self.direction else dirs[1])
        elif len(dirs) > 2:
            min_dist = (self.position.to_rel() + dirs[0] - self.game.units.pacman.get_position().to_rel()).get_length()
            for i in range(1, len(dirs)):
                cur_dist = (self.position.to_rel() + dirs[i]
                            - self.game.units.pacman.get_position().to_rel()).get_length()
                if dirs[i] != -self.direction and cur_dist < min_dist:
                    self.set_direction(dirs[i])
                    min_dist = cur_dist
        else:
            self.set_direction(Direction.ZERO)
        if self.position.to_rel() == self.game.units.pacman.get_position().to_rel():
            pass  # обработка съедания пакмена
        super(Ghost, self).move()

    def set_destination(self, destination):
        """Set destination of ghost"""
        self.destination = destination

    def get_destination(self):
        """Return destination of ghost"""
        return self.destination

    def set_mode(self, mode):
        """Set mode of ghost
        0 - ...
        1 - ...
        2 - ..."""
        self.mode = mode

    def set_spawn_cell(self, vector):
        super(Ghost, self).set_spawn_cell(vector)
        self.set_random_direction()

    def set_random_direction(self):
        dirs = self.game.field.get_cell_directions(self.position.to_rel())
        if dirs:
            # self.direction = dirs[random.randint(0, len(dirs) - 1)]
            self.set_direction(dirs[0])
        else:
            self.set_direction(Direction.ZERO)


class Blinky(Ghost):
    def __init__(self, game, spawn_cell=None):
        if spawn_cell == None:
            spawn_cell = Vector()
        super(Blinky, self).__init__(game=game, spawn_cell=spawn_cell)
        self.image = Image.get('../resrc/ghosts/Blinky_Up.gif')

    def move(self):
        self.set_destination(self.game.units.pacman.get_position().to_rel())
        super(Blinky, self).move()


class Pinky(Ghost):
    def __init__(self, game, spawn_cell=None):
        if spawn_cell == None:
            spawn_cell = Vector()
        super(Pinky, self).__init__(game=game, spawn_cell=spawn_cell)
        self.image = Image.get('../resrc/ghosts/Pinky_Up.gif')

    def move(self):
        self.set_destination(
            self.game.units.pacman.get_position().to_rel() + self.game.units.pacman.get_direction() * 4)
        super(Pinky, self).move()


class Inky(Ghost):
    def __init__(self, game, spawn_cell=None):
        if spawn_cell == None:
            spawn_cell = Vector()
        super(Inky, self).__init__(game=game, spawn_cell=spawn_cell)
        self.image = Image.get('../resrc/ghosts/Inky_Up.gif')

    def move(self):
        self.set_destination(
            self.game.units.blinky.get_destination() * 2 -
            self.game.units.blinky.get_position().to_rel())
        super(Inky, self).move()


class Clyde(Ghost):
    def __init__(self, game, spawn_cell=None):
        if spawn_cell == None:
            spawn_cell = Vector()
        super(Clyde, self).__init__(game=game, spawn_cell=spawn_cell)
        self.image = Image.get('../resrc/ghosts/Clyde_Up.gif')

    def get_distance_to_pacman(self):
        return (self.position.to_rel() - self.game.units.pacman.get_position().to_rel()).get_length()

    def move(self):
        if self.get_distance_to_pacman() >= 9:
            self.set_destination(self.game.units.pacman.get_position().to_rel())
        else:
            self.set_destination(Vector(0, 1))
        super(Clyde, self).move()


class Units(object):
    """Represents all units in game"""

    def __init__(self, game):
        self.game = game
        self.pacman = None
        self.blinky = None
        self.pinky = None
        self.inky = None
        self.clyde = None

    def add_pacman(self, spawn_cell):
        """Set Pacman from spawn cell"""
        self.pacman = Pacman(self.game, spawn_cell)

    def add_blinky(self, spawn_cell):
        """Set Blinky from spawn cell"""
        self.blinky = Blinky(self.game, spawn_cell)

    def add_pinky(self, spawn_cell):
        """Set Pinky from spawn cell"""
        self.pinky = Pinky(self.game, spawn_cell)

    def add_inky(self, spawn_cell):
        """Set Inky from spawn cell"""
        self.inky = Inky(self.game, spawn_cell)

    def add_clyde(self, spawn_cell):
        """Set Clyde from spawn cell"""
        self.clyde = Clyde(self.game, spawn_cell)

    def get_all(self):
        """Return tuple of all units"""
        res = []
        for u in (self.pacman, self.blinky, self.pinky, self.inky, self.clyde):
            if u:
                res.append(u)
        return tuple(res)

    def draw(self):
        for u in self.get_all():
            u.draw()
