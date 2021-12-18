from pprint import pprint

with open('input_11') as file:
	board = [[int(x) for x in line.rstrip()] for line in file.readlines()]

def adj(i, j):
    xs = []
    l = j > 0
    r = j < len(board[0])-1
    u = i > 0
    d = i < len(board)-1
    if u:
        xs.append((i-1,j))
    if d:
        xs.append((i+1, j))
    if l:
        xs.append((i,j-1))
    if r:
        xs.append((i, j+1))
    if u and l:
        xs.append((i-1, j-1))
    if u and r:
        xs.append((i-1, j+1))
    if d and l:
        xs.append((i+1, j-1))
    if d and r:
        xs.append((i+1, j+1))
    return xs

def flash(i, j, flashed):
    if (i,j) in flashed:
        return
    if board[i][j] <= 9:
        return
    flashed.add((i,j))
    for p in adj(i, j):
        board[p[0]][p[1]] += 1
        flash(p[0], p[1], flashed)

def step():
    flashcount = 0
    flashed = set()

    for i in range(len(board)):
        for j in range(len(board[i])):
            board[i][j] += 1
            
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] > 9:
                if (i,j) not in flashed:
                    flash(i, j, flashed)

    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] > 9:
                flashcount += 1
                board[i][j] = 0
    
    return len(flashed)

x = sum([step() for x in range(100)])
#p1
print(x)

cycles = 100
while True:
    f = step()
    cycles += 1
    if f == len(board) * len(board[0]):
        #p2
        print(cycles)
        break