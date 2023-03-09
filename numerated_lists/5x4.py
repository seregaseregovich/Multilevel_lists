# creating matrix m = 5x4
m = [[0 for i in range(5)] for j in range(4)]
# m = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
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

while n <= 25:
    if m[i][j] == 0:
        m[i][j] = n
        n += 1
        if j + h == len(m[i]):
            h = 0
            v = 1
        elif i + v == len(m):
            h = -1
            v = 0
        elif j + h == -1:
            h = 0
            v = -1
        elif i + v == -1:
            h = 1
            v = 0
    else:
        if h == 1 and v == 0 and m[i][j] != 0:
            h = 0
            v = 1
            i += v
            j += h
            continue
        elif h == 0 and v == 1 and m[i][j] != 0:
            h = -1
            v = 0
            i += v
            j += h
            continue
        elif h == -1 and v == 0 and m[i][j] != 0:
            h = 0
            v = -1
            i += v
            j += h
            continue
        elif h == 0 and v == -1 and m[i][j] != 0:
            h = 1
            v = 0
            i += v
            j += h
            continue
    i += v
    j += h
for i in m:
    print(i)
