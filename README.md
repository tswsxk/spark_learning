# Beginner Tutorial

## Preparation

1. Install dependencies and initial the package

```bash
make install
```

If you have multi-version python, use the command like

```bash
make install ENVPIP=pip3.9
```
to specify your pip.


Also, you can use the following command:

```bash
pip install -e . --config-settings editable_mode=compat
```

(Optional)

If you want to include the spider deps, use the following command:

```bash
pip install -e .[spider] --config-settings editable_mode=compat
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

## Trouble Shooter

1. For M1/M2/M3 mac users, use `conda` to install lightgbm if you found there is no usable one: `conda install -c conda-forge lightgbm`
