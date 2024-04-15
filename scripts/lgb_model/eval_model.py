# -*- coding: utf-8 -*-
# @shiweitong 2024/4/12
import logging

import pandas as pd
from sklearn.metrics import ndcg_score


def eval_model(submit_file, ground_truth_file):
    submit_df = pd.read_excel(submit_file)
    ground_truth_df = pd.read_excel(ground_truth_file)

    eval_df = pd.merge(ground_truth_df, submit_df, on="edition_id", suffixes=("", "_pred"))

    top5_ground_truth = set(eval_df.sort_values(by=["pheat"], ascending=False)["edition_id"].to_list()[:5])
    top20_pred = set(eval_df.sort_values(by=["pheat_pred"], ascending=False)["edition_id"].to_list()[:20])

    metrics = {
        "ndcg": ndcg_score([eval_df["pheat"]], [eval_df["pheat_pred"]]),
        "recall@20": len(top20_pred & top5_ground_truth) / len(top5_ground_truth),
        "precision@20": len(top20_pred & top5_ground_truth) / len(top20_pred),
    }

    logging.info(metrics)


if __name__ == '__main__':
    from spark_learning import config_logging

    config_logging()

    eval_model("submit.xlsx", "../../data/test_y.xlsx")
