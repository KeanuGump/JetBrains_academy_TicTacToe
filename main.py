field = "         "
p = 0
# win = 0
state = ""


def field_print(fields):
    # i = 0
    print("---------")
    for i in range(0, 9, 3):
        print("|", fields[i], fields[i + 1], fields[i + 2], "|")
    print("---------")


def user_move(fields):
    global p
    # taking user's input

    in_x, in_y = input("Enter the coordinates: ").split()

    # sanitizing input--------------------------------------------------------------------------

    while not in_x.isnumeric() or not in_y.isnumeric():
        print("You should enter numbers!")
        in_x, in_y = input("Enter the coordinates: ").split()

    while int(in_y) > 3 or int(in_x) > 3:
        print("Coordinates should be from 1 to 3!")
        in_x, in_y = input("Enter the coordinates: ").split()

    while fields[int(in_y) - 1 + (int(in_x) - 1) * 3] != " ":  # converting coordinates in situ
        print("This cell is occupied! Choose another one!")
        in_x, in_y = input("Enter the coordinates: ").split()

    # done sanitizing input---------------------------------------------------------------------

    in_x = int(in_x) - 1            #
    in_y = int(in_y) - 1            # converting coordinates
    input_fields = in_y + in_x * 3  #

    # updating the field
    current_player = ['X', 'O']
    fields = list(fields)
    fields[input_fields] = current_player[p % 2]
    p += 1
    global field
    field = "".join(fields)


# big block for checking the state


def win_condition(fields):
    # x = 0
    # o = 0
    # global win
    global state
    # checking for wins in lines
    for i in range(0, 9, 3):
        if fields[i] == fields[i + 1] == fields[i + 2] and fields[i] != " ":
            state = fields[i] + " wins"
    #        win += 1
            return True
    # checking for wins in columns
    for i in range(3):
        if fields[i] == fields[i + 3] == fields[i + 6] and fields[i] != " ":
            state = fields[i] + " wins"
    #        win += 1
            return True
    # checking for wins in diagonals
    if (fields[0] == fields[4] == fields[8] or fields[2] == fields[4] == fields[6]) and fields[4] != " ":
        state = fields[4] + " wins"
    #    win += 1
        return True
    # check if game is in progress or draw
    if not any([cell == " " for cell in fields]):
        # win += 1
        state = "Draw"
        return True
        # for cell in field:
        #     if cell == " ":
        #         state = "Game not finished"
    # check for invalid game
    # for cell in fields:
    #    if cell == "X":
    #        x += 1
    #    if cell == "O":
    #        o += 1
    # if abs(x - o) > 1 or win > 1:
    #    state = "Impossible"
    return False

# ---------------------------------------------------------------------------------------------


field_print(field)

while True:
    if win_condition(field):
        print(state)
        break
    user_move(field)
    field_print(field)

