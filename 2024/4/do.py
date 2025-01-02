f = open('data.txt', 'r')

matrix = []

for line in f.readlines():
    data = line
    data = data.replace('\n', '')
    matrix.append(list(data))

f.close()

cnt = 0

def count_XMAS(matrix):
    global cnt
    for arr in matrix:
        # XMAS
        x = "".join(arr)
        while "XMAS" in x:
            cnt += 1
            x = x.replace("XMAS", "....", 1)
        # SAMX
        x = "".join(arr)
        while "SAMX" in x:
            cnt += 1
            x = x.replace("SAMX", "....", 1)

# horizontal string
count_XMAS(matrix)

# vertical string
"""
0123
0123
0123
"""
rotated_matrix = [[] for i in range(len(matrix[0]))]
for arr in matrix:
    idx = 0
    for x in arr:
        rotated_matrix[idx].append(x)
        idx += 1
count_XMAS(rotated_matrix)

# diagonal string \
diagonal_matrix_1 = []
step = 0
for arr in matrix:
    """
    0123 step:0
    4012 step:1
    5401 step:2
    6540 step:3
    7654 step:4
    8765 step:5
    9876 step:6
    ...
    """
    """
    01234567 step:0
    80123456 step:1
    """
    idx = 0
    for x in arr:
        real_idx = idx - step
        if real_idx < 0:
            real_idx = - real_idx + len(arr) - 1
        if len(diagonal_matrix_1) > real_idx:
            diagonal_matrix_1[real_idx].append(x)
        else:
            diagonal_matrix_1.append([x])
        idx += 1
    step += 1
count_XMAS(diagonal_matrix_1)

# diagonal string /
diagonal_matrix_2 = []
step = 0
for arr in matrix:
    """
    0123 step:0
    1234 step:1
    2345 step:2
    3456 step:3
    4567 step:4
    ...
    """
    idx = 0
    for x in arr:
        real_idx = idx + step
        if len(diagonal_matrix_2) > real_idx:
            diagonal_matrix_2[real_idx].append(x)
        else:
            diagonal_matrix_2.append([x])
        idx += 1
    step += 1
count_XMAS(diagonal_matrix_2)

print(cnt)


    