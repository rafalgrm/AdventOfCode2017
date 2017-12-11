with open('input.txt') as f:
    phrases = f.readlines()

    res = 0
    for phrase in phrases:
        tokens = phrase.split()
        if len(tokens) == len({tuple(sorted(word)) for word in tokens}):
            res += 1
    print(res)
