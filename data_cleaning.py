import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def clean_data(df_raw):
    print("Starting data cleaning...")

    df = df_raw.copy()

    # Step 1: Convert 'Date' column to datetime with error coercion
    df["Date"] = pd.to_datetime(df["Date"], format="%d/%m/%Y", errors='coerce')

    # Step 2: Remove duplicates if any
    duplicates = df.duplicated().sum()
    if duplicates > 0:
        df = df.drop_duplicates(ignore_index=True)

    # Step 3: Clean whitespace in categorical cols
    for col in ["Seasons", "Holiday", "Functioning Day"]:
        df[col] = df[col].str.strip()

    # Step 4: Check for negative values (optional handling can be added)
    numerical_cols = ['Rented Bike Count', 'Temperature(°C)', 'Humidity(%)',
                      'Wind speed (m/s)', 'Visibility (10m)', 'Rainfall(mm)',
                      'Snowfall (cm)']
    for col in numerical_cols:
        negative_count = (df[col] < 0).sum()
        if negative_count > 0:
            print(f"Warning: {negative_count} negative values found in '{col}'")

    # Save cleaned data
    df.to_csv("SeoulBikeData_cleaned.csv", index=False)
    print("Cleaned data saved as 'SeoulBikeData_cleaned.csv'")

    return df


if __name__ == "__main__":
    df_raw = pd.read_csv("SeoulBikeData.csv", encoding="latin1")
    df_clean = clean_data(df_raw)

    # Visualize temperature distribution
    plt.figure(figsize=(10, 6))
    sns.histplot(df_clean["Temperature(°C)"], bins=50, kde=True)
    plt.title("Temperature Distribution (°C)")
    plt.xlabel("Temperature (°C)")
    plt.ylabel("Frequency")
    plt.show()

    # Inspect negative temperature values if any
    neg_temps = df_clean[df_clean["Temperature(°C)"] < 0]
    print(f"Number of negative temperature entries: {neg_temps.shape[0]}")
    print("Sample negative temperature records:")
    print(neg_temps[["Date", "Temperature(°C)"]].head(10))
