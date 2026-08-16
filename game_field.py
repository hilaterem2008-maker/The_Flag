from consts import AMOUNT_OF_COLS , AMOUNT_OF_ROWS
import random

def create_start_board() :
    board = [[[] for _ in range(AMOUNT_OF_COLS)] for _ in range(AMOUNT_OF_ROWS)]


def get_possible_mine_positions() :
    list_options_mine_row = []
    list_options_mine_col = []
    for r in range(AMOUNT_OF_ROWS):
        list_options_mine_row.append(r)
    for c in range(AMOUNT_OF_COLS):
        list_options_mine_col.append(c)



def get_random_mine_position(list_options) :     #Call this function twice - once for rows and once for columns
    mine_position_options = []
    while len(mine_position_options) != 20 :
        to_append = random.choice(list_options)
        while to_append in mine_position_options :
            to_append = random.choice(list_options)
        mine_position_options.append(to_append)
    return mine_position_options






