import time


class Timer:
    def __init__(self, start=False):
        self.__paused = not start
        self.__elapsed_time = 0
        self.__time_point = time.time()

    def is_paused(self):
        return self.__paused

    def elapsed_time(self):
        return self.__elapsed_time

    def restart(self):
        self.__elapsed_time = 0

    def pause(self):
        self.__paused = True

    def resume(self):
        self.__paused = False

    def start(self):
        self.restart()
        self.resume()

    def stop(self):
        self.restart()
        self.pause()

    def update(self):
        if not self.is_paused():
            self.__elapsed_time += time.time() - self.__time_point
        self.__time_point = time.time()
