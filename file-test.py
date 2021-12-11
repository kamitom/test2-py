
from os import read, write
import random
import names


# open('~/Downloads/pytest.txt', mode=write)
fileContent = open("pytest.txt", mode="r")
fileContent2 = open("pytest2.txt", mode="a")

# print(fileContent.buffer.readlines.__str__)

# print(fileContent.read())  # read 全部
i = 1
for line in fileContent:
    print(str(i) + ": " + line)
    i += 1

# contents1 = fileContent.readline()
# testList = fileContent.readlines()
# print(contents1)  # 只read第一行
# print(testList[2])  # read 第3行

fileContent2.write("東京您好\n")
fileContent2.write("大阪您好\n")
fileContent2.write("名古屋您好\n")


with open("pytest3.txt", mode="a") as fileContent3:
    fileContent3.write(str(random.randint(1, 999)) + ": " +
                       names.get_full_name() + " 你好\n")
    fileContent3.write(str(random.randint(1, 999)) + ": " +
                       names.get_full_name() + " 你好\n")
    fileContent3.write(str(random.randint(1, 999)) + ": " +
                       names.get_full_name() + " 你好\n")
    fileContent3.write(str(random.randint(1, 999)) + ": " +
                       names.get_full_name() + " 你好\n")

# fileContent2.read()

fileContent.close()
fileContent2.close()
