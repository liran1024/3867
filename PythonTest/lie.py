# 序列指元素有序的排列并且通过下标偏移量访问到它一个或多个元素
# 序列分为字符串“abc”，列表[ 0, 'adad'],元组 ( "aaa","ccc")


# 随便输入年份判断生肖星座
chinese_zodiac = "鼠牛虎兔蛇马羊猴鸡狗猪"
# 通过下标输出元素
print(chinese_zodiac[0])
# 通过下标输出多个元素
print(chinese_zodiac[0:4])
# 从后往前输出
print(chinese_zodiac[-1])
# 判断元素是否在序列中 元素 in 序列
print('人' in chinese_zodiac)
print('猪' in chinese_zodiac)

# 两个序列的连接 序列+序列
print(chinese_zodiac + 'wwwwww')
# 重复操作符 *整数
print(chinese_zodiac * 3)



zodiac_name = (u'摩羯座', u'水瓶座', u'双鱼座', u'白羊座', u'金牛座', u'双子座',u'巨蟹座', u'狮子座', u'处女座', u'天秤座',u'天蝎座', u'射手座')
zodiac_days = ((1, 20), (2, 19), (3, 21), (4, 21), (5, 21), (6, 22), (7, 23), (8, 23), (9, 23), (10, 23), (11, 23), (12, 23))

a = (2, 15)
zodiac_day = filter(lambda x: x <= a, zodiac_days)
# print(list(zodiac_day))
zodiac_len = len(list(zodiac_day)) % 12
print(zodiac_len)
print(zodiac_name[zodiac_len])
