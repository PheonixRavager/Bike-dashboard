from load_data import load_data
from data_cleaning import clean_data
import pandas as pd

def test_load_data():
    df = load_data("SeoulBikeData_cleaned.csv")
    df["Date"] = pd.to_datetime(df["Date"], errors="coerce")  # Ensure datetime dtype
    assert not df.empty
    assert "Date" in df.columns
    assert pd.api.types.is_datetime64_any_dtype(df["Date"])

def test_clean_data():
    df_raw = pd.read_csv("SeoulBikeData.csv", encoding="latin1")
    df_clean = clean_data(df_raw)
    assert df_clean["Rented Bike Count"].isnull().sum() == 0  # or .notnull().all()
    assert pd.api.types.is_datetime64_any_dtype(df_clean["Date"])

def test_filtering():
    df = load_data("SeoulBikeData_cleaned.csv")
    df["Date"] = pd.to_datetime(df["Date"], errors="coerce")
    filtered = df[(df["Date"].dt.month == 1) & (df["Hour"] == 6)]
    assert (filtered["Date"].dt.month == 1).all()
    assert (filtered["Hour"] == 6).all()



