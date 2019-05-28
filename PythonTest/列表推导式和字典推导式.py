# 列表
# 假设求 1-10 的所有偶数的平方
alist = []
for i in range(1, 11):
    if i % 2 == 0:
        alist.append(i*i)
print(alist)
# 列表的推导式
blist = [i*i for i in range(1, 11) if(i % 2) == 0]
print(blist)

# 字典
chinese_zodiac = "猴鸡狗猪鼠牛虎兔龙蛇马羊"
c_zodiac = {}
# 初始化赋值
for item in chinese_zodiac:
    c_zodiac[item] = 0
# 字典推导式
c_zodiac = {item: 0 for item in chinese_zodiac}
print(c_zodiac)
