# -*- coding: utf-8 -*-
# @shiweitong 2024/4/15
import pytest
from spark_learning.CatEncoder import CatEncoder


def test_catencoder(tmp_data_path):
    encoder = CatEncoder()

    encoder.fit("test_fea", [1, 2, 4])

    cat_encoder_path = tmp_data_path / "cat_encoder.dill"

    encoder.save(cat_encoder_path)

    CatEncoder.load(cat_encoder_path)
    assert encoder.transform("test_fea", [0, 2, 3]) == [-1, 1, -1]
