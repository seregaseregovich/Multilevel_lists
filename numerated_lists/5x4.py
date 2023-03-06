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

while m[i][j] == 0:
    m[i][j] = n
    n += 1
    if n <= 25:
        if j + h == len(m[i]) or m[i + v][j + h] != 0:
            h = 0
            v = 1
        elif i + v == len(m)-1 or m[i + v][j + h] != 0:
            h = -1
            v = 0
        elif j + h == -1 or m[i + v][j + h] != 0:
            h = 0
            v = -1
        elif i + v == -1 or m[i + v][j + h] != 0:
            h = 1
            v = 0
        i += v
        j += h
    else:
        break
for i in m:
    print(i)
