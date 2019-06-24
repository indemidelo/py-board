import numpy as np


class bcolors:
    CYANO = '\033[96m'
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    GRAY = '\033[90m'
    UNDERLINE = '\033[4m'
    BOLD = '\033[1m'
    ENDC = '\033[0m'


class Game(object):
    def __init__(self):
        self.board = [] * 24
        self.playing = True
        self.plays = 0
        self.winner = None
        self.reward = 0

    @staticmethod
    def input_shape():
        return

    @staticmethod
    def policy_shape():
        return

    def __repr__(self):
        pass

    @property
    def hash(self):
        return ''.join(''.join(str(int(k)) for k in j) for j in self.board)

    def play_(self, player, index):
        return

    def index_to_pos(self, index):
        return

    def game_over(self, *args):
        return
