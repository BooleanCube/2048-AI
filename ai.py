import time
import algorithm

move_delay = 0.1


# AI TAKES TURN
def generate_move(board_values, game_over):
    direction = ''
    score = 0
    if not game_over:
        direction, score = algorithm.search_move_tree(board_values, 20, 10)

    return direction, score, time.time()+move_delay
