with open('input.txt') as f:
    layers = f.readlines()
    d = 0
    while True:
        res = 0
        for layer in layers:
            i, depth = map(int, layer.split(': '))
            if i+d == 0 or (i+d) % ((depth-1)*2) == 0:
                break
        else:
            print(d)
            break
        d += 1
