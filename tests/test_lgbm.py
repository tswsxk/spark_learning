# -*- coding: utf-8 -*-
# @shiweitong 2024/4/15

import pandas as pd
from lightgbm import LGBMRegressor
from spark_learning.lgbm.analyze import get_feature_importance


def test_feature_importance():
    model = LGBMRegressor()
    test_x = pd.DataFrame({"fea1": [1, 2, 3], "fea2": [4, 5, 6]})
    test_y = [1, 1, 1]
    model.fit(test_x, test_y)
    assert len(get_feature_importance(model)) == 2
