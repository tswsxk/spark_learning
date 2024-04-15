from setuptools import setup

test_deps = [
    'pytest>=4',
    'pytest-cov>=2.6.0',
    'pytest-flake8<5.0.0',
    'flake8<5.0.0'
]

spider_deps = [
    "google-api-python-client",
]

setup(
    name='spark_learning',
    version='0.0.1',
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
        "lightgbm"
    ],  # And any other dependencies foo needs
    entry_points={
    },
)
