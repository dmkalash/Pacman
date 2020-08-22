from pygame import image


class Image(object):
    @staticmethod
    def get(path):
        return image.load(path)
