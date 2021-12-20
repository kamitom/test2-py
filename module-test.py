import random
import names
import tool
import module1
import module2


# print(random.gammavariate(0.01, 1.23))

print(names.get_full_name())

print(tool.AddMe(100, 200))
print(tool.AddMe(names.get_first_name(), names.get_last_name()))

module1.foo()
module2.foo()
