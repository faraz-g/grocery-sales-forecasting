# Grocery Sales Forecasting

Experimenting with:

https://www.kaggle.com/competitions/favorita-grocery-sales-forecasting/overview

# Quickstart Guide

### Install poetry
We use `poetry` for dependency management, refer to [their documentation](https://python-poetry.org/docs/) for a thorough intro and installation guide.

If you install `poetry` with their official installer as opposed to `pipx`, make sure it's been added to your system path.

**Test** your installation by running the following command in a fresh shell:
```bash
poetry --version
```

### Install project dependencies

Simply run:
```
poetry install
```

### Download the dataset

1) Create an account on https://www.kaggle.com/
2) Follow the instructions on https://www.kaggle.com/docs/api#authentication to create an API key for your Kaggle account
3) Run the following command:
```bash
poetry run python grocery_sales_forecasting/data_downloader.py
```
