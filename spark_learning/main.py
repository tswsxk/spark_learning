# -*- coding: utf-8 -*-
# @shiweitong 2024/4/12

from fire import Fire


def show_importance(modelpath):
    from spark_learning.utils.models import load_model
    from spark_learning.lgbm import get_feature_importance
    from pprint import pprint

    pprint(get_feature_importance(load_model(modelpath)))


def main():
    Fire({
        "lgb": {"imp": show_importance}
    })
