
import random


choose_size = 8

alpha = ["A", "B", "C", "D", "E", "F", "G", "H"]
score_o = 1
score_x = 1
blank = 0


# display game board
def board(info):
    grid = ['|{:1}' * choose_size + '|' for n in range(choose_size)]
    print()
    print(" O " + str(score_o) + " - " + str(score_x) + " X ")
    print("-" * (2 * choose_size + 2))

    data_row = ["", "", "", "", "", "", "", ""]

    x = 0
    for row in grid:
        for y in range(choose_size):
            if info[x][y] == 0:
                data_row[y] = ""
            elif info[x][y] == 1:
                data_row[y] = "O"
            elif info[x][y] == 2:
                data_row[y] = "X"
            else:
                data_row[y] = "#"
        x = x + 1
        print(str(choose_size - x + 1) + row.format(data_row[0], data_row[1], data_row[2], data_row[3], data_row[4],
                                                    data_row[5], data_row[6], data_row[7]))

    print("-" * (2 * choose_size + 2))
    print((" " + "|{:1}" * choose_size + "|").format("A", "B", "C", "D", "E", "F", "G", "H"))


# display next step path
def path(info, player):
    if player == 1:
        x, y = 0, 0
        for row in info:
            for col in row:
                if col == 1:
                    print("( " + str(alpha[x]) + " , " + str(choose_size - y) + " )")
                x += 1
            y += 1
            x = 0


# add new moves
def move(col, row, info, player):
    global blank
    global score_o
    global score_x

    x = choose_size - int(row)
    y = alpha.index(col)

    if player == 0:
        if info[x][y] == 2:
            info[x][y] = 3
            blank += 1
            score_o += 1
            score_x -= 1
        elif info[x][y] == 0:
            info[x][y] = 1
            score_o += 1

    elif player == 1:
        if info[x][y] == 1:
            info[x][y] = 3
            blank += 1
            score_o -= 1
            score_x += 1
        elif info[x][y] == 0:
            info[x][y] = 2
            score_x += 1
    board(info)


if __name__ == '__main__':
    size = input("Enter size of board: ")
    choose_size = int(size)
    total = choose_size * choose_size

    data = [[0] * choose_size for n in range(choose_size)]
    data[choose_size - 1][0] = 1
    data[0][choose_size - 1] = 2

    board(data)

    step = 0
    while total >= 0:
        total = total - score_x - score_o - blank
        if step % 2 == 0:
            print()
            print("player O")
            x = input("Enter row: ").upper()
            y = input("Enter column: ")
        else:
            print("player X")
            n = random.randint(0, choose_size-1)
            x = alpha[n % choose_size]
            y = str(n % choose_size)

        move(x, y, data, step % 2)
        step += 1

    if score_o > score_x:
        print("Player O win!!!")
    elif score_x > score_o:
        print("Player X win!!!")
    else:
        print("!!!")


