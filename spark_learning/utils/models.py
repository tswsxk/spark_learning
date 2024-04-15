# -*- coding: utf-8 -*-
# @shiweitong 2024/4/12

import dill

from .utils import timeit


def save_model(model, filepath):
    with open(filepath, "wb") as wf, timeit(f"Model is saved to {filepath}"):
        dill.dump(model, wf)


def load_model(filepath):
    with open(filepath, "rb") as f, timeit(f"Model is loaded from {filepath}"):
        return dill.load(f)
