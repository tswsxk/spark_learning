# -*- coding: utf-8 -*-
# @shiweitong 2024/4/15


import pytest

from spark_learning import config_logging

config_logging()


@pytest.fixture(scope="session")
def tmp_data_path(tmp_path_factory):
    return tmp_path_factory.mktemp("data")
