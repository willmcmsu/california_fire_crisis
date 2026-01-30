"""Small numeric summary using NumPy."""

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy import stats
from mpl_toolkits.axes_grid1.inset_locator import inset_axes, mark_inset

DATA_PATH = "2018-07-wildfire-trends/data/calfire_frap.csv"

# Load and coerce fire sizes.
df = pd.read_csv(DATA_PATH)
fire_sizes = pd.to_numeric(df["gis_acres"], errors="coerce").dropna().values

# NumPy-based summary stats.
mean_size = np.mean(fire_sizes)
median_size = np.median(fire_sizes)
std_size = np.std(fire_sizes)

print("Mean acres:", round(mean_size, 2))
print("Median acres:", round(median_size, 2))
print("Std dev acres:", round(std_size, 2))

# Quick z-score example (first 10 values)
z_scores = (fire_sizes - mean_size) / std_size
print("Z-scores (first 10):", np.round(z_scores[:10], 2))

# SciPy-based distribution stats (skewness and kurtosis)
skewness = stats.skew(fire_sizes, nan_policy="omit")
kurt = stats.kurtosis(fire_sizes, nan_policy="omit")
print("Skewness:", round(skewness, 2))
print("Kurtosis:", round(kurt, 2))

# Seaborn-styled visualization that highlights mean/median/std
sns.set_theme(style="whitegrid")

plot_df = pd.DataFrame({"gis_acres": fire_sizes})
fig, ax = plt.subplots(figsize=(8.5, 4.5), constrained_layout=True)
sns.histplot(plot_df["gis_acres"], bins=40, ax=ax, color="#2a9d8f", alpha=0.6)

# Marker tied directly to the computed stats
ax.axvspan(mean_size - std_size, mean_size + std_size, color="#f4a261", alpha=0.2, label="±1 std dev")

ax.set_title("Fire Size Distribution with Mean/Median/Std")
ax.set_xlabel("Fire Size (acres)")
ax.set_ylabel("Count")
ax.legend(frameon=False, loc="lower right")

# Inset: zoomed distribution for small fires (< 2000 acres)
small = plot_df[plot_df["gis_acres"] < 2000]["gis_acres"]
axins = inset_axes(ax, width="42%", height="42%", loc="upper right", borderpad=1.1)
sns.histplot(small, bins=30, ax=axins, color="#2a9d8f", alpha=0.7)
axins.axvline(mean_size, color="#e76f51", linestyle="--", linewidth=1.5, label="Mean")
axins.axvline(median_size, color="#264653", linestyle="-", linewidth=1.5, label="Median")
axins.set_title("< 2000 acres", fontsize=9)
axins.set_xlabel("")
axins.set_ylabel("")
axins.tick_params(axis="both", labelsize=8)

# Label mean/median lines inside the inset if they fall within the range.
if mean_size < 2000:
    axins.text(
        mean_size,
        0.88,
        "Mean",
        transform=axins.get_xaxis_transform(),
        color="#e76f51",
        fontsize=8,
        ha="left",
        va="center",
    )
if median_size < 2000:
    axins.text(
        median_size,
        0.76,
        "Median",
        transform=axins.get_xaxis_transform(),
        color="#264653",
        fontsize=8,
        ha="left",
        va="center",
    )

mark_inset(ax, axins, loc1=2, loc2=4, fc="none", ec="0.5")

plt.savefig("fire_size_distribution.png", dpi=150)
plt.show()
