import logging

from loguru import logger


class InterceptHandler(logging.Handler):  # pragma: no cover
    def emit(self, record):
        # 获取对应的 Loguru 等级
        try:
            level = logger.level(record.levelname).name
        except ValueError:
            level = record.levelno

        # 将日志记录转发给 loguru
        frame, depth = logging.currentframe(), 2
        while frame.f_code.co_filename == logging.__file__:
            frame = frame.f_back
            depth += 1
        logger.opt(depth=depth, exception=record.exc_info).log(level, record.getMessage())


def config_logging(name=None, level="INFO"):  # pragma: no cover
    logging.getLogger(name).addHandler(InterceptHandler())
    logging.getLogger(name).setLevel(level)
