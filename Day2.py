# Data Types

# String
from io import TextIOWrapper


print("Hello"[4])

# Int
print(123_456_786)

# float
print(123_456.789)

print(len("123_456"))
# print(len(100))

vlan_ids = 2**12
print('vlan id, ', vlan_ids)

two_digit_number = input('Type a two digit number: ')
first_number = two_digit_number[0]
second_number = two_digit_number[1]

print('result ', int(first_number)*int(second_number))
