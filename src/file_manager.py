import pygame
from image import Image


class FileManager():
    path_to_seed = "../resrc/objects/Seed.gif"
    path_to_energizer = "../resrc/objects/Red_pill.gif"
    #
    path_to_wall_down_left = "../resrc/new_walls/dl.gif"
    path_to_wall_down_right = "../resrc/new_walls/dr.gif"
    path_to_wall_left_right = "../resrc/new_walls/lr.gif"
    path_to_wall_up_down = "../resrc/new_walls/ud.gif"
    path_to_wall_up_left = "../resrc/new_walls/ul.gif"
    path_to_wall_up_right = "../resrc/new_walls/ur.gif"
    #
    path_to_wall_middle_right = "../resrc/new_walls/mr.gif"
    path_to_wall_middle_left = "../resrc/new_walls/ml.gif"
    path_to_wall_middle_up = "../resrc/new_walls/mu.gif"
    path_to_wall_middle_down = "../resrc/new_walls/md.gif"
    #
    path_to_wall_end_right = "../resrc/new_walls/er.gif"
    path_to_wall_end_left = "../resrc/new_walls/el.gif"
    path_to_wall_end_up = "../resrc/new_walls/eu.gif"
    path_to_wall_end_down = "../resrc/new_walls/ed.gif"
    path_to_door = "../resrc/walls/Door.gif"
    #
    path_to_main_menu_background = "../resrc/tabs/main_menu/background.gif"
    #
    path_to_play_button = "../resrc/tabs/main_menu/play.gif"
    path_to_shop_button = "../resrc/tabs/main_menu/shop.gif"
    path_to_levels_button = "../resrc/tabs/main_menu/levels.gif"
    path_to_records_button = "../resrc/tabs/main_menu/records.gif"
    path_to_exit_button = "../resrc/tabs/main_menu/exit.gif"
    #
    path_to_play_button_pressed = "../resrc/tabs/main_menu/play_pressed.gif"
    path_to_shop_button_pressed = "../resrc/tabs/main_menu/shop_pressed.gif"
    path_to_levels_button_pressed = "../resrc/tabs/main_menu/levels_pressed.gif"
    path_to_records_button_pressed = "../resrc/tabs/main_menu/records_pressed.gif"
    path_to_exit_button_pressed = "../resrc/tabs/main_menu/exit_pressed.gif"
    #

    wall_dict = {
        'lr': pygame.image.load(path_to_wall_left_right),
        'ud': pygame.image.load(path_to_wall_up_down),
        'ul': pygame.image.load(path_to_wall_up_left),
        'ur': pygame.image.load(path_to_wall_up_right),
        'dl': pygame.image.load(path_to_wall_down_left),
        'dr': pygame.image.load(path_to_wall_down_right),
        'mr': pygame.image.load(path_to_wall_middle_right),
        'ml': pygame.image.load(path_to_wall_middle_left),
        'mu': pygame.image.load(path_to_wall_middle_up),
        'md': pygame.image.load(path_to_wall_middle_down),
        'ed': pygame.image.load(path_to_wall_end_down),
        'el': pygame.image.load(path_to_wall_end_left),
        'eu': pygame.image.load(path_to_wall_end_up),
        'er': pygame.image.load(path_to_wall_end_right),
        'do': pygame.image.load(path_to_door),
        '00': pygame.image.load(path_to_seed),
        'ez': pygame.image.load(path_to_energizer),
        'oo': pygame.image.load(path_to_seed),
    }
    button_dict = {
        'play': pygame.image.load(path_to_play_button),
        'shop': pygame.image.load(path_to_shop_button),
        'exit': pygame.image.load(path_to_exit_button),
        'records': pygame.image.load(path_to_records_button),
        'play_pressed': pygame.image.load(path_to_play_button_pressed),
        'shop_pressed': pygame.image.load(path_to_shop_button_pressed),
        'exit_pressed': pygame.image.load(path_to_exit_button_pressed),
        'records_pressed': pygame.image.load(path_to_records_button_pressed),
    }

    @staticmethod
    def get_button_image(type):
        return Image.get(FileManager.button_images.get(type, ''))

    @staticmethod
    def get_button_image(type):
        return FileManager.button_dict.get(type)

    @staticmethod
    def get_image_main_menu_background():
        return Image.get(FileManager.path_to_main_menu_background)
