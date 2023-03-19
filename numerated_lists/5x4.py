''' Creating matrix (size = AxB),
filled with numbers from 1 to matrix size (A*B). '''

# Stage 1: creating matrix.
a = int(input('Enter horizontal matrix size (integer number): '))
b = int(input('Enter vertical matrix size (integer number): '))
m = [[0] * a for i in range(b)]
# Stage 2. Creating initial conditions (position and direction)
# for initial and further enumeration and filling of matrix
# cells. Initial position is left-upper cell of the matrix (m[0][0]).
x = -1  # position x (index)
y = 0  # position y (index)
dx = 1  # direction x (1 - right, 0 - no move, -1 - left)
dy = 0  # direction y (1 - down, 0 - no move, -1 - up)
n = 1  # content of first matrix cell (m[0][0])
# Stage 3. Implementation of control over the excess
# of the upper value of the matrix content (condition for loop exit).
while n <= a * b:
    # Stage 4. Implementation of control over feeling the free cells.
    # Implementation of control over the formation
    # of correct indexes of matrix cells during the moving.
    if 0 <= x + dx < len(m[0]) and 0 <= y + dy < len(m) \
            and m[y + dy][x + dx] == 0:
        x += dx
        y += dy
        m[y][x] = n
        n += 1
    else:
        # Stage 5. Implementation of conditions for changing
        # the directions of moving due to impossibility
        # of fulfilling the previous conditions.
        if dx == 1:
            dx = 0
            dy = 1
        elif dy == 1:
            dx = -1
            dy = 0
        elif dx == -1:
            dx = 0
            dy = -1
        elif dy == -1:
            dx = 1
            dy = 0
# Printing of result.
for i in m:
    print(i)
