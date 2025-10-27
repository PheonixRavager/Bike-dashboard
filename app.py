import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="Seoul Bike Sharing Dashboard", layout="wide")

# Load data and ensure 'Date' is datetime type for filtering/visuals
df = pd.read_csv("SeoulBikeData_cleaned.csv")
df["Date"] = pd.to_datetime(df["Date"], errors="coerce")

# Sidebar filters
st.sidebar.header("Filters")
months = sorted(df["Date"].dt.month.dropna().unique())
hours = sorted(df["Hour"].dropna().unique())
seasons = sorted(df["Seasons"].astype(str).unique())

selected_month = st.sidebar.selectbox("Select Month", options=months, format_func=lambda m: f"{m:02}")
selected_hour = st.sidebar.selectbox("Select Hour", options=hours)
selected_season = st.sidebar.selectbox("Select Season", options=seasons)

filtered_df = df[
    (df["Date"].dt.month == selected_month) &
    (df["Hour"] == selected_hour) &
    (df["Seasons"].astype(str) == selected_season)
]

# Add button to check filter result
if st.sidebar.button("Check Filter Result"):
    st.sidebar.success(f"Rows matching filters: {len(filtered_df)}")
    if len(filtered_df) == 0:
        st.sidebar.warning("No data found for these filters! Try a different combination.")

st.title("🚲 Seoul Bike Sharing Data Dashboard")
st.markdown("Explore hourly, daily, and monthly bike rental patterns with interactive charts!")

# Preview filtered data (drop Date if Arrow fails)
st.subheader("Sample of Filtered Data")
try:
    filtered_df_display = filtered_df.copy()
    filtered_df_display["Date"] = filtered_df_display["Date"].astype(str)
    st.dataframe(filtered_df_display.head(20))
except Exception as e:
    st.write(f"Exception occurred: {e}")
    st.dataframe(filtered_df.drop(columns=['Date'], errors='ignore').head(20))

# Show summary stats (drop Date column for Arrow issues)
st.subheader("Summary Statistics")
st.write(df.drop(columns=['Date']).describe())

# Visualization 1: Daily Rental Trends
st.subheader("Daily Bike Rentals Over Time")
daily_rentals = df.groupby("Date")["Rented Bike Count"].sum()
fig1, ax1 = plt.subplots(figsize=(12, 5))
ax1.plot(daily_rentals.index, daily_rentals.values, color="tab:blue")
ax1.set_xlabel("Date")
ax1.set_ylabel("Total Rentals")
ax1.set_title("Daily Bike Rentals Over Time")
st.pyplot(fig1)

# Visualization 2: Hourly Usage Patterns
st.subheader("Hourly Bike Rentals (Boxplot)")
fig2, ax2 = plt.subplots(figsize=(10, 5))
sns.boxplot(x="Hour", y="Rented Bike Count", data=df, ax=ax2, palette="Set3", hue="Hour", legend=False)
ax2.set_xlabel("Hour of Day")
ax2.set_ylabel("Number of Rentals")
ax2.set_title("Hourly Bike Rentals (All Days)")
st.pyplot(fig2)

# Visualization 3: Monthly Analysis
st.subheader("Monthly Total Bike Rentals")
df["Month"] = df["Date"].dt.month
monthly_totals = df.groupby("Month")["Rented Bike Count"].sum().reset_index()
fig3, ax3 = plt.subplots(figsize=(10, 5))
sns.barplot(x="Month", y="Rented Bike Count", data=monthly_totals, ax=ax3, palette="viridis", hue="Month", legend=False)
ax3.set_xlabel("Month")
ax3.set_ylabel("Total Rentals")
ax3.set_title("Monthly Total Bike Rentals")
st.pyplot(fig3)

# Visualization 4: Correlation Heatmap
st.subheader("Feature Correlation Heatmap")
fig4, ax4 = plt.subplots(figsize=(9, 7))
sns.heatmap(df.drop(columns=['Date']).corr(numeric_only=True), annot=True, cmap="coolwarm", ax=ax4)
ax4.set_title("Correlation Heatmap")
st.pyplot(fig4)


