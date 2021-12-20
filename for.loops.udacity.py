cities = ['new york city', 'paris', 'tokyo', 'san francisco', 'mountain view']

capitalized_city = []

for single_city in cities:
    # print(single_city.title())
    capitalized_city.append(single_city.title())

print(capitalized_city)

for index in range(len(cities)):
    cities[index] = cities[index].title()
    print(cities[index])

names = ["Joey Tribbiani", "Monica Geller", "Chandler Bing", "Phoebe Buffay"]
names1 = ["Joey Tribbiani", "Monica Geller", "Chandler Bing", "Phoebe Buffay"]
usernames = []

for name in range(len(names)):
    names[name] = names[name].lower().replace(' ', '_')
    usernames.append(names[name])

for name1 in names1:
    name1 = name1.lower().replace(' ', '_')
    print(name1)


print(names1)

print(usernames)

items = ['first string', 'second string']
html_str = "<ul>\n"  # "\ n" is the character that marks the end of the line, it does
# the characters that are after it in html_str are on the next line

# write your code here
for ul in range(len(items)):
    # html_str += '<li>' + items[ul] + '</li>\n'
    html_str += '<li>{}</li>\n'.format(ul)

html_str += '</ul>'

print(html_str)
