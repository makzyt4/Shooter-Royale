'''
network.py

Module that contains network related classes.
'''
import enum
import pickle


class MessageType(enum.Enum):
    '''
    Enum type of Message object.
    '''
    SERVER_NEW_PLAYER_INFO = 0
    SERVER_PLAYER_INFO = 1
    CLIENT_PLAYER_INFO = 2


class Message:
    '''
    Message sent via sockets between server and clients.
    '''
    def __init__(self, msg_type, msg_data):
        self.type = msg_type
        self.data = msg_data

    def pack(self):
        '''
        Dump Message object into binary.
        '''
        return pickle.dumps(self)

    def unpack(self):
        '''
        Load message binary into Message object.
        '''
        return pickle.loads(self)
