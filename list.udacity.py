import statistics


lst_of_random_things = [1, 3.4, 'a string', True]
months = ['JAN', 'FEB', 'MAR', 'APR', 'MAY', 'JUN',
          'JUL', 'AUG', 'SEP', 'OCT', 'NOV', 'DEC']

print(len(lst_of_random_things))
print(lst_of_random_things[-2])

# slicing
print(months[6:9])
print(months[6:])
print(months[:9])

print(lst_of_random_things[1:2])

name = 'tom'
student = name
name = 'jordan'

print(name)
print(student)

scores = [103, 123, 592, 118, 65, 39, 203, 529]

grades = scores
scores[3] = 99.9

print('scores: ', str(scores))
print('grades: ', str(grades))

scores1 = [103, 123, 592, 118, 65, 39, 203, 529]
print('scores1 max: ', max(scores1))

print('sorted: ', sorted(scores1, reverse=True))
print('original sort: ', scores1)


# 取中位數
numbers = [1, 2, 3]
print('numbers 中位數', statistics.median(numbers))
print('scores1 中位數', statistics.median(scores1))
