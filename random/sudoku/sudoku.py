board = [
	[8,6,0,0,2,0,0,0,0],
	[0,0,0,7,0,0,0,5,9],
	[0,0,0,0,0,0,0,0,0],
	[0,0,0,0,6,0,8,0,0],
	[0,4,0,0,0,0,0,0,0],
	[0,0,5,3,0,0,0,0,7],
	[0,0,0,0,0,0,0,0,0],
	[0,2,0,0,0,0,6,0,0],
	[0,0,7,5,0,9,0,0,0]
]

def solve(bo):
    find = find_next(bo)
    
    if not find:
        return True
    
    for i in range(1,10):
        if valid(bo, i, find):
            x, y = find
            bo[x][y] = i

            if solve(bo):
                return True

            bo[x][y] = 0

    return False

def valid(bo, num, pos):
    # check row
    for i in range(len(bo)):
        if bo[pos[0]][i] == num and i != pos[1]:
            return False

    # check column
    for i in range(len(bo)):
        if bo[i][pos[1]] == num and i != pos[0]:
            return False

    # check square
    x, y = [value // 3 for value in pos]

    for i in range(x*3, x*3 + 3):
        for j in range(y*3, y*3 + 3):
            if bo[i][j] == num and (i,j) != pos:
                return False

    return True
            
def find_next(bo):
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j] == 0:
                return (i,j)
    return None

def draw_board(bo):
    output = []
    for i in range(len(bo)):
        if i % 3 == 0 and i != 0:
            output.append("-----------------------\n")
        for j in range(len(bo[0])):
            if j % 3 == 0 and j != 0:
                output.append(" | ")

            if j == 8:
                output.append(str(bo[i][j]) + "\n")
            else:
                output.append(str(bo[i][j]) + " ")

    print("".join(output))

draw_board(board)
print('################')
solve(board)
draw_board(board)