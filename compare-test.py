"""
比較運算與邏輯運算

"""

flag1 = 1 == 1
flag2 = 2 > 3

flag3 = flag1 and flag2

flag4 = not (1 != 2)

print("flag3 = ", flag3)
print("flag4 = ", flag4)
# print('%d and %d = %d' % (flag1, flag2, flag3))

ff = float(input('請輸入華氏溫度: '))
cc = (ff-32) / 1.8
# print(ff)
print('%.1f華氏溫度 = %.1f攝氏溫度' % (ff, cc))
