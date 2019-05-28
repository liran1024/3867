# 映射类型：字典 dict
# 字典包含哈希值和指向的对象 {'哈希值':对象}

# 建立一个空对象
dict1 = {}
print(type(dict1))
# 如何给字典增加值
dict2 = {'x': 1, 'y': 2}

dict2['z'] = 3
print(dict2)

# 统计生肖和星座
chinese_zodiac = "猴鸡狗猪鼠牛虎兔龙蛇马羊"
zodiac_name = (u'摩羯座', u'水瓶座', u'双鱼座', u'白羊座', u'金牛座', u'双子座', u'巨蟹座', u'狮子座', u'处女座', u'天秤座', u'天蝎座', u'射手座')
zodiac_days = (
    (1, 20), (2, 19), (3, 21), (4, 21), (5, 21), (6, 22), (7, 23), (8, 23), (9, 23), (10, 23), (11, 23), (12, 23)
)
# 创建统计生肖和星座的字典
c_zodiac = {}
zodiac = {}
# 初始化赋值
for item in chinese_zodiac:
    c_zodiac[item] = 0
for item in zodiac_name:
    zodiac[item] = 0

# 记录每次用户的星座和年份
while True:
    # int转化成整数
    int_year = int(input('请输入年份：'))
    int_month = int(input('请输入月份：'))
    int_day = int(input('请输入月份：'))

    n = 0
    while zodiac_days[n] < (int_month, int_day):
        if int_month == 12 and int_day > 23:
            break
        n += 1
    print(zodiac_name[n])
    print('%s年的生肖是%s' % (int_year, chinese_zodiac[int_year % 12]))
    c_zodiac[chinese_zodiac[int_year % 12]] += 1
    zodiac[zodiac_name[n]] += 1
    # 打印字典
    for item in c_zodiac.keys():
        print('%s 有 %d 个' % (item, c_zodiac[item]))
    for item in zodiac.keys():
        print('%s 有 %d 个' % (item, zodiac[item]))
