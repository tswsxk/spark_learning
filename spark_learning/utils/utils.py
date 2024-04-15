# -*- coding: utf-8 -*-
# @shiweitong 2024/4/12

import logging
import datetime
from contextlib import contextmanager


@contextmanager
def timeit(prefix, level="info"):
    now = datetime.datetime.now()
    yield
    eval(f"logging.{level}")(f"[TIMEIT] {prefix}, Time Cost: {(datetime.datetime.now() - now).total_seconds()}s")
