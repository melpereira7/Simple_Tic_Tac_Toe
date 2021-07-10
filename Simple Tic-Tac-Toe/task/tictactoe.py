# write your code here
import string


def x_in_a_row(cells_):
    counter = 0
    for cell in range(3):
        if cells[cell][0] == cells[cell][1] == cells[cell][2] == 'X':
            counter += 1
        if cells[0][cell] == cells[1][cell] == cells[2][cell] == 'X':
            counter += 1
    if cells_[0][0] == cells_[1][1] == cells_[2][2] == 'X':
        counter += 1
    if cells_[2][0] == cells_[1][1] == cells_[0][2] == 'X':
        counter += 1
    return counter


def o_in_a_row(cells_):
    counter = 0
    for cell in range(3):
        if cells[cell][0] == cells[cell][1] == cells[cell][2] == 'O':
            counter += 1
        if cells[0][cell] == cells[1][cell] == cells[2][cell] == 'O':
            counter += 1
    if cells_[0][0] == cells_[1][1] == cells_[2][2] == 'O':
        counter += 1
    if cells_[2][0] == cells_[1][1] == cells_[0][2] == 'O':
        counter += 1
    return counter


def print_grid(cells_):
    print(f"---------")
    print(f"| {cells_[0][0]} {cells_[0][1]} {cells_[0][2]} |")
    print(f"| {cells_[1][0]} {cells_[1][1]} {cells_[1][2]} |")
    print(f"| {cells_[2][0]} {cells_[2][1]} {cells_[2][2]} |")
    print("---------")


cells = [[' ' for i in range(3)] for j in range(3)]

print_grid(cells)
turn = 0
while True:
    coords = input("Enter the coordinates: ")
    c1 = coords.split(' ')[0]
    c2 = coords.split(' ')[1]

    if c1 not in string.digits or c2 not in string.digits:
        print("You should enter numbers!")
    elif 1 < int(c1) > 3 or 1 < int(c2) > 3:
        print("Coordinates should be from 1 to 3!")
    elif cells[int(c1) - 1][int(c2) - 1] != ' ':
        print("This cell is occupied! Choose another one!")
    else:
        if turn % 2 == 0:
            cells[int(c1) - 1][int(c2) - 1] = 'X'
        else:
            cells[int(c1) - 1][int(c2) - 1] = 'O'
        print_grid(cells)
        x = 0
        o = 0
        empty = 0
        for i in range(3):
            x += cells[i].count('X')
            o += cells[i].count('O')
            empty += cells[i].count(' ')

        if x_in_a_row(cells) == 1:
            print('X wins')
            break
        elif o_in_a_row(cells) == 1:
            print('O wins')
            break
        elif empty == 0:
            print('Draw')
            break

