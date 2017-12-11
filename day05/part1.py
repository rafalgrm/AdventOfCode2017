with open('input.txt') as f:
    jumps = list(map(int, f.readlines()))
    i = 0
    step_count = 0
    while 0 <= i < len(jumps):
        jumps[i] += 1
        i += jumps[i]-1
        step_count += 1
    print(step_count)