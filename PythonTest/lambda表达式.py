# lambda将简单的函数 简易化

# 例如
def true():
    return True


true()

lambda: True


def add(x, y):
    return x + y


print(add(3, 5))

a = lambda x, y: x + y

print(a(3, 8))
