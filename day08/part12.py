import operator
curr_max = []

ops = {'>': (lambda x, y: x > y),
       '<': (lambda x, y: x < y),
       '>=': (lambda x, y: x >= y),
       '<=': (lambda x, y: x <= y),
       '==': (lambda x, y: x == y),
       '!=': (lambda x, y: x != y),
       'inc': (lambda x, y: x + y),
       'dec': (lambda x, y: x - y)}

with open('input.txt') as f:
    regs = {}
    for line in f.readlines():
        ins = line.strip().split(' ')
        reg = ins[0]
        pol = ins[1]
        num = ins[2]
        reg_con = ins[4]
        con = ins[5]
        num_con = ins[6]

        if reg_con not in regs: regs[reg_con] = 0
        if reg not in regs: regs[reg] = 0

        if ops[con](regs[reg_con],int(num_con)):
            regs[reg] = ops[pol](regs[reg], int(num))

        curr_max.append(max(regs.items(), key=operator.itemgetter(1))[1])

    print(max(regs.items(), key=operator.itemgetter(1))[1])
    print(max(curr_max))
