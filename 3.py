with open('in_data.txt') as f_in:
    matrix_data = [list(map(float, row.split())) for row in f_in.readlines()]
    print(matrix_data)