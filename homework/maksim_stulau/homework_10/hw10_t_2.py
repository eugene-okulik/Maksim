"""Создайте универсальный декоратор, который будет управлять тем,
сколько раз запускается декорируемая функция
Код, использующий этот декоратор может выглядеть, например, так:

@repeat_me
def example(text):
    print(text)

example('print me', count=2)
В результате работы будет такое:
print me
print me
Если есть время и желание погуглить и повозиться,
то можно попробовать создать декоратор, который сможет обработать такой код:

@repeat_me(count=2)
def example(text):
    print(text)

example('print me')"""


def repeat(times):
    def decorator(func):
        def wrapper(*args):
            for x in range(times):
                result = func(*args)
            return result
        return wrapper
    return decorator


@repeat(times=3)
def say_hello(name):
    print(f"Hello, {name}!")


say_hello("John")
