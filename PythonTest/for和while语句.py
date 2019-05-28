# for语句和while语句都用于执行多次循环
# while 表达式：
#  表达式为真时将持续进行 也可以用break停止
chinese_zodiac = "猴鸡狗猪鼠牛虎兔龙蛇马羊"
# 遍历生肖
for zs in chinese_zodiac:
    print(zs)
# 数字遍历
for i in range(1, 13):
    print(i)
# 字符串替换 要替换的位置用%加上数据类型
for year in range(2000, 2019):
    a = year % 12
    # print(a)
    # print(chinese_zodiac[11])
    print('%s年的生肖是%s' % (year, chinese_zodiac[a]))
# break 和 continue
# break结束当前循环
num = 0
while True:
    num = num + 1
    if num > 10:
       break
    print(num)

# continue跳出这次循环
# item = 0
# while True:
#     item += 1
#     if item == 10:
#         continue
#     print(item)
