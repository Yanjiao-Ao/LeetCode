def isValidSudoku_1(board):
    row = [{},{},{},{},{},{},{},{},{}]
    column = [{},{},{},{},{},{},{},{},{}]
    box = [{},{},{},{},{},{},{},{},{}]
    #验证每一行：
    for i in range(9):
        for j in range(9):
            if board[i][j] != ".":
                if board[i][j] not in row[i]:
                    row[i][board[i][j]] = 1
                else: #board[i][j] in row
                    row[i][board[i][j]] += 1
    #验证每一列：
            if board[j][i] != ".":
                if board[j][i] not in column[i]:
                    column[i][board[j][i]] = 1
                else:
                    column[i][board[j][i]] += 1
    #每一个3乘以3的方块：第[i][j]个元素在第k = (i//3)*3+(j//3)个方块
            k = (i//3)*3 + j//3
            if board[i][j] != ".":
                if board[i][j] not in box[k]:
                    box[k][board[i][j]] = 1
                else:
                    box[k][board[i][j]] += 1

    # for i in range(9):
    #     print('row',i)
    #     print(row[i])
    # for i in range(9):
    #     print('box',i)
    #     print(box[i])
    # for i in range(9):
    #     print('column',i)
    #     print(column[i])

    #{k:v for k, v in test_dict.items() if v>=3}
    sum = row + column + box
    for i in range(len(sum)):
        for item in sum[i]:
            if sum[i][item] >= 2:
                return False
    return True

board = [
      ["8","3",".",".","7",".",".",".","."],
      ["6",".",".","1","9","5",".",".","."],
      [".","9","8",".",".",".",".","6","."],
      ["8",".",".",".","6",".",".",".","3"],
      ["4",".",".","8",".","3",".",".","1"],
      ["7",".",".",".","2",".",".",".","6"],
      [".","6",".",".",".",".","2","8","."],
      [".",".",".","4","1","9",".",".","5"],
      [".",".",".",".","8",".",".","7","9"]
    ]

#---------------------------------------------------------

def isValidSudoku_2(board):
    map = {}

    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == ".":
                continue

            inRow = str(board[i][j]) + " in row " + str(i)
            inCol = str(board[i][j]) + " in col " + str(j)
            inBox = str(board[i][j]) + " in box " + str(i//3) + " " + str(j//3)

            # print(inRow)
            # print(inCol)
            # print(inBox)

            if inRow in  map or inCol in map or inBox in map:
                return False
            else:
                map[inRow] = 1
                map[inCol] = 1
                map[inBox] = 1

    return True


print(isValidSudoku_2(board))
