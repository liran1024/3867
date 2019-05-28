# 闭包是由函数及其相关的引用环境组合而成的实体(即：闭包=函数+引用环境)

# 例如 让两个变量相加
# 普通函数
def func():
    a = 2
    b = 3
    return a + b


# 闭包函数
def sum(a):
    def add(b):
        return a + b

    return add


# add 函数名称或者函数引用
# add() 函数的调用
# 调用

line1 = func()
line2 = sum(1)

print(type(line1))
print(type(line2))

print(line2(3))


# 函数计数器每次调用 加一

def country():
    a = 0

    def add():
        # nonlocal 用于声明，修改嵌套作用域
        nonlocal a
        a += 1
        return a

    return add


num = country()
print(num())

# 同上个列子 扩展化 a不设定固定值

def country2(FIRST=0):
    a = FIRST

    def add2():
        # nonlocal 用于声明，修改嵌套作用域
        nonlocal a
        a += 1
        return a

    return add2

num2 = country2(10)

print(num2())