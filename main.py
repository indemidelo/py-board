from backgammon.game import Game, Board


# For testing purposes
g = Game()
g.initialize()
print(g)
g.play_(1, 0, 9)
print(g)
g.play_(-1, 7, 9)
print(g)
g.play_(-1, 7, 5)
print(g)
# g.play(1, 0, 11)
# print(g)
g.play_(-1, 5, 7)
print(g)