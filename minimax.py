import copy
from game import get_valid_moves, perform_move, get_heuristic

target_heuristic = 1


def minimax(game_state, moves_stack):

    if get_heuristic(game_state) == target_heuristic:
        print(f"Found order of moves which achieves desired score of {target_heuristic}!")
        print(moves_stack)
        # can just exit since we found our solution
        exit(1)

    nextMoves = get_valid_moves(game_state)
    if len(nextMoves) == 0:
        return

    for move in nextMoves:
        # store current move in the stack
        moves_stack.append(move)

        # play the move
        new_game_state = copy.deepcopy(game_state)
        perform_move(new_game_state, move)

        # continue depth first search
        minimax(new_game_state, moves_stack)

        # remove last move from stack, since we are returning from depth
        moves_stack.pop()

    return f"No order of moves found with specified score of {target_heuristic}"
