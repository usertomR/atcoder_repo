N = int(input())

change_to_hex = {10 : "A", 11 : "B", 12 : "C", 13 : "D", 14 : "E", 15 : "F"}

a_digit = int(N / 16)
if a_digit in change_to_hex:
  a_digit = change_to_hex[a_digit]

two_digits = N % 16
if two_digits in change_to_hex:
  two_digits = change_to_hex[two_digits]

print(str(a_digit) + str(two_digits))