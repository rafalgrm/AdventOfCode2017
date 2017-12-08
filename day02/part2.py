with open('input.txt') as f:
    numbers = [list(map(int, line.split())) for line in f.readlines()]
    s = 0
    for line in numbers:
        for i, number in enumerate(line):
            for j in range(i+1, len(line)):
                if max((number, line[j])) % min((number, line[j])) == 0:
                    s += max((number, line[j])) / min((number, line[j]))
    print(s)
