with open('input.txt') as f:
    phrases = f.readlines()

    res = 0
    for phrase in phrases:
        tokens = phrase.split()
        if len(tokens) == len(set(tokens)):
            res += 1
    print(res)
