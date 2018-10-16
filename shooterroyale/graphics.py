import pygame as pg
import shooterroyale.time as sr_t


class Sheet:
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


class Animation:
    def __init__(self, frames, frame_time, play=True):
        self.frames = frames
        self.frame_time = frame_time
        self.timer = sr_t.Timer(play)
        self.__current_frame_index = 0

    def get_current_frame(self):
        return self.frames[self.__current_frame_index]

    def update(self):
        self.timer.update()

        if self.timer.elapsed_time() > self.frame_time:
            self.__current_frame_index += 1
            self.__current_frame_index %= len(self.frames)
            self.timer.restart()

    def is_paused(self):
        return self.timer.is_paused()

    def elapsed_time(self):
        return self.timer.elapsed_time()

    def restart(self):
        self.timer.restart()

    def pause(self):
        self.timer.pause()

    def resume(self):
        self.timer.resume()

    def start(self):
        self.timer.start()

    def stop(self):
        self.timer.stop()
