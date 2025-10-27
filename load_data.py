import pandas as pd


def load_data(data_path="SeoulBikeData_cleaned.csv"):
    print("Loading Seoul Bike Sharing Demand data...")
    df = pd.read_csv(data_path, encoding="latin1", parse_dates=["Date"])
    # Ensure Date col is datetime type
    df["Date"] = pd.to_datetime(df["Date"], errors="coerce")
    print("✅ Data loaded successfully!")
    print(f"Dataset shape: {df.shape}")  # (rows, columns)
    print("\n" + "=" * 60 + "\n")

    print("First 5 rows:")
    print(df.head())
    print("\n" + "=" * 60 + "\n")

    print("Column names:")
    print(df.columns.tolist())
    print("\n" + "=" * 60 + "\n")

    print("Dataset info:")
    df.info()
    print("\n" + "=" * 60 + "\n")

    print("Missing values in each column:")
    print(df.isnull().sum())
    print("\n" + "=" * 60 + "\n")

    return df


if __name__ == "__main__":
    load_data()
