from inspect import getgeneratorstate


def simple_generator():
    for i in range(1, 10):
        yield i


def simple_coroutine():
    print('-> coroutine started')
    x: int = yield  # the coroutine can receive a value
    print(f'-> coroutine received: {x}')


def simple_coroutine2(a: int):
    print(f'-> Started: a = {a}')
    b: int = yield a
    print(f'-> Received: b = {b}')
    c: int = yield a + b
    print(f'-> Received: c = {c}')
    yield a + b + c


if __name__ == '__main__':

    my_coroutine2 = simple_coroutine2(10)
    next(my_coroutine2)
    print(my_coroutine2.send(11))
    print(my_coroutine2.send(12))

    my_generator = simple_generator()
    for item in my_generator:
        print(f'generator value {item}')

    my_coroutine = simple_coroutine()
    print(f'coroutine state {getgeneratorstate(my_coroutine)}')
    next(my_coroutine)
    print(f'coroutine state {getgeneratorstate(my_coroutine)}')
    my_coroutine.send(42)
