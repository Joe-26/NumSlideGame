import random
import random
import copy


def generateMatrix(n):
    board = []
    i = 1
    while i < (n**2) + 1:
        count = 0
        buffer = []
        while count < n:
            buffer.append(i)
            i += 1
            count += 1
        board.append(buffer)
    board[n - 1][n - 1] = '-'
    return board


def shuffleBoard(board):
    left(board)
    up(board)
    for i in range(100):
        move = random.choice([1, 2, 3, 4])
        if move == 1:
            up(board)
        elif move == 2:
            down(board)
        elif move == 3:
            left(board)
        elif move == 4:
            right(board)
    return board

def printBoard(board):
    print('X\t\t'*(len(board)+1))
    rownum = 0
    for row in board:
        print('X', end = '\t\t')
        for _ in row:
            print(_, end='\t\t')
        rownum += 1
        print()


def swap(a, b):
    buffer = a
    a = b
    b = buffer
    return a, b


def emptyLoc(board):
    empty = (0, 0)
    for row in range(len(board)):
        for col in range(len(board)):
            if board[row][col] == '-':
                empty = (row, col)
                return empty


def up(board):
    empty = emptyLoc(board)

    if empty[0] == 0:
        print('Move not possible!')
        return board
    else:
        board[empty[0]][empty[1]], board[empty[0] - 1][empty[1]] = swap(board[empty[0]][empty[1]], board[empty[0] - 1][empty[1]])
        printBoard(board)
        return board


def down(board):
    empty = emptyLoc(board)

    if empty[0] == len(board) -1:
        print('Move not possible!')
        return board
    else:
        board[empty[0]][empty[1]], board[empty[0] + 1][empty[1]] = swap(board[empty[0]][empty[1]], board[empty[0] + 1][empty[1]])
        printBoard(board)
        return board


def left(board):
    empty = emptyLoc(board)

    if empty[1] == 0:
        print('Move not possible!')
        return board
    else:
        board[empty[0]][empty[1]], board[empty[0]][empty[1] - 1] = swap(board[empty[0]][empty[1]], board[empty[0]][empty[1] - 1])
        printBoard(board)
        return board


def right(board):
    empty = emptyLoc(board)

    if empty[1] == len(board) - 1:
        print('Move not possible!')
        return board
    else:
        board[empty[0]][empty[1]], board[empty[0]][empty[1] + 1] = swap(board[empty[0]][empty[1]], board[empty[0]][empty[1] + 1])
        printBoard(board)
        return board


def check(board, og):
    if board == og:
        print('You Won!')
        return True
    else:
        return False


if __name__ == '__main__':
    chooseSize = int(input('Enter 3 for 3 X 3; 4 for 4 X 4 and so on: '))
    originalBoard = generateMatrix(chooseSize)
    board = shuffleBoard(copy.deepcopy(originalBoard))
    printBoard(board)

    while True:
        userInput = input('Enter Key - ')
        if userInput == 'w':
            up(board)
            if check(board, originalBoard): break
        elif userInput == 'a':
            left(board)
            if check(board, originalBoard): break
        elif userInput == 'd':
            right(board)
            if check(board, originalBoard): break
        elif userInput == 's':
            down(board)
            if check(board, originalBoard): break

