import asyncio
import itertools
import sys
import time


async def spin(msg: str):
    for char in itertools.cycle('|/-\\'):
        status = f'\r{char} {msg}'
        print(status, flush=True, end='')
        try:
            await asyncio.sleep(.1)
        except asyncio.CancelledError:
            break
    blanks = ' ' * len(status)
    print(f'\r{blanks}\r', end='')


async def slow_io_function():
    # pretend waiting for a long time for I/O
    await asyncio.sleep(3)  # GIL is released in time function
    return 42


async def supervisor() -> int:
    spinner = asyncio.create_task(spin('thinking!'))
    print(f'Spinner object: {spinner}')
    result = await slow_io_function()
    spinner.cancel()
    return result


def main() -> None:
    result = asyncio.run(supervisor())
    print(f'Answer: {result}')


if __name__ == '__main__':
    main()

