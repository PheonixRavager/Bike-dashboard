import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("SeoulBikeData_cleaned.csv", parse_dates=["Date"])

# 1. Daily Rental Trends Over Time
plt.figure(figsize=(12, 5))
daily_rentals = df.groupby("Date")["Rented Bike Count"].sum()
plt.plot(daily_rentals.index, daily_rentals.values, color="tab:blue")
plt.title("Daily Bike Rentals Over Time")
plt.xlabel("Date")
plt.ylabel("Total Rentals")
plt.tight_layout()
plt.show()

# 2. Hourly Usage Patterns (Boxplot)
plt.figure(figsize=(10, 5))
sns.boxplot(x="Hour", y="Rented Bike Count", data=df, hue="Hour", palette="Set3", legend=False)
plt.title("Hourly Bike Rentals")
plt.xlabel("Hour of Day")
plt.ylabel("Number of Rentals")
plt.tight_layout()
plt.show()

# 3. Monthly Analysis
df["Month"] = df["Date"].dt.month
plt.figure(figsize=(10, 5))
sns.barplot(x="Month", y="Rented Bike Count", data=df, estimator=sum, hue="Month", palette="viridis", legend=False)
plt.title("Monthly Total Bike Rentals")
plt.xlabel("Month")
plt.ylabel("Total Rentals")
plt.tight_layout()
plt.show()

# 4. Correlation Heatmap (wider figure)
plt.figure(figsize=(12, 8))
sns.heatmap(df.corr(numeric_only=True), annot=True, cmap="coolwarm", linewidths=.5)
plt.title("Correlation Heatmap")
plt.tight_layout()
plt.show()
