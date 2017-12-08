import math

input_value = 277678

guess = int(math.sqrt(input_value))
if guess % 2 == 0:
    guess += 1
if math.sqrt(input_value) > guess:
    guess += 1

square_no = guess
n = square_no**2

additional_steps = None

if input_value > n-square_no+1:
    additional_steps = input_value - (n - square_no // 2)
elif input_value > n-2*square_no+2:
    additional_steps = input_value - (n - 3 * square_no // 2 + 1)
elif input_value > n-3*square_no+3:
    additional_steps = input_value - (n - 5 * square_no // 2 + 2)
elif input_value > n-4*square_no+4:
    additional_steps = input_value - (n - 7 * square_no // 2 + 3)

print(square_no//2+abs(additional_steps))
