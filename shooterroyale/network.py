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
    SERVER_BULLET_INFO = 2
    CLIENT_PLAYER_INFO = 3
    CLIENT_BULLET_INFO = 4


class Message:
    '''
    Message sent via sockets between server and clients.
    '''
    def __init__(self, msg_type, msg_data):
        self.type = msg_type
        self.data = msg_data
