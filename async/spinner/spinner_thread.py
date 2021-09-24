import itertools
import sys
import threading
import time


class Signal:
    go = True


def spin(msg: str, signal: Signal):
    write, flush = sys.stdout.write, sys.stdout.flush
    for char in itertools.cycle('|/-\\'):
        status = char + ' ' + msg
        write(status)
        flush()
        time.sleep(.1)
        write('\x08' * len(status))
        if not signal.go:
            break
    write(' ' * len(status + '\x08' * len(status)))


def slow_io_function():
    # pretend waiting for a long time for I/O
    time.sleep(3)  # GIL is released in time function
    return 42


def supervisor():
    signal = Signal()
    spinner = threading.Thread(target=spin, args=('thinking', signal))
    print(f'Spinner object: {spinner}')
    spinner.start()
    result = slow_io_function()
    signal.go = False
    spinner.join()
    return result


def main():
    result = supervisor()
    print(f'Answer: {result}')


if __name__ == '__main__':
    main()

