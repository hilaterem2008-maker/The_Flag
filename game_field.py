from consts import AMOUNT_OF_COLS , AMOUNT_OF_ROWS
import random

def create_start_board() :
    board = [[[] for _ in range(AMOUNT_OF_COLS)] for _ in range(AMOUNT_OF_ROWS)]
    return board


def get_possible_mine_positions() :
    list_options_mine_row = []
    list_options_mine_col = []
    for r in range(AMOUNT_OF_ROWS):
        list_options_mine_row.append(r)
    for c in range(AMOUNT_OF_COLS):
        list_options_mine_col.append(c)
    return list_options_mine_row , list_options_mine_col


def create_list_mine_position_options_rows(list_options) :
    mine_position_options_row = []
    valid_len = 20
    while len(mine_position_options_row) != valid_len :
        to_append = random.choice(list_options)
        while to_append in mine_position_options_row :
            to_append = random.choice(list_options)
        mine_position_options_row.append(to_append)
    return mine_position_options_row


def create_list_mine_position_options_cols(list_options , start_list_positions) :
    valid_len = 20
    biggest_possible_number = AMOUNT_OF_COLS - 3
    while len(start_list_positions) != valid_len :
        to_append = random.choice(list_options)
        while to_append in start_list_positions or to_append > biggest_possible_number:
            to_append = random.choice(list_options)
        start_list_positions.append(to_append)
    return start_list_positions


def check_mine_position_options_col(mine_position_to_check) :
    len_list_to_check = len(mine_position_to_check)
    list_to_remove = []
    while mine_position_to_check != []:
        for number in mine_position_to_check:
            for i in range(len_list_to_check) :
                if mine_position_to_check[i] == number + 1 :
                    list_to_remove.append(mine_position_to_check[i])
                elif mine_position_to_check[i] == number + 2 :
                    list_to_remove.append(mine_position_to_check[i])
    return list_to_remove


def main():
    board = create_start_board()
    list_options_mine_row, list_options_mine_col = get_possible_mine_positions()
    mine_position_options_row = create_list_mine_position_options_rows(list_options_mine_row)
    start_list_positions = []
    create_list_mine_position_options_cols(list_options_mine_col, start_list_positions)








    # list_options_mine_row, list_options_mine_col = get_possible_mine_positions()
    # mine_position_options_row = create_list_mine_position_options_rows(list_options_mine_row)
    # mine_position_options_col = []
    # mine_position_options_col = create_list_mine_position_options_cols(list_options_mine_col , mine_position_options_col)
    # list_remove_number = check_mine_position_options_col(mine_position_options_col)
    # for character in list_remove_number :
    #     while character in mine_position_options_col :
    #         mine_position_options_col.remove(character)
    # valid_len = 20
    # while len(mine_position_options_col) != valid_len :
    #     mine_position_options_col = create_list_mine_position_options_cols(list_options_mine_col , mine_position_options_col)
    #     mine_position_options_col = check_mine_position_options_col(mine_position_options_col)
    # print(mine_position_options_col , "mine_position_to_check")
    # print(mine_position_options_row)






main()