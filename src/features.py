import pandas as pd


def create_features(df):
    df = df.copy()

    # Convert dates to datetime
    dates = pd.to_datetime(df["date"])

    # Create date features
    df["month"] = dates.dt.month
    df["day_of_week"] = dates.dt.dayofweek
    df["days_since_start"] = (
        dates - pd.Timestamp("2025-01-01")
    ).dt.days

    # Remove columns not used for prediction
    df = df.drop(
        columns=["load_id", "date", "posted_rate", "rate_per_mile"],
        errors="ignore"
    )

    return df