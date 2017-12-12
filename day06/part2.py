with open('input.txt') as f:
    banks = list(map(int, f.readline().strip().split('\t')))
    res = 0

    history_set = {}

    while tuple(banks) not in history_set:
        history_set[tuple(banks)] = res

        max_value = max(banks)
        max_index = banks.index(max_value)

        iters = banks[max_index]
        banks[max_index] = 0

        while iters:
            banks[(max_index+iters)%len(banks)] += 1
            iters -= 1

        res += 1

    print(res-history_set[tuple(banks)])