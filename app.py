#!/usr/bin/env python

import asyncio
from classType import reflect

from structx import x
from structx import modulex


async def main():
    reflect.reflect_use_case()

    print(x)
    print(modulex.x)
    async for temp in work():
        print(temp)

    print("main over")


async def work():
    print("work fine")
    for x in range(10):
        yield x
    print("work over")




if __name__ == "__main__":
    asyncio.run(main())
