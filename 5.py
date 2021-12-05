import pprint
import itertools

coords = []

with open("input_5") as f:
    for line in f.readlines():
        x = [[int(e) for e in x.strip().split(',')]
             for x in line.split("->")]
        if len(x) > 0:
            coords.append(x)


def nondiagonal(line):
    [[x1, y1], [x2, y2]] = line
    if x1 != x2 and y1 != y2:
        return False
    return True


def makeboard(x, y):
    return [[0 for _ in range(x)] for _ in range(y)]


nondiagonalCoords = [x for x in coords if nondiagonal(x)]
diagonalCoords = [x for x in coords if not nondiagonal(x)]
board = makeboard(990, 990)


def drawLine(pts):
    [[x1, y1], [x2, y2]] = pts
    if x1 == x2:
        for e in range(min(y1, y2), max(y1, y2) + 1):
            board[e][x1] += 1
    else:
        for e in range(min(x1, x2), max(x1, x2) + 1):
            board[y1][e] += 1


def q1():
    for e in nondiagonalCoords:
        drawLine(e)
    crosses = [x for x in itertools.chain(*board) if x > 1]
    print("q1: ", len(crosses))


q1()


def drawDiagonalLine(pts):
    [[x1, y1], [x2, y2]] = pts
    if x1 > x2:
        x1, x2 = x2, x1
        y1, y2 = y2, y1
    direction = 1 if y1 < y2 else -1
    for i, e in enumerate(range(x1, x2 + 1)):
        board[y1 + (i * direction)][e] += 1


def q2():
    for e in diagonalCoords:
        drawDiagonalLine(e)
    crosses = [x for x in itertools.chain(*board) if x > 1]
    print("q2: ", len(crosses))


q2()
