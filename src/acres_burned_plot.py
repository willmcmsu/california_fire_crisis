"""Aggregate acres burned by year from the FRAP dataset."""

import pandas as pd
import matplotlib.pyplot as plt

# Hard-coded path to the FRAP fire perimeter dataset.
DATA_PATH = "2018-07-wildfire-trends/data/calfire_frap.csv"

# Load data (large-ish but still manageable for class demo).
# Using report_ac where available; falling back to gis_acres for missing values.

df = pd.read_csv(DATA_PATH)

# Coerce year and acres to numeric; lots of messy rows in the raw data.
df["year_"] = pd.to_numeric(df["year_"], errors="coerce")
df["report_ac"] = pd.to_numeric(df["report_ac"], errors="coerce")
df["gis_acres"] = pd.to_numeric(df["gis_acres"], errors="coerce")

# Prefer reported acres, but use GIS acres when report_ac is missing.
df["acres"] = df["report_ac"].fillna(df["gis_acres"])

# Drop rows without year or acres.
df = df.dropna(subset=["year_", "acres"])

# Aggregate total acres by year.
by_year = (
    df.groupby("year_")["acres"]
    .sum()
    .reset_index()
    .sort_values("year_")
)

fig, ax = plt.subplots(figsize=(9, 4.8))
ax.plot(by_year["year_"], by_year["acres"], color="#3c6e71")
ax.set_title("California Wildfire Acres Burned by Year (FRAP)")
ax.set_xlabel("Year")
ax.set_ylabel("Total Acres Burned")
ax.grid(alpha=0.3)

# Add a rolling average to smooth year-to-year volatility.
by_year["rolling_5"] = by_year["acres"].rolling(5, min_periods=1).mean()
ax.plot(by_year["year_"], by_year["rolling_5"], color="#284b63", linestyle="--", label="5-yr avg")
ax.legend(frameon=False)

plt.tight_layout()
plt.savefig("acres_burned.png", dpi=150)
plt.show()
