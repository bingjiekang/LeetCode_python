# board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]

# # 存对应已输入数字
# lt = []
# Trow = [[False for i in range(9)] for j in range(9)]
# Tcol = [[False for i in range(9)] for j in range(9)]
# Tbox = [[[False for i in range(9)] for j in range(3)] for x in range(3)]
# for row in range(9):
#     for col in range(9):
#         if board[row][col] != ".":
#             temp = int(board[row][col])-1
#             Trow[row][temp] = True
#             Tcol[col][temp] = True
#             Tbox[col//3][col//3][temp] = True
#         else:
#             lt.append((row,col))

# print(lt)
a = "11"
b = "1"
print(int(a,2)+int(b,2))