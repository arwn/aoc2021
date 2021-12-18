import sys
import itertools
import pprint


with open("input_4") as f:
    header = f.readline().rstrip().split(",")
    f.readline()

    boards = []
    currentBoard = []
    for line in f.readlines():
        line = line.rstrip()
        if len(line) < 1:
            boards.append(currentBoard)
            currentBoard = []
        else:
            line = [int(e) for e in line.split()]
            currentBoard.append(line)
    boards.append(currentBoard)

called = set()


def getWinner():
    for i, board in enumerate(boards):
        for row in board:
            if all(e in called for e in row):
                return i
        for row in (zip(*board[::-1])):
            if all(e in called for e in row):
                return i
    return None


def p1():
    for e in header:
        called.add(int(e))
        winner = getWinner()
        if winner is not None:
            boardn = winner
            board = boards[boardn]
            unmarked = [e for e in itertools.chain(*board) if e not in called]
            print(sum(unmarked) * int(e))
            return
    print("no winner")


# part 2
def p2():
    for e in header:
        called.add(int(e))
        winner = getWinner()
        while winner is not None:
            if len(boards) < 2:
                print("one board left")
                unmarked = [e for e in itertools.chain(
                    *boards[0]) if e not in called]

                print(f"{unmarked} * {e}={sum(unmarked) * int(e)}")
                sys.exit(0)
            boards.pop(winner)
            winner = getWinner()


p1()
p2()
