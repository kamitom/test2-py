import random
import names
import tool


# print(random.gammavariate(0.01, 1.23))

print(names.get_full_name())

print(tool.AddMe(100, 200))
print(tool.AddMe(names.get_first_name(), names.get_last_name()))
