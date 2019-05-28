# open()打开文件
# read()输入
# readline()输入一行
# seek()文件内移动
# write()输入
# close()关闭
# tell()记录文件操作的指针
# seek()操作指针 第一个参数是相对位置 第二个参数 0 为从开头开始偏移 1 是从当前 2是从结尾

# open()有多个参数
# 练习写入一个文件
file = open('name.txt', 'w')
file.write('hello word')
file.close()
# # 读取文件
file2 = open('name.txt')
print(file2.read())
file2.close()
#
# # 文件增加
file3 = open('name.txt', 'a')
file3.write('gogogo')
file3.close()

# 文件读取一行(默认只读取一行)
file4 = open('name.txt', 'r', encoding='UTF-8')
print(file4.readline())
file4.close()

# 逐行读取
file5 = open('name.txt', 'r', encoding='UTF-8')
for line in file5.readlines():
    print(line)



