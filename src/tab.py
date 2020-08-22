# -*- coding:utf8 -*-
from vector import Vector
from input import Input
from file_manager import FileManager
from drawable import (Drawable)
from painter import Painter


class Tab(object):
    def __init__(self, wrapper, background_image):
        self.wrapper = wrapper  # Оболочка
        self.background_image = background_image
        self.size = self.background_image.get_rect().size  # Размер

    def get_size(self):
        return Vector(self.background_image.get_rect().size)

    def draw(self):
        Painter.draw(self.background_image, (0, 0))


class MainMenu(Tab):
    def __init__(self, wrapper):
        super(self.__class__, self).__init__(wrapper, FileManager.get_image_main_menu_background())
        self.button_play = Button(Vector(325, 200), FileManager.get_button_image('play'),
                                  FileManager.get_button_image('play_pressed'),
                                  FileManager.get_button_image('play_pressed'),
                                  self.play_button_press)
        self.button_shop = Button(Vector(325, 290), FileManager.get_button_image('shop'),
                                  FileManager.get_button_image('shop_pressed'),
                                  FileManager.get_button_image('shop_pressed'),
                                  self.shop_button_press)
        self.button_records = Button(Vector(325, 290 + 90), FileManager.get_button_image('records'),
                                     FileManager.get_button_image('records_pressed'),
                                     FileManager.get_button_image('records_pressed'),
                                     self.records_button_press)
        self.button_exit = Button(Vector(325, 290 + 90 + 90), FileManager.get_button_image('exit'),
                                  FileManager.get_button_image('exit_pressed'),
                                  FileManager.get_button_image('exit_pressed'),
                                  self.exit_button_press)

    #

    def play_button_press(self):
        # self.wrapper.current_menu = self.wrapper.simple_menu
        print "Play button"
        pass

    def shop_button_press(self):
        # current tab -> SHOP TAB (in procees)
        print "Shop button"
        pass

    def records_button_press(self):
        print "Records button"
        # current tab -> RECORD TAB (in process)
        pass

    def exit_button_press(self):
        print "Exit button"
        Input.quit()

    def update(self):
        self.button_play.update()
        self.button_shop.update()
        self.button_records.update()
        self.button_exit.update()

    def draw(self):
        super(self.__class__, self).draw()
        Painter.draw(self.button_play)
        Painter.draw(self.button_shop)
        Painter.draw(self.button_records)
        Painter.draw(self.button_exit)


class Button(Drawable):
    def __init__(self, position, link_image, hover_image, active_image, func):
        self.link_image = link_image
        self.hover_image = hover_image
        self.active_image = active_image
        self.func = func
        self.image_dict = {
            0: self.hover_image,
            1: self.active_image,
            2: self.active_image
        }
        super(self.__class__, self).__init__(position=position,
                                             image=self.link_image)

    def is_inside(self, position):
        return (
                   self.position.x <= position.x <= self.position.x + self.get_size().x) and \
               (
                   self.position.y <= position.y <= self.position.y + self.get_size().y)

    def get_image_rect(self):
        if self.is_inside(Input.get_mouse_position()):
            self.set_image(self.image_dict.get(Input.get_mouse_mode()))
        else:
            self.set_image(self.link_image)
        return super(self.__class__, self).get_image_rect()

    def update(self):
        if self.is_inside(
                Input.get_mouse_position()) and Input.mouse_mode == 2:
            self.press()

    def press(self):
        self.func()

# class SimpleMenu(Tab):
#     def __init__(self, wrapper):
#         self.size = (400, 500)
#         super(self.__class__, self).__init__(wrapper, self.size)
#         self.mouse_position = Position()
#         self.mouse_status = 0
#         self.play_button = StandardButton(self, Position(40, 40), 'End Game', self.play_button_press)
#         self.shop_button = StandardButton(self, Position(40, 160), 'Back', self.shop_button_press)
#         # 0 - not pressed
#         # 1 - down
#         # 2 - up
#     def play_button_press(self):
#         self.wrapper.current_menu = self.wrapper.main_menu
#
#     def shop_button_press(self):
#         pass
#
#     def update(self):
#         self.low_update()
#
#     def draw(self, surface):
#         self.play_button.draw()
#         self.shop_button.draw()

# class Button(Drawable): # Не изучай
#     def __init__(self, tab, position, text, text_color, idle_color, mouse_on_color,
#                  pressed_color, edging, press_function):
#         self.tab = tab
#         self.position = position
#         self.idle_color = idle_color
#         self.mouse_on_color = mouse_on_color
#         self.pressed_color = pressed_color
#         self.text = text
#         self.text_color = text_color
#         self.font = pygame.font.Font(None, 72)
#         self.text_render = self.font.render(self.text, 1, self.text_color)
#         self.text_rect = self.text_render.get_rect()
#         self.size = Position.to_pos(self.text_rect.size) + edging
#         self.text_rect.center = self.get_rect().center
#
#
#
#         self.press_function = press_function
#
#
#
#
#     def is_inside(self, position):    # Является ли позиция внутри кнопки
#         return (self.position.x <= position.x <= self.position.x + self.size.x) and \
#                (self.position.y <= position.y <= self.position.y + self.size.y)
#
#     def get_rect(self):
#         return pygame.Rect(self.position.x, self.position.y, self.size.x, self.size.y)
#
#     def press(self):
#         self.press_function()
#
#     def draw(self):
#         if self.is_inside(self.tab.mouse_position):
#             if self.tab.mouse_mode == 0:
#                 pygame.draw.rect(self.tab.wrapper.screen, self.mouse_on_color, self.get_rect())
#             elif self.tab.mouse_mode == 1:
#                 pygame.draw.rect(self.tab.wrapper.screen, self.pressed_color, self.get_rect())
#             elif self.tab.mouse_mode == 2:
#                 self.press()
#                 pygame.draw.rect(self.tab.wrapper.screen, self.mouse_on_color, self.get_rect())
#         else:
#             pygame.draw.rect(self.tab.wrapper.screen, self.idle_color, self.get_rect())
#         self.tab.wrapper.screen.blit(self.text_render, self.text_rect)
#
# class StandardButton(Button):
#     def __init__(self, tab, position, text, press_function): # press_function - функция, выполняющаяся при нажатии
#         self.text_color = (13, 33, 73)              # Цвет текста
#         self.idle_color = (249, 235, 224)           # Обычный цвет кнопки
#         self.mouse_on_color = (32, 138, 174)        # Цвет кнопки, над которой мышка
#         self.pressed_color = (255, 255, 255)        # Цвет зажатой кнопки
#         self.edging = Position(10, 10)              # Размер окантовки
#         super(self.__class__, self).__init__(tab, position, text, self.text_color, self.idle_color,
#                                              self.mouse_on_color, self.pressed_color, self.edging, press_function)
