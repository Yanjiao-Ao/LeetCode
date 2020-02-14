def rotate(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if i < j:
                matrix[i][j],matrix[j][i] = matrix[j][i], matrix[i][j]
    for i in range(len(matrix)):
        matrix[i].reverse()
    return matrix


matrix = [
          [ 1, 2, 3],
         [ 4, 5, 6],
        [ 7, 8, 9],

        ]

print(rotate(matrix))
