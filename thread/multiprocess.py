from itertools import starmap
import multiprocessing as mp
import time

""" 
多进程运行
> 1
"""
# 计算pi 值的公式
# pi = 4(1 - 1/3 + 1/5 - 1/7 + 1/9 - 1/11 + ...)
def calculate_pi(start: int, end: int) -> float:
    result = 0.0
    positive = True if start % 2 == 0 else False
    for i in range(start, end):
        tmp = 1.0 / (float(i * 2) + 1.0)
        if positive:
            result += tmp
        else:
            result -= tmp
        positive = not positive

    return result * 4.0


iter_rond = 100_000_000


##########################################################################################
def single_process() -> float:
    return calculate_pi(0, iter_rond)


def test_single() -> None:
    start_time = time.time()
    print(single_process())
    print(f"single_process: {time.time() - start_time} seconds")


##########################################################################################
# 多进程版本
# process 并没有提供获取子进程运算结果的方式，需要通过其他的方式来获取不同子进程的结果
#    - 共享内存
#    - 通过中间数据结果，队列等


def multi_process() -> float:
    # 由于python 默认的除法得到的是浮点数, 这里直接使用 `//` 取整
    step = iter_rond // 8
    procs = []
    for start in range(0, iter_rond, step):
        # 共享内存(接受一个参数表示共享内存中存储的数据类型)
        result = mp.Value("d")
        # target 是在子进程中运行的, 他们的运行地址空间不同
        # multiprocessing 可能会根据不同的调用 api 对参数使用 pickle 进行序列化和反序列化操作
        # 基本类型已经实现了这样的序列化, 传递一些自定义类型的参数的时候需要注意
        p = mp.Process( target=calculate_pi_wrapper, args=[result, start, start + step])
        # 启动进程
        p.start()
        procs.append((p, result))

    pi = 0.0
    for p, v in procs:
        p.join()
        pi += v.value
    return pi


def calculate_pi_wrapper(result, start: int, end: int):
    result.value = calculate_pi(start, end)


def test_multiple() -> None:
    start_time = time.time()
    print(multi_process())
    print(f"multi_process: {time.time() - start_time} seconds")


##########################################################################################
# 简化的多进程版本
# 使用进程池 Pool 类(帮助我们管理进程的创建，执行和返回值的获取)

def multi_process_pool() -> float:
    params = []
    step = iter_rond // 8
    for start in (0, iter_rond, step):
        params.append((start, start + step))
    # Pool 的参数就是需要启动的进程的数量
    with mp.Pool(8) as pool:
        # starmap() 的第二个参数是一个二维参数列表，内层为每次调用 calculate_pi 的参数
        # 外层为多次调用 calculate_pi 
        # starmap 会返回调用后的结果，以列表的形式返回
        result = pool.starmap(calculate_pi, params)

    return sum(result)


def test_multiple_pool() -> None:
    start_time = time.time()
    print(multi_process_pool())
    print(f"multi_process_pool: {time.time() - start_time} seconds")


def main() -> None:
    #  test_single()
    test_multiple()
    test_multiple_pool()


if __name__ == "__main__":
    main()
