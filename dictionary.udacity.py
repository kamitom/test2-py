
elements = {"hydrogen": 1, "helium": 2, "carbon": 6}

elements["Phosphorus"] = 15

elements["oxygen"] = 8

print('oxygen' in elements)
print(elements)

find_one_element = elements.get("dilithium")

print(find_one_element is None)
print(find_one_element is not None)

population = {"Shanghai": 17.8, "Istanbul": 13.3,
              "Karachi": 13.0, "Mumbai": 12.5}

# print(elements["silicon"])  # KeyError: 'silicon'
print(elements.get('kryptonite', 'There\'s no such element!'))
