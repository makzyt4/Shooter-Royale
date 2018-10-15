'''
graphics.py

Module that contains graphics related classes.
'''
import pygame as pg


class Sheet:
    '''
    Loads a sheet and converts it into an array of frames.
    '''
    def __init__(self, frame_size=(32, 32), image=None):
        self.__frames = []
        self.frame_size = frame_size
        self.image = image

    def load(self, filename):
        self.image = pg.image.load(filename).convert()
        fsize = self.frame_size

        for c_x in range(self.image.get_size()[0] // fsize[0]):
            for c_y in range(self.image.get_size()[1] // fsize[1]):
                coord = (c_x * fsize[0], c_y * fsize[1])
                frame = self.image.subsurface(pg.Rect(coord, fsize))
                self.__frames.append(frame)

    def get_frame(self, index):
        return self.__frames[index].copy()
