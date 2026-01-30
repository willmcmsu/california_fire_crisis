"""Quick plot of damaged structures by year (California)."""

import pandas as pd
import matplotlib.pyplot as plt

# This is intentionally a little rough: path is hard-coded and no CLI args.
DATA_PATH = "2018-07-wildfire-trends/data/calfire_damage.csv"

# Load the small, tidy CSV of total structures damaged each year.
# Columns: year, structures

df = pd.read_csv(DATA_PATH)

# Make sure year is sorted (just in case).
df = df.sort_values("year")

fig, ax = plt.subplots(figsize=(9, 4.8))
ax.plot(df["year"], df["structures"], marker="o", color="#d1495b")
ax.set_title("California Wildfire Damage by Year")
ax.set_xlabel("Year")
ax.set_ylabel("Structures Damaged")
ax.grid(alpha=0.3)

# A small annotation to help students see the peak
max_row = df.loc[df["structures"].idxmax()]
ax.annotate(
    f"Peak: {int(max_row['structures'])}",
    xy=(max_row["year"], max_row["structures"]),
    xytext=(max_row["year"] - 6, max_row["structures"] * 0.75),
    arrowprops=dict(arrowstyle="->", color="#444"),
    fontsize=9,
)

plt.tight_layout()
plt.savefig("damage_trend.png", dpi=150)
plt.show()
