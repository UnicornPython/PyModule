#!/python

import time 

"""
#####################################################################################################
1. 基础版本, 串行执行过程
#####################################################################################################
"""

def play( )-> None: 
    print("enter play")
    for _ in range(5):
        time.sleep(1) # wait complete thinking
        for _ in range(1000): # wang think, use CPU
            pass


def version1() -> None:
    print("enter main")
    start = time.time()
    for _ in range(10):
        play()
    print(f"total time: {time.time() - start} seconds")

"""
##################################################################################################### 
"""


"""
##################################################################################################### 
2. asyncio 

1. asyncio.run()  内部会构建一个 EventLoop 并立即启动 executor 执行 task 
2. 但是开始的时候 eventloop 中是没有 task 的, 因此需要传入一个 coroutine作为参数
3. run 函数会为这个 coroutine 创建 task 并运行它
4. 普通函数加上 async 关键字就变成了一个 coroutine, 在调用这些函数的时候就不会立即执行了，而是返回一个
   代表这个函数的 coroutine 实例. 
5. 当在某个作用域中使用 event loop, 后续我们需要向其中添加 task, 而不是每次都使用 run 方法创建新的
   asyncio.create_task() 即可向 event loop 中提交任务
6. 当使用多个子协程的时候，主函数是不能结束的，否则程序不会等所有的子协程执行结束才停止，未执行完成
   的协程不会继续执行, 可能直接被清理了
7. create_task 会返回任务本身, 这些任务需要 使用 await 来等待完成
   await 的返回值就是协程 coroutine 的返回值
8. sleep 函数的特殊性，虽然协程是异步的，但是在 python 中还是单线程程序，虽然 sleep 不会占用 CPU 
   但是他会阻塞程序不会返回，直到 sleep 时间满足条件或被打断
   
9. 在异步 IO 中，所有的 API 应该尽可能的都使用他们的异步版本，否则都有可能会降低吞吐

10. 由于创建一个 coroutine，然后 await 去等待他执行，这样的代码如此常见，因此可以简化
    sp = asyncio.sleep(1)
    await asyncio.create_task(sp)
    > 可以简化为如下的写法，python 解释器会自动创建 task
    await asyncio.sleep(1)

"""

import asyncio


async def async_play() -> None: 
    print("enter play")
    for _ in range(5):
        # time.sleep(1) # wait complete thinking
        # 这里将 sleep 也做成一个 coroutine 任务
        # 这样在 await 的时候就可以执行其他已经准备好的 coroutine

        # sp = asyncio.sleep(1)
        # await asyncio.create_task(sp)

        # 简化为

        # await asyncio.sleep(1)

        # 当可以阻塞函数没有异步版本的时候，可以使用多线程的技术来解决
        # 这里会返回一个 coroutine, 这个任务实际上被交给了一个内置线程池来执行, 效果与协程类似，
        # 
        # 但是 python 中存在的 gil 锁，导致同一个时刻在执行的只能是一个线程
        # 所以在大部分时候，python 程序使用多线程并不能提高程序的效率，还要考虑线程同步的问题
        # 需要慎用
        await asyncio.to_thread(time.sleep, 1)

        for _ in range(1000): # wang think, use CPU
            pass

async def manager() -> None:
    print("enter main")
    start = time.time()
    tasks = []
    for _ in range(10):
        # 使用 create_task() 来提交一个 coroutinue
        tasks.append(asyncio.create_task(async_play()))

    # 这里不必关心 await 的是哪一个，因为所有的都在执行
    # 只是阻塞等待结果, 所有任务执行的总时间一定是最长世间的那一个的耗时
    # for t in tasks:
    #     await t
    # 可简化为如下，返回值为参数中所有 coroutine 的返回值组成的列表
    await asyncio.gather(*tasks)

    print(f"total time: {time.time() - start} seconds")


def version2() -> None:
    asyncio.run(manager())



"""
##################################################################################################### 
3. 其他的函数
asyncio.Event() 构建时间通知的方式来控制异步任务的执行

"""

async def async_play_with_init(init_event) -> None:
    # 等待初始化任务的完成之后才开始当前任务
    # 事件的等待是异步操作，
    await init_event.wait()
    print("enter play")
    for _ in range(5):
       await asyncio.sleep(1)
       for _ in range(1000): # wang think, use CPU
            pass


async def async_init()  -> None:
    print("enter version3")
    tasks = []
    init_event = asyncio.Event()

    for _ in range(10):
        # 使用 create_task() 来提交一个 coroutinue
        tasks.append(asyncio.create_task(async_play_with_init(init_event)))

    await asyncio.sleep(1)
    print("init Done")
    # 事件的触发是同步执行的
    init_event.set()
    await asyncio.gather(*tasks)


def version3() -> None: 
    asyncio.run(async_init())

"""
#####################################################################################################
4. asyncio 中的其他同步机制中的异步版本

> ------ lock -----------
lock = asyncio.Lock()
await lock.acquire()
try: 
    ...
finally:
    lock.release()

> ------Semaphore--------
sem = asyncio.Semaphore(10)
await sem..acquire()
try:
    ...
finally:
    sem.release()

> ----- Barrier ---------
barrier = asyncio.Barrier(2)
await barrier.wait()

barrier = asyncio.Barrier(2)
async with barrier:
    ....

> -----condition---------
cond = asyncio.Condition()
await = cond.acquire()
try:
    await cond.wait()
finally:
    cond.release()

"""


def main() ->  None: 
    # version1()
    # version2()
    version3()

if __name__ == "__main__":
    main()

