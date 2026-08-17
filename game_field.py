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
    valid_len = 20
    list_mine_indexes = []
    while len(list_mine_indexes) != valid_len :
        mine_index = random.choice(list_options)
        while mine_index in list_mine_indexes :
            mine_index = random.choice(list_options)
        list_mine_indexes.append(mine_index)
    return list_mine_indexes


def create_list_mine_position_options_cols(list_options) :
    valid_len = 60
    list_mine_indexes = []
    biggest_possible_number = AMOUNT_OF_COLS - 3
    len_list = len(list_mine_indexes)
    while len_list != valid_len :
        mine_index_possible = []
        item_valid = True
        mine_index = random.choice(list_options)
        while mine_index in list_mine_indexes or mine_index > biggest_possible_number:
            mine_index = random.choice(list_options)
        for a in range(0 , 3) :
            mine_index_possible.append(mine_index + a)
        for item in mine_index_possible :
            if item in list_mine_indexes or item > biggest_possible_number:
                item_valid = False
        if item_valid :
            for character in mine_index_possible :
                if not character in list_mine_indexes :
                    list_mine_indexes.append(character)
        len_list = len(list_mine_indexes)
    return list_mine_indexes






def check(list_options_row , list_options_col):
    valid_len_row = 20
    list_mine_indexes = []
    while len(list_mine_indexes) != valid_len_row:
        mine_index = random.choice(list_options_row)
        while mine_index in list_mine_indexes:
            mine_index = random.choice(list_options_row)
        list_mine_indexes.append(mine_index)












# def check_mine_position_options_col(mine_position_to_check) :
#     len_list_to_check = len(mine_position_to_check)
#     list_to_remove = []
#     while mine_position_to_check != []:
#         for number in mine_position_to_check:
#             for i in range(len_list_to_check) :
#                 if mine_position_to_check[i] == number + 1 :
#                     list_to_remove.append(mine_position_to_check[i])
#                 elif mine_position_to_check[i] == number + 2 :
#                     list_to_remove.append(mine_position_to_check[i])
#     return list_to_remove


def main():
    board = create_start_board()
    list_options_mine_row, list_options_mine_col = get_possible_mine_positions()
    mine_indexes_row = create_list_mine_position_options_rows(list_options_mine_row)
    mine_indexes_col = create_list_mine_position_options_cols(list_options_mine_col)
    print("col" , mine_indexes_col , "row" , mine_indexes_row)









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