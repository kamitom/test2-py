
from typing import Dict


dictest = {0: "tom", 1: "mary", "apple": "🍎", "orange": "🍊", "banana": "🍌"}

print(dictest["apple"])
# print(type(dictest))
print(isinstance(dictest, dict))


def testFn(para1):
    if (isinstance(para1, dict) == True):
        return (para1["banana"])


print(testFn(dictest))
