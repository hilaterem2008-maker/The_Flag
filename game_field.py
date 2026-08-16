from consts import BOARD_HEIGHT , BOARD_WIDTH
import random

def create_start_board() :
    board = [[[] for _ in range(BOARD_WIDTH)] for _ in range(BOARD_HEIGHT)]


def get_possible_mine_positions() :
    list_options_mine_row = []
    list_options_mine_col = []
    for r in range(BOARD_HEIGHT):
        list_options_mine_row.append(r)
    for c in range(BOARD_WIDTH):
        list_options_mine_col.append(c)



def get_random_mine_position_in_row(list_options_row , list_options_col) :
    mine_position_row = []
    mine_position_col = []
    while len(mine_position_row) != 20 :
        to_append = random.choice(list_options_row)
        while to_append in mine_position_row :
            to_append = random.choice(list_options_row)
        mine_position_row.append(to_append)
    return mine_position_row


