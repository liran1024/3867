# 读取人物名称
# f = open('name.txt', 'r', encoding='UTF-8')
# data = f.read()
# print(data.split('|'))
# 读取兵器名称
# 取奇数行
# f2 = open('weapon.txt', encoding='UTF-8')
# i = 1
# for line in f2.readlines():
#     if i % 2 == 1:
#         print(line.strip('\n'))
#     i += 1
# 读取三国演义
# f3 = open('sanguo_utf8.txt', encoding='UTF-8')
# data = f3.read().replace('\n', '')
# print(data)

# 封装函数
# def 函数名():
#     return
# 函数调用  函数名()


# 统计人物出现的次数

import re

def find_name( hero):
    with open('sanguo_utf8.txt', encoding='UTF-8') as f:
        data = f.read().replace('\n', '')
        name_num = re.findall(hero, data)
        print('%s 出现了 %s' % (hero, len(name_num)))
    return len(name_num)

name_dict = {}

with open('name.txt', encoding='UTF-8') as f:
    for line in f:
        names = line.split('|')
        for n in names:
            name_num = find_name(n)
            name_dict[n] = name_num

print(name_dict)

name_data = sorted(name_dict.items(), key=lambda item: item[1], reverse=True)
print(name_data)
