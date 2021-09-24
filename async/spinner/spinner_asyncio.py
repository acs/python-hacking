import asyncio
import itertools
import sys
import time


async def spin(msg: str):
    write, flush = sys.stdout.write, sys.stdout.flush
    for char in itertools.cycle('|/-\\'):
        status = char + ' ' + msg
        write(status)
        flush()
        time.sleep(.1)
        write('\x08' * len(status))
    write(' ' * len(status + '\x08' * len(status)))


async def slow_io_function():
    # pretend waiting for a long time for I/O
    time.sleep(3)  # GIL is released in time function
    return 42


def supervisor():
    spinner = asyncio.create_task(spin('thinking!'))
    print(f'Spinner object: {spinner}')
    result = yield from slow_io_function()
    spinner.cancel()
    return result


def main():
    loop = asyncio.get_event_loop()
    result = loop.run_until_complete(supervisor())
    loop.close()
    print(f'Answer: {result}')


if __name__ == '__main__':
    main()

