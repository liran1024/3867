# 内置函数包括 filter map reduce zip

# filter用于过滤序列

# filter(function, iterable)

a = list(filter(lambda x: x > 2, [1, 2, 3, 4, 5, 6, 7]))
a2 = list(filter(lambda x: x > 2, (1, 2, 3, 4, 5)))
print(a)
print(a2)

# map会根据提供的函数对指定序列做映射。

# map(fuc, *iterable)

b = list(map(lambda x: x + 2, [1, 2, 3, 4, 5, 6, 7]))
print(b)

b2 = list(map(lambda x, y: x + y, [1, 2, 3], [4, 5, 6]))
print(b2)

from functools import reduce

# reduce 函数会对参数序列中元素进行累积。
# reduce(function, iterable[, initializer])

c = reduce(lambda x, y: x + y, [1, 2, 3, 4])
c2 = reduce(lambda x, y: x + y, [1, 2, 3, 4], 3)
print(c)
print(c2)

# zip函数用于将可迭代的对象作为参数，将对象中对应的元素打包成一个个元组，然后返回由这些元组组成的对象

# zip([iterable, ...])
# zip元素个数以最短的列表为主
d = list(zip([1, 2, 3, 4], [4, 3, 2, 1]))
print(d)
# 利用zip转换key和value
al = {'a': 'aa', 'b': 'bb'}
ac = zip(al.values(), al.keys())
print(dict(ac))
