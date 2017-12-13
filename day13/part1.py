with open('input.txt') as f:
    step = 0
    res = 0
    for layer in f.readlines():
        i, depth = map(int, layer.split(': '))
        if i == 0 or i % ((depth-1)*2) == 0:
            res += i*depth
    print(res)
