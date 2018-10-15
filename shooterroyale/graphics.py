'''
graphics.py

Module that contains graphics related classes.
'''
import pygame as pg


class Sheet:
    '''
    Loads a sheet and converts it into an array of tiles.
    '''
    def __init__(self, tile_size=(32, 32), image=None):
        self.__tiles = []
        self.tile_size = tile_size
        self.image = image

    def load(self, filename):
        self.image = pg.image.load(filename)
        tsize = self.tile_size

        for c_x in range(self.image.get_size()[0] // tsize[0]):
            row = []
            for c_y in range(self.image.get_size()[1] // tsize[1]):
                coord = (c_x * tsize[0], c_y * tsize[1])
                frame = self.image.subsurface(pg.Rect(coord, tsize))
                row.append(frame)
            self.__tiles.append(row)

    def get_tile(self, index_x, index_y):
        return self.__tiles[index_x][index_y].copy()
