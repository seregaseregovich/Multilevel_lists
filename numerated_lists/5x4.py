# creating matrix m = 5x4
m = [[0 for i in range(5)] for j in range(4)]
for i in m:
    print(i)  # printing m
i = 0  # index i
j = 0  # index j
h = 1  # horisontal moving:
        # +1 - to the right
        # 0 - no move
        # -1 - to the left
v = 0  # vertical moving:
        # +1 - down
        # 0 - no move
        # -1 - up
n = 1

while m[i][j] == 0:
    m[i][j] = n
    n += 1
    if h == 1 and v == 0 \
            or j + h == -1 \
            or j + h == len(m[i]) \
            or m[i + h][j + v] != 0:
        h = 0
        v = 1
    if h == 0 and v == 1 \
            or j + h == -1 \
            or j + h == len(m[i]) \
            or m[i + h][j + v] != 0:
        h = -1
        v = 0
    if h == 1 and v == 0 \
            or j + h == -1 \
            or j + h == len(m[i]) \
            or m[i + h][j + v] != 0:
        h = 0
        v = -1
    if h == 1 and v == 0 \
            or j + h == -1 \
            or j + h == len(m[i]) \
            or m[i + h][j + v] != 0:
        h = 0
        v = 1
    i += h
    j += v