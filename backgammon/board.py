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


COLOR = {1: 'W', -1: 'B', 0: ' '}


class Board(object):
    """
    A Board object.
    1 is the while player
    -1 is the black player
    """

    def __init__(self):
        self.board = [[] for _ in range(24)]
        self.bar = list()
        self.out = list()
        self.white_to_bear = 10
        self.black_to_bear = 10

    def __repr__(self):
        """
        Print the board with W letter for white's checkers and B for black's
        :return: empty (str)
        """
        max_up = min(max([len(v) for v in self.board[: 12]]), 5)
        max_down = min(max([len(v) for v in self.board[12:]]), 5)
        height = max_up + max_down + 1

        board_up = self.board[: 12][::-1]
        board_down = self.board[12:]

        print('-------------------------')
        print('--------THE BOARD--------')
        print('-------------------------')
        print(' B A 9 8 7 6 5 4 3 2 1 0 ')

        for j in range(height):
            print('|', end='')

            if j < max_up:  # print from upper board
                for cols in board_up:
                    if len(cols) > j:
                        print(f'{COLOR[cols[j]]}|', end='')
                    else:
                        print(' |', end='')

            elif j == max_up:
                for _ in range(12):
                    print(' |', end='')

            else:
                for cols in board_down:
                    index = height - j - len(cols)
                    if index < 1:
                        print(f'{COLOR[cols[index]]}|', end='')
                    else:
                        print(' |', end='')

            print()

        print(' 0 1 2 3 4 5 6 7 8 9 A B')
        print('-------------------------')
        print(f'Bar: {["W" if i == 1 else "B" for i in self.bar]}')
        print(f'Out: {["W" if i == 1 else "B" for i in self.out]}')
        return ''

    def initialize(self):
        """ Initialize the board with the starting setting """

        # White checkers
        self.board[0] = [1] * 2
        self.board[11] = [1] * 5
        self.board[16] = [1] * 3
        self.board[18] = [1] * 5

        # Black checkers
        self.board[23 - 0] = [-1] * 2
        self.board[23 - 11] = [-1] * 5
        self.board[23 - 16] = [-1] * 3
        self.board[23 - 18] = [-1] * 5

    def put_checker_(self, player, point):
        """
        Put a checker in a point
        :param player:
        :param pos:
        :return:
        """
        if point == 'bar':
            self.bar.append(player)
        elif point == 'out':
            self.out.append(player)
        else:
            self.board[point].append(player)

    def remove_checker_(self, player, point):
        """
        Remove a checker from a point
        :param player:
        :param pos:
        :return:
        """
        if point == 'bar':
            self.bar.remove(player)
        else:
            self.board[point].remove(player)

    def len_point(self, point: int):
        """
        Returns the numer of checkers in a point
        :param point: point id
        :return:
        """
        return len(self.board[point])

    def is_hit_point(self, point, player):
        """
        Check if a point is a hit for player
        :param player:
        :return:
        """
        if self.len_point(point) == 1 and self.board[point][0] != player:
            return False
        else:
            return True

    def is_open_point(self, point, player):
        """
        Check if a point is open for player
        :param point:
        :param player:
        :return:
        """
        if self.len_point(point) > 1 and self.board[point][0] == -player:
            return False
        else:
            return True

    def next_points(self, point, player):
        """
        Return the list of next points in the board for player
        :param point:
        :param player:
        :return:
        """
        if player == 1:
            if self.white_to_bear <= 0:
                return self.board[point:] + 'out'
            return self.board[point:]
        else:
            if self.black_to_bear <= 0:
                return self.board[:-point][::-1] + 'out'
            return self.board[:-point][::-1]
