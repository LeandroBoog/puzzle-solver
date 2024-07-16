import copy
from game import perform_move


# This initial game state can be ignored since all 4 available moves achieve the same result just mirrored
# ([5, 3], [4, 3], [3, 3]) == ([1, 3], [2, 3], [3, 3]) == ([3, 5], [3, 4], [3, 3]) == ([1, 3], [2, 3], [3, 3])
state_initial = [
    [-1, -1, 1, 1, 1, -1, -1],
    [-1, -1, 1, 1, 1, -1, -1],
      [1, 1, 1, 1, 1, 1, 1],
      [1, 1, 1, 0, 1, 1, 1],
      [1, 1, 1, 1, 1, 1, 1],
    [-1, -1, 1, 1, 1, -1, -1],
    [-1, -1, 1, 1, 1, -1, -1],
]

# Hence, we consider the second board state which has two unique next moves
state_after_first_move = copy.deepcopy(state_initial)
perform_move(state_after_first_move, ([5, 3], [4, 3], [3, 3]))

# This board is another mirror
# ([4, 5], [4, 4], [4, 3]) ==  ([4, 1], [4, 2], [4, 3])
state_v_1 = copy.deepcopy(state_after_first_move)
perform_move(state_v_1, ([4, 5], [4, 4], [4, 3]))

# While this is the last unique state
state_v_2 = copy.deepcopy(state_after_first_move)
perform_move(state_v_2, ([2, 3], [3, 3], [4, 3]))
