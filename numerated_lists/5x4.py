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
v = 1  # vertical moving:
        # +1 - down
        # 0 - no move
        # -1 - up
n = 1
