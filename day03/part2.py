input_value = 277678

values = [1]
i = 0
dirs = ['R', 'U', 'L', 'D']
dirs_i = 0
step = 1
change = False
n = 0
results = {(0, 0) : 1}
position = (0, 0)


def get_sum(pos):
    s = 0
    for i in [-1, 0, 1]:
        for j in [-1, 0, 1]:
            if i != 0 or j != 0:
                if (pos[0] + i, pos[1] + j) in results:
                    s += results[(pos[0] + i, pos[1] + j)]
    return s


while values[i] < input_value:
    direction = dirs[dirs_i]

    if direction == 'R':
        position = (position[0]+1,position[1])
    elif direction == 'L':
        position = (position[0]-1, position[1])
    elif direction == 'U':
        position = (position[0], position[1]+1)
    elif direction == 'D':
        position = (position[0], position[1]-1)
    results[position] = get_sum(position)
    values.append(results[position])

    i += 1
    n += 1

    if n == step:
        dirs_i = (dirs_i+1) % 4
        n = 0
        if change:
            step += 1
            change = False
        else:
            change = True

print(values[i])
