import pandas as pd
import numpy as np
from pandas.core.dtypes.common import is_integer_dtype

def test_col_exists(df: pd.DataFrame, column_name: str) -> None:
    """
    Check if a column exists in the DataFrame.

    Parameters:
    - df (pd.DataFrame): The DataFrame to be checked.
    - column_name (str): The name of the column to be checked.

    Raises:
    - AssertionError: If the specified column does not exist in the DataFrame.
    """
    assert column_name in df.columns, f"Column '{column_name}' does not exist in the DataFrame."

def test_null_check(df: pd.DataFrame, column_name: str) -> None:
    """
    Check if there are no null values in a specific column of the DataFrame.

    Parameters:
    - df (pd.DataFrame): The DataFrame to be checked.
    - column_name (str): The name of the column to be checked.

    Raises:
    - AssertionError: If there are null values in the specified column.
    """
    assert df[column_name].notnull().all(), f"Null values found in column '{column_name}'."

def test_unique_check(df: pd.DataFrame, column_name: str) -> None:
    """
    Check if all values in a specific column of the DataFrame are unique.

    Parameters:
    - df (pd.DataFrame): The DataFrame to be checked.
    - column_name (str): The name of the column to be checked.

    Raises:
    - AssertionError: If there are duplicate values in the specified column.
    """
    assert df[column_name].is_unique, f"Not all values in column '{column_name}' are unique."

def test_productkey_dtype_int(df: pd.DataFrame, column_name: str) -> None:
    """
    Check if the data type of a specific column is integer.

    Parameters:
    - df (pd.DataFrame): The DataFrame to be checked.
    - column_name (str): The name of the column to be checked.

    Raises:
    - AssertionError: If the data type of the specified column is not integer.
    """
    assert is_integer_dtype(df[column_name]), f"The data type of column '{column_name}' is not integer."

def test_productname_dtype_str(df: pd.DataFrame, column_name: str) -> None:
    """
    Check if the data type of a specific column is string.

    Parameters:
    - df (pd.DataFrame): The DataFrame to be checked.
    - column_name (str): The name of the column to be checked.

    Raises:
    - AssertionError: If the data type of the specified column is not string.
    """
    assert pd.api.types.is_string_dtype(df[column_name]), f"The data type of column '{column_name}' is not string."

def test_range_val(df: pd.DataFrame, column_name: str, min_val: int, max_val: int) -> None:
    """
    Check if values in a specific column are within a specified range.

    Parameters:
    - df (pd.DataFrame): The DataFrame to be checked.
    - column_name (str): The name of the column to be checked.
    - min_val (int): The minimum allowed value.
    - max_val (int): The maximum allowed value.

    Raises:
    - AssertionError: If values in the specified column are outside the specified range.
    """
    assert df[column_name].between(min_val, max_val).any(), f"Values in column '{column_name}' are not within the range {min_val}-{max_val}."

def test_range_val_str(df: pd.DataFrame, column_name: str, valid_values: set) -> None:
    """
    Check if values in a specific column are in a specified list.

    Parameters:
    - df (pd.DataFrame): The DataFrame to be checked.
    - column_name (str): The name of the column to be checked.
    - valid_values (set): A set of valid values.

    Raises:
    - AssertionError: If values in the specified column are not in the specified list.
    """
    assert set(df[column_name].unique()) == valid_values, f"Invalid values found in column '{column_name}'. Expected values: {valid_values}."
