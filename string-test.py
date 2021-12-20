s1 = 'hello, tom'
s2 = "htllo, lucas"

# 3個單引號, 或3個爽引號, 可以折行
s3 = """
hello, 
馮韋元!
"""

print(s1, s2, s3, end='')
# print(s1, s2, s3)

s11 = "hello " * 3
s12 = "world"
s11 += s12
print(s11)

print("ll" in s11)
print("test" in s11)
print(s11.capitalize())
print(s11.title())
