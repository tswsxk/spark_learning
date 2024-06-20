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

**NOTICE: Download the data before you run the scripts:**
```
data/
├── test_X.xlsx
├── test_y.xlsx
└── train.xlsx
```

3. The following parts are optional

* Run tests

```bash
pip install -e .[test] --config-settings editable_mode=compat
pytest
```

* Use command line tools to see the feature importance of model

```bash
# After you have trained the lgb model
tsl lgb imp scripts/lgb_model/lgb.dill
```

### Troubleshooter

1. **For M1/M2/M3 Mac Users**: If you encounter issues with installing LightGBM, create a conda virtual environment, and install it using `conda`: 
   ```sh
   conda install -c conda-forge lightgbm
   ```

2. **File Not Found Error**: If you see an error like `"No such file or directory: '../../data/train.xlsx'"` after placing the files in the `data` directory, ensure that you are running the script from its directory (e.g., `.../spark_learning/scripts/lgb_model`) rather than the project root (e.g., `.../spark_learning`). Note that VSCode's default behavior is to use the project directory, so run the script from the command line instead.
