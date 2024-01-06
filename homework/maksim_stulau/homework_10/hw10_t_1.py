"""Создайте универсальный декоратор, который можно будет применить к любой функции.
Декоратор должен делать следующее:
он должен распечатывать слово "finished" после выполнения декорированной функции.
Код, использующий этот декоратор может выглядеть, например, так:

@finish_me
def example(text):
    print(text)

example('print me')
В результате работы будет такое:
print me
finished"""


def uni_dec(func):
    def wrapper(*args):
        func(*args)
        print("finished")
    return wrapper


@uni_dec
def calc():
    print("Hello")


@uni_dec
def calc1(x):
    print(x * 2)


calc()
calc1(3)
