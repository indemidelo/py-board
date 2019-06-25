def list_possible_moves(dice_1, dice_2):
    """
    List all possible moves with dices outcomes
    :param dice_1: result from dice 1
    :param dice_2: result from dice 2
    :return: list of list of moves
    """
    moves = list()

    if dice_1 == dice_2:
        moves.append((dice_1, dice_1 * 3))
        moves.append((dice_1 * 4,))
        moves.append((dice_1 * 2, dice_1 * 2))
    else:
        moves.append((dice_1, dice_2))
        moves.append((dice_1 + dice_2,))

    return moves
