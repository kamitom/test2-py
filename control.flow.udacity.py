phone_balance = 4
bank_balance = 100

if phone_balance < 5:
    phone_balance += 10
    bank_balance -= 10

print(phone_balance, bank_balance)

# n = input('Number is')
n = int(input("n = "))

if n % 2 == 0:
    print('Number ' + str(n) + ' is even')
else:
    print('Number ' + str(n) + ' is odd')

# print(n)
season = str(input('season = '))

if season == 'spring':
    print('spring')
elif season == 'summer':
    print('summer')
elif season == 'fall':
    print('fall')
elif season == 'winter':
    print('Stay indoors!')
else:
    print('unrecognized season!')
