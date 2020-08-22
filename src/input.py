import pygame
from vector import (Vector, Direction)


# class Input(type):
#     def __init__(cls):
#         cls.instance=None
#     def __call__(cls, *args, **kwargs):
#         if cls.instance==None:
#             cls.instance=super(Input, cls).__call__(*args, **kwargs)
#         return cls.instance

class Input():
    exit = False
    # Mouse variables
    mouse_position = Vector()
    mouse_mode = 0
    # 0 - link
    # 1 - hover
    # 2 - active

    # Keyboard variables
    key_direction = Direction.ZERO
    key_dict = {
        pygame.K_UP: Direction.UP,
        pygame.K_DOWN: Direction.DOWN,
        pygame.K_LEFT: Direction.LEFT,
        pygame.K_RIGHT: Direction.RIGHT
    }

    @staticmethod
    def update():
        Input.mouse_update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Input.exit = True
            if event.type == pygame.MOUSEMOTION:
                Input.set_mouse_position(pygame.mouse.get_pos())
            if event.type == pygame.MOUSEBUTTONDOWN:
                Input.on_mouse_down()
            if event.type == pygame.MOUSEBUTTONUP:
                Input.on_mouse_up()
            if event.type == pygame.KEYDOWN:
                if event.key in Input.key_dict:
                    Input.set_key_direction(Input.key_dict.get(event.key))

    @staticmethod
    def set_mouse_position(position):
        Input.mouse_position = Vector(position)

    @staticmethod
    def get_mouse_position():
        return Input.mouse_position

    @staticmethod
    def on_mouse_down():
        Input.mouse_mode = 1

    @staticmethod
    def on_mouse_up():
        Input.mouse_mode = 2

    @staticmethod
    def get_mouse_mode():
        return Input.mouse_mode

    @staticmethod
    def mouse_update():
        if Input.mouse_mode == 2:
            Input.mouse_mode = 0

    @staticmethod
    def set_key_direction(direction):
        Input.key_direction = direction

    @staticmethod
    def quit():
        Input.exit = True
