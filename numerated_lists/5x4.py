# creating matrix m = 5x4
m = [[0 for i in range(5)] for j in range(4)]
# m = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
for i in m:
    print(i)  # printing m
x = -1  # initial position in the column (horisontal moving)
y = 0  # initial position in the string (vertical moving)
dx = 1  # moving in the column (horisontal moving):
        # +1 - to the right
        # 0 - no move
        # -1 - to the left
dy = 0  # moving in the string (vertical moving):
        # +1 - down
        # 0 - no move
        # -1 - up
n = 1

while n <= 25:
    if 0 <= x + dx <= len(m[x]) and 0 <= y + dy <= len(m) and m[y + dy][x + dx] == 0:
        x += dx
        y += dy
        m[y][x] = n
        n += 1
    else:
        if dx == 1 and dy == 0:
            dx = 0
            dy = 1
        elif dx == 0 and dy == 1:
            dx = -1
            dy = 0
        elif dx == -1 and dy == 0:
            dx = 0
            dy = -1
        elif dx == 0 and dy == -1:
            dx = 1
            dy = 0
for i in m:
    print(i)

