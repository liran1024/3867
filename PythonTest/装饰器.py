import time


# print(time.time()) #从1970年1月1日到现在运行多少秒
# print(time.sleep(2))# 停顿多少秒
# 例子 假如记录函数运行多少秒
def i_can_sleep():
    time.sleep(3)


start_time = time.time()
i_can_sleep()
stop_time = time.time()
print('函数运行了 %s 秒' % (stop_time - start_time))


# 装饰器就是用于拓展原来函数功能的一种函数，
# 这个函数的特殊之处在于它的返回值也是一个函数，
# 使用python装饰器的好处就是在不用更改原函数的代码前提下给函数增加新的功能。
def timmer(func):
    def wrapper():
        start_time1 = time.time()
        func()
        stop_time1 = time.time()
        print('第二次函数运行了 %s 秒' % (stop_time1 - start_time1))

    return wrapper


@timmer
def i_can_sleep_one():
    time.sleep(3)


i_can_sleep_one()


# 例子 给函数传参 以及给修饰器传参
# 举例对两个参数进行运算
def new_tips(argv):
    def tips(func):
        # 函数需要传参 装饰器内部函数可以同接受
        def nei(a, b):
            print('提示开始参数为 %s 函数名为 %s' % (argv, func.__name__))
            func(a, b)
            print('提示结束')

        return nei

    return tips


@new_tips('2')
def addnum(a, b):
    print(a + b)


print(addnum(1, 2))