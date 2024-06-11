


import logging
from logging.handlers import RotatingFileHandler
# 当实例化的时候，我希望你直接去写数据


class Logger:
    def __init__(self, name, log_file, level=logging.DEBUG):
        # 1. 实例化日志对象，同时设置级别
        self.logger = logging.getLogger(name)
        self.logger.setLevel(level)

        # 2. 设置日志的格式
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

        # 3. 写入的地方：控制器、文件
        # 创建控制台处理器
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)
        self.logger.addHandler(console_handler)

        # 文件
        file_handler = RotatingFileHandler(log_file, maxBytes=1048576, backupCount=3)
        file_handler.setFormatter(formatter)  # 设置格式
        self.logger.addHandler(file_handler)  # 添加到对应的处理器中


if __name__ == '__main__':
    log = Logger("单列前面的文字", "..\log\log.log")
    log.logger.debug("XXXXXX1")
    log.logger.info("XXXXXX2")
    log.logger.warning("XXXXXX3")
    log.logger.error("XXXXXX4")
    log.logger.critical("XXXXXX5")
