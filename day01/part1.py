with open('input1.txt', 'r') as f:
    digits = [int(digit) for digit in f.readline()]
    n = len(digits)
    print(sum([(number if number == digits[(i+1) % n] else 0) for i, number in enumerate(digits)]))
