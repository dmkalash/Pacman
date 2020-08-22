# -*- coding: utf-8 -*-
import codecs
from drawable import Drawable
from vector import Vector, Direction
from cell import Cell
from image import Image


class Field(Drawable):
    """Class that represents the field with cells"""
    path_to_images = ''

    def __init__(self, path_to_field_images='../resrc/field_images/', vector=None):
        if vector == None:
            vector = Vector()
        super(Field, self).__init__(position=vector)
        Field.path_to_images = path_to_field_images
        Cell.path_to_images = Field.path_to_images
        self.filename = ''
        self.cells = []
        self.seed_count = 0

    def get_size(self):
        # type: () -> Vector
        """Return size vector of all cells"""
        return Vector(len(self.cells), len(self.cells[0]))

    def parse(self, filename):
        # type: (str) -> None
        """Parse map"""
        self.seed_count = 0
        self.filename = filename
        self.cells = []
        type_arr = []
        with codecs.open('../resrc/maps/' + self.filename, 'r') as map_file:

            lines = map_file.readlines()
            for row in range(len(lines)):
                type_arr.append([])
                for i in range(len(lines[row][:-1])):
                    type = str(lines[row][i])
                    type_arr[row].append(type)

        type_arr_f = []  # отражаем массив относительно главной диагонали
        for y in range(len(type_arr[0])):
            type_arr_f.append([])
            for x in range(len(type_arr)):
                if len(type_arr[x]) != len(type_arr[0]):
                    raise FieldSizeError(row=x, row_len=len(type_arr[x]),
                                         z_len=len(type_arr[0]))
                type_arr_f[y].append(type_arr[x][y])

        self.cells = [[type_arr_f[x][y] for y in range(len(type_arr_f[x]))]
                      for x
                      in range(len(type_arr_f))]
        for x in range(len(type_arr_f)):
            for y in range(len(type_arr_f[x])):
                type = type_arr_f[x][y]
                self.set_cell(Cell(type, Vector(x + .5, y + .5).to_abs()),
                              Vector(x, y))
                if type not in ['0', 'w', 'd', 'e', 'g', 's', 't', 'p']:
                    raise FieldElementError(type=type, pos=Vector(x, y))
                if type == 'p':
                    self.pacman_spawn = Vector(x, y)
                elif type == 'g':
                    self.ghost_spawn = Vector(x, y)
                elif type == 's':
                    self.seed_count += 1

                if type == 'w':  # отрисовка стен
                    img_file = ''
                    if y:
                        if type_arr_f[x][y - 1] == 'w':
                            img_file += 't'  # top
                    if x != len(type_arr_f) - 1:
                        if type_arr_f[x + 1][y] == 'w':
                            img_file += 'r'  # right
                    if y != len(type_arr_f[x]) - 1:
                        if type_arr_f[x][y + 1] == 'w':
                            img_file += 'b'  # bottom
                    if x:
                        if type_arr_f[x - 1][y] == 'w':
                            img_file += 'l'  # left
                    if img_file == '':
                        img_file = 'w'
                    self.cells[x][y].set_image(Image.get(
                        Field.path_to_images + 'walls/' + img_file +
                        '.gif'))
                elif type in ['p', 'g', 't']:
                    self.cells[x][y].set_image(Image.get(
                        Field.path_to_images + '0.gif'))
                else:
                    self.cells[x][y].set_image(Image.get(
                        Field.path_to_images + type + '.gif'))

    def get_cell(self, vector_rel):
        # type: (Vector) -> Cell
        """Return cell on vector_rel"""
        vector_rel = vector_rel.floor()
        if 0 <= vector_rel.x < len(self.cells) and 0 <= vector_rel.y < len(self.cells[vector_rel.x]):
            return self.cells[vector_rel.x][vector_rel.y]
        else:
            raise IndexError(str(vector_rel) + ' is out of field')

    def get_cell_by_abs(self, vector_abs):
        # type: (Vector) -> Cell
        """Return cell from absolute coordinates"""
        rel = vector_abs.to_rel()
        try:
            return self.cells[rel.x][rel.y]
        except IndexError:
            raise IndexError(str(rel) + ' is out of field')

    def set_cell(self, cell, vector=None):
        # type: (Cell, Vector) -> None
        """Set cell on position"""
        if vector == None:
            vector = Vector()
        try:
            self.cells[int(vector.x)][int(vector.y)] = cell
        except IndexError:
            raise IndexError(str(vector) + ' is out of field')

    def set_cell_type(self, vector, type='0'):
        # type: (Vector, str) -> None
        try:
            self.cells[vector.x][vector.y].set_type(type)
        except IndexError:
            raise IndexError(str(vector) + ' is out of field')

    def get_seed_count(self):
        # type: () -> int
        """Return number of remaining seeds"""
        return self.seed_count

    def draw(self):
        """Draw all cells"""
        for cell_collumn in self.cells:
            for cell in cell_collumn:
                cell.draw()

    def get_pacman_spawn(self):
        # type: () -> Vector
        """Return vector of pacman spawn cell"""
        return self.pacman_spawn

    def get_ghosts_spawn(self):
        # type: () -> Vector
        """Return vector of ghosts spawn cell"""
        return self.ghost_spawn

    def get_cell_directions(self, vector_rel):
        # type: (Vector) -> list
        res = []
        for dir in Direction.ALL:
            try:
                if self.get_cell(vector_rel + dir).is_passable():
                    res.append(dir)
            except IndexError:
                pass
        return res


class FieldElementError(Exception):
    def __init__(self, *args, **kwargs):
        if len(kwargs):
            self.type = kwargs.get('type', '0')
            self.pos = kwargs.get('pos', Vector())
        elif len(args):
            self.type = args[0]
            self.pos = args[1]
        else:
            self.type = '0'
            self.pos = Vector()

    def __str__(self):
        return ("unknown element type '{type}' in {pos}".format(
            type=self.type, pos=self.pos))


class FieldSizeError(Exception):
    def __init__(self, *args, **kwargs):
        if kwargs:
            self.row = kwargs.get('row', 0)
            self.row_len = kwargs.get('row_len', 0)
            self.z_len = kwargs.get('z_len', 0)
        elif args:
            self.row = args[0]
            self.row_len = args[1]
            self.z_len = args[2]
        else:
            self.row = 0
            self.row_len = 0
            self.z_len = 0

    def __str__(self):
        return (
            'field is not a rectangle: length of row {row} ({row_len}) does '
            'not matches length of first row ({z_len}).'.format(
                row=self.row, row_len=self.row_len, z_len=self.z_len))
