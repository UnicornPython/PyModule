#!/usr/bin/env python

import collections
import heapq
import itertools
import random
import time
from time import sleep

"""
>>- ------------------------------------
   > 模仿事件循环机制驱动任务执行

>>-
"""


class EventLoop:
    def __init__(self):
        self._ready = collections.deque()
        self._scheduled = []
        self._stopping = False

    def call_soon(self, callback, *args):
        self._ready.append((callback, args))

    def call_later(self, delay, callback, *args):
        t = time.time() + delay
        heapq.heappush(self._scheduled, (t, callback, args))

    def stop(self):
        self._stopping = True

    def run_forever(self):
        while True:
            self.run_one()
            if self._stopping:
                break

    def run_one(self):
        # 取出到时间的任务到就绪队列
        now = time.time()
        if self._scheduled:
            if self._scheduled[0][0] < now:
                _, cb, args = heapq.heappop(self._scheduled)
                self._ready.append((cb, args))

        # 执行就绪队列中的任务
        num = len(self._ready)
        for i in range(num):
            cb, args = self._ready.popleft()
            cb(*args)


class Awaitable:
    pass


task_id_iterator = itertools.count(1)


class Task:
    def __init__(self, coro):
        self.coro = coro
        self._done = False
        self._result = None
        self._id = f"Task-${next(task_id_iterator)}"

    def run(self):
        print(f"----------------${self._id}---------------")
        if not self._done:
            try:
                x = self.coro.send(None)
            except StopIteration as e:
                self._result = e.value
                self._done = True
            else:
                assert isinstance(x, Awaitable)
                loop.call_later(x.value, self.run)
        else:
            print("task is done")
        print("-------------------------------------------")


async def one_task():
    pass


async def small_step():
    print("         休息以下，马上回来")
    t1 = time.time()
    sleep_time = random.random()
    await Awaitable(sleep_time)
    assert time.time() - t1 > 2, "睡眠不足！！"
    print("             努力工作中!!")
    return 123


async def big_step():
    # ... other step
    print(f"     begin samll step: ... ")


def main():
    loop = EventLoop()
    t = Task(one_task())
    loop.call_soon(t.run)
    loop.call_later(2, t.run)
    loop.call_later(2.1, loop.stop)
    loop.run_forever()


if __name__ == "__main__":
    main()
