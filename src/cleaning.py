import pandas as pd


def clean_weight(df, median_weight):
    # create copy for safety so I dont edit the original
    df = df.copy()

    # Treat zero and negative weights as missing values.
    df.loc[df["weight"] <= 0, "weight"] = float("nan")

    # Replace missing weights with the training median.
    df["weight"] = df["weight"].fillna(median_weight)

    return df

def clean_market_index(df, daily_medians, overall_median):
    # Copy the DataFrame to protect the original.
    df = df.copy()

    # Find the median market index for each row's date.
    same_day_median = df["date"].map(daily_medians)

    # Fill missing values using the same-day median.
    df["market_index"] = df["market_index"].fillna(same_day_median)

    # If the date has no known median, use the training median.
    df["market_index"] = df["market_index"].fillna(overall_median)

    return df