number = input()
number_str = str(number)
odd_sum = 0
even_sum = 0

for digit in number_str:
    digit_int = int(digit)
    if digit_int % 2 == 0:
        even_sum += digit_int
    else:
        odd_sum += digit_int

if odd_sum == even_sum:
    print("True")
else:
    print("False")