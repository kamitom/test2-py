
# define a set
set_str = {'usa', 'tw', 'japan', 'russia',
           'italy', 'germany', 'japan', 'tw', 'usa'}

print(set(set_str))  # 去除重複
print(len(set(set_str)))

set_str.add('france')
set_str.add('korea')
print('new set_str: ', set_str)
set_str.pop()  # remove a random element
print('new set_str: ', set_str)
print('korea' not in set_str)
