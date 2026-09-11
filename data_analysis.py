import pandas as pd


def get_dataset_info(df):

    info = {
        "Number of Rows": df.shape[0],
        "Number of Columns": df.shape[1],
        "Column Names": list(df.columns),
        "Data Types": df.dtypes.astype(str).to_dict(),
        "Missing Values": df.isnull().sum().to_dict()
    }

    return info


def get_statistics(df):

    numeric_df = df.select_dtypes(include="number")

    if numeric_df.empty:
        return None

    return numeric_df.describe()


def get_missing_values(df):

    missing_values = df.isnull().sum()

    return missing_values


def get_categorical_summary(df):

    categorical_df = df.select_dtypes(
        include=["object", "category"]
    )

    if categorical_df.empty:
        return None

    summary = {}

    for column in categorical_df.columns:

        mode_values = categorical_df[column].mode()

        summary[column] = {
            "Unique Values": categorical_df[column].nunique(),
            "Most Common Value": (
                mode_values.iloc[0]
                if not mode_values.empty
                else "No value"
            )
        }

    return summary