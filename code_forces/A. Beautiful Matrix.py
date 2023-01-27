matrix = []
one_row, one_col = 0, 0

# input matrix and find the location of the one
for i in range(5):
    row = list(map(int, input().split()))
    matrix.append(row)
    if 1 in row:
        one_row = i
        one_col = row.index(1)

# calculate number of moves needed to move the one to the middle
row_moves = abs(2 - one_row)
col_moves = abs(2 - one_col)

print(row_moves + col_moves)