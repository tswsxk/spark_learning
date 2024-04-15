# -*- coding: utf-8 -*-
# @shiweitong 2024/4/12

import pandas as pd
from lightgbm import LGBMRegressor


def get_feature_importance(model: LGBMRegressor) -> pd.Series:
    return pd.Series(model.feature_importances_, index=model.feature_name_)
