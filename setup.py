from setuptools import setup, find_packages

test_deps = [
    'pytest>=4',
    'pytest-cov>=2.6.0',
    'flake8'
]

spider_deps = [
    "google-api-python-client",
]

setup(
    name='spark_learning',
    version='0.0.1',
    packages=find_packages(
        include=[
            "spark_learning", "spark_learning.*"
        ],
    ),
    extras_require={
        'test': test_deps,
        'spider': spider_deps
    },
    install_requires=[
        "pandas",
        "scikit-learn",
        "dill",
        "tqdm",
        "loguru",
        "lightgbm",
        "jupyter",
        "openpyxl",
        "matplotlib",
        "fire",
        'db-dtypes',
    ],  # And any other dependencies for needs
    entry_points={
        "console_scripts": [
            "tsl = spark_learning.main:main"
        ],
    },
)
