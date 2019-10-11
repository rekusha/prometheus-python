def maze_controller(mr):
    x = 0
    y = 0
    rotate_y = 1
    rotate_x = 0
    a = [[1]]
    while (mr.found() == False):
        if y + rotate_y <= 0:
            a = [[0] * len(a[-1])] + a
            y = y + 1
        if len(a) - 1 <= y + rotate_y:
            a.append([0] * len(a[-1]))
        if x + rotate_x <= 0:
            map(lambda x: x.insert(0, 0), a)
            x = x + 1
        if len(a[y]) - 1 <= x + rotate_x:
            map(lambda x: x.append(0), a)
        steps = min(a[y - 1][x], a[y][x - 1], a[y][x + 1], a[y + 1][x])
        while a[y + rotate_y][x + rotate_x] != steps:
            mr.turn_right()
            rotate_x, rotate_y = 0 if rotate_x else (1 if rotate_y == 1 else -1),\
                0 if rotate_y else (-1 if rotate_x == 1 else 1)
        if mr.go():
            y += rotate_y
            x += rotate_x
            a[y][x] += 1
        else:
            a[y + rotate_y][x + rotate_x] = 'x'