#!/usr/bin/env python3

# From https://realpython.com/async-io-python/
import asyncio


async def count():
    print("One")
    await asyncio.sleep(1)
    print("Two")


async def main():
    for i in range(0,10):
        asyncio.create_task(count())
    await asyncio.gather(count(), count(), count())
    await asyncio.gather(count(), count(), count())


if __name__ == '__main__':
    import time
    s = time.perf_counter()
    asyncio.run(main())
    pass
