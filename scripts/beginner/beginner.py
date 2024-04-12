# -*- coding: utf-8 -*-
# @shiweitong 2024/4/12
import logging
import time

from tqdm import tqdm

from spark_learning.utils import config_logging

if __name__ == '__main__':
    config_logging()

    logging.info("This is the beginner script")

    for _ in tqdm(range(100), "Loading"):
        time.sleep(0.02)

    print("*** Spark ***")
