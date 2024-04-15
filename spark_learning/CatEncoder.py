# -*- coding: utf-8 -*-
# @shiweitong 2024/4/12

import dill
from .utils.models import save_model, load_model


class CatEncoder(object):
    """
    Examples
    --------
    >>> x = ["1", "5", "7"]
    >>> encoder = CatEncoder()
    >>> encoder.fit_transform("id", x)
    [0, 1, 2]
    >>> encoder.transform("id", [-1, 2])
    [-1, -1]
    """

    def __init__(self):
        self.encoders = {}

    def fit(self, feature_name, X):
        encoder = {}
        for x in X:
            if x not in encoder:
                encoder[x] = len(encoder)

        self.encoders[feature_name] = encoder

    def fit_transform(self, feature_name, X) -> list:
        self.fit(feature_name, X)
        return self.transform(feature_name, X)

    def transform(self, feature_name, X) -> list:
        return [self.encoders[feature_name].get(x, -1) for x in X]

    def save(self, filepath):
        save_model(self, filepath)

    @classmethod
    def load(cls, filepath):
        return load_model(filepath)
