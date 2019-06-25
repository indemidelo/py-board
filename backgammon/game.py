import numpy as np
from backgammon.board import Board
from utils import list_possible_moves


class Game(object):
    def __init__(self, board=None):
        self.board = board or Board()
        self.bar = []
        self.out = []
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
        """
        Print the board
        :return:
        """
        print(self.board)
        return ''

    def initialize(self):
        """
        Initialize the board
        :return:
        """
        self.board.initialize()
        # self.board_to_print = self.board
        # self.board = {}
        # self.board['bar'] = self.board_to_print.bar
        # self.board['out'] = self.board_to_print.out
        # self.board.update({j: v for j, v in enumerate(self.board_to_print.board)})

    @property
    def hash(self):
        return ''.join(''.join(str(int(k)) for k in j) for j in self.board)

    def play_(self, player, from_pos, to_pos):
        """
        The player moves a checker from from_pos to to_pos
        :param player: (label) making the move
        :param from_pos: (start)
        :param to_pos: (destination)
        :return: None
        """
        self.check_hit_(player, to_pos)
        self.board.put_checker_(player, to_pos)
        self.board.remove_checker_(player, from_pos)

    def check_hit_(self, player, to_pos):
        """
        Check if the move is a hit
        :param player: (label) making the move
        :param to_pos: (destination)
        :return: bool
        """
        if self.board.is_hit_point(to_pos, player):
            self.board.remove_checker_(-player, to_pos)
            self.board.put_checker_(-player, 'bar')

    def list_available_moves(self, player, dices):
        """
        List all the available moves for player when rolls the dices
        :param player: (label) making the move
        :param dice_1: (list) dices results.
            Could be two different int or four identical int (0-5)
            Two different dices results [A, B]:
            - checker #1 moves by A positions and checker #2 moves by B positions
            - checker #1 moves by A + B positions.
            Two identical dices results [A, A]:
            - four checkers moves by A positions,
            - two checkers moves by A and two by 2 * A positions
            - one checkers moves by 4 * A positions
        :return: (list) of moves
        """
        available_moves = []
        moves = list_possible_moves(*dices)
        if player in self.bar:
            for m in moves:
                if len(m) == 2:
                    if self.board.is_open_point(player, m[0]):
                        available_moves += [{'from': 'bar', 'to': m[0]}]

    def list_available_moves_easy(self, player, dices):
        """
        List all the available moves for player when rolls the dices
        :param player: (label) making the move
        :param dice_1: (list) dices results.
            Could be two different int or four identical int (0-5)
            Two different dices results [A, B]:
            - checker #1 moves by A positions and checker #2 moves by B positions
            - checker #1 moves by A + B positions.
            Two identical dices results [A, A]:
            - four checkers moves by A positions,
            - two checkers moves by A and two by 2 * A positions
            - one checkers moves by 4 * A positions
        :return: (list) of moves
        """
        available_moves = []

    def moves_from_position(self, player, from_pos):
        """
        List all movements available from a position
        :param player: (label) making the move
        :param from_pos:
        :return: (list) of moves
        """
        if player == 1:
            for k, v in self.board.items():
                pass

    def game_over(self, *args):
        return
