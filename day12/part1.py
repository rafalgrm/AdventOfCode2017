with open('input.txt') as f:
    connections = {}
    for line in f.readlines():
        left, right = line.split(' <-> ')
        left_int = int(left)
        right_list = map(int, right.strip().split(', '))

        connections[left_int] = set(right_list)

        for r in right_list:
            if r in connections:
                connections[r].add(left_int)
            else:
                connections[r] = {left_int}

    # finding for id = 0
    to_look = [0]
    res = {0}

    while len(to_look) > 0:
        i = to_look.pop()
        for c in connections[i]:
            if c not in res:
                res.add(c)
                to_look.append(c)

    print(len(res))
