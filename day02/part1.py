with open('input.txt') as f:
    print(sum(max(numbers)-min(numbers) for numbers in [list(map(int, line.split())) for line in f.readlines()]))
