import consts


def soldier_body_index(soldier_location):
    soldier_y = soldier_location[1]
    soldier_x = soldier_location[0]
    body_indexes = []
    for i in range(3):
        soldier_y += consts.SIDE_LENGTH
        board_row = soldier_y / consts.SIDE_LENGTH
        for j in range(2):
            soldier_x += consts.SIDE_LENGTH
            board_col = soldier_x / consts.SIDE_LENGTH
            body_indexes.append(board_row, board_col)
    return body_indexes

def soldier_legs_location(soldier_location):
    soldier_y = soldier_location[1]
    soldier_x = soldier_location[0]
    leg_indexes = []
    soldier_y += 3 * consts.SIDE_LENGTH
    board_row = soldier_y/ consts.SIDE_LENGTH
    for i in range(2):
        soldier_x += consts.SIDE_LENGTH
        board_col = soldier_x / consts.SIDE_LENGTH
        leg_indexes.append(board_row, board_col)
    return leg_indexes


print("bye")




