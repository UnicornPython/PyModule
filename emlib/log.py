import logging as log


# 可以通过 basicConfig 来对 logging 进行配置, 这个配置需要在所有的 log 打印日志之前进行调用
# 否则可能会出现各种错误
# 这样配置的 logger 在全局生效(它的名字就是 root), 
log.basicConfig(
    level = log.INFO,  # 日志的级别
    format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s',  # 日志的格式
    filename = "./log/log.txt",  # 输出到文件的文件名称
    filemode = "w"  # 输出到文件的模式(w 代表每次都产生一个新的文件)
)


###########################
# 自定义 logger
###########################
# 自定义 logger(每个logger 都有一个名字, 这个函数可以多次调用, 当名字相同的时候会返回相同的 logger)
# 很多项目中使用 `__name__` 来获取 logger (如果是当前文件则为 `__main__`, 否则为 `{filename}`)

# 新产生的 logger 会继承全局的 basicConfig(), 当需要修改这个自定义的 logger 的时候，需要使用 handler 
logpool = log.getLogger("pool")
# 设置 文件处理 handle 保存到文件
file_handler = log.FileHandler("./log/logpool.log", mode = "w")
# 修改输出的日志格式
file_handler.setFormatter(log.Formatter("%(levelname)s -%(message)s"))
# 添加 handler (可以添加多个, StreamHandler, SocketHandler, 自定义 handler 等)
logpool.addHandler(file_handler)


def use_custom_logger() -> None:
    logpool.warning("This is custom logger, use logpool")



def log_exception() -> None:

    try:
        1 / 0 
    except:
        # 在 异常捕获的时候可以使用 log.exception() 记录到异常的堆栈信息
        logpool.exception("Get exception")



def log_level() -> None: 
    """
    按照日志的级别逐级控制输出内容的级别, 默认情况下，只会打印 warning 以及以上级别的日志
    """
    log.debug("debug")
    log.info("info")
    log.warning("warning")
    log.error("error")
    log.critical("critical")


def main()-> None: 
    log_level()
    use_custom_logger()
    log_exception()


if __name__ == "__main__":
    main()
