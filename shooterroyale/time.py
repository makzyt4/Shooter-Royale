'''
time.py

Module that contains time related classes, like Timer for example.
'''
import time


class Timer:
    '''
    A class that can measure time (like a Clock) and can be paused, restarted,
    unpaused etc.
    '''
    def __init__(self, start=False):
        self.__paused = not start
        self.__elapsed_time = 0
        self.__time_point = time.time()

    def is_paused(self):
        '''
        Returns __paused field value.
        '''
        return self.__paused

    def elapsed_time(self):
        '''
        Returns __elapsed_time field value (in seconds).
        '''
        return self.__elapsed_time

    def restart(self):
        '''
        Sets __elapsed_time field to 0.
        '''
        self.__elapsed_time = 0

    def pause(self):
        '''
        Sets __paused field to True.
        '''
        self.__paused = True

    def resume(self):
        '''
        Sets __paused field to False.
        '''
        self.__paused = False

    def start(self):
        '''
        Restarts and resumes the timer.
        '''
        self.restart()
        self.resume()

    def stop(self):
        '''
        Restarts and pauses the timer.
        '''
        self.restart()
        self.pause()

    def update(self):
        '''
        Updates the __elapsed_time field with time difference of __time_point
        and time.time() if the timer is paused.
        '''
        if not self.is_paused():
            self.__elapsed_time += time.time() - self.__time_point
        self.__time_point = time.time()
