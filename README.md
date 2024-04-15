# Beginner Tutorial

## Preparation

1. Install dependencies and initial the package

```bash
pip install -e .
```

(Optional)

If you want to include the spider deps, use the following command:

```bash
pip install -e .[spider]
```

2. Run the demo script to see whether everything has been prepared

```bash
cd scripts/beginner
python beginner.py
```

If you see `*** Spark ***` in the terminal, then everything goes well.

Then, run the notebook `eda.ipynb` in `scripts/EDA`

3. The following parts are optional

* Run tests

```bash
pip install -e .[test]
pytest
```

* Use command line tools to see the feature importance of model

```bash
# After you have trained the lgb model
tsl lgb imp scripts/lgb_model/lgb.dill
```
