'''
network.py

Module that contains network related classes.
'''
import enum


class MessageType(enum.Enum):
    '''
    Enum type of Message object.
    '''
    SERVER_NEW_PLAYER_INFO = 0
    SERVER_PLAYER_INFO = 1
    CLIENT_PLAYER_INFO = 2
