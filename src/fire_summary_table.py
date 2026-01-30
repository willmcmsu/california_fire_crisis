"""Build a formatted summary table with Great Tables."""

from pathlib import Path

import pandas as pd
from great_tables import GT, md

DATA_PATH = "2018-07-wildfire-trends/data/calfire_frap.csv"
DAMAGE_PATH = "2018-07-wildfire-trends/data/calfire_damage.csv"
OUTPUT_PATH = Path("results") / "fire_summary_table.html"

df = pd.read_csv(DATA_PATH)
df["gis_acres"] = pd.to_numeric(df["gis_acres"], errors="coerce")
df["year_"] = pd.to_numeric(df["year_"], errors="coerce")
df = df.dropna(subset=["gis_acres", "year_"])

summary = (
    df.groupby("year_")
    .agg(
        fires=("fire_name", "count"),
        total_acres=("gis_acres", "sum"),
        avg_acres=("gis_acres", "mean"),
    )
    .reset_index()
    .rename(columns={"year_": "year"})
)

damage = pd.read_csv(DAMAGE_PATH)
summary = summary.merge(damage, on="year", how="left")

max_year = int(summary["year"].max())
recent = summary[summary["year"] >= (max_year - 9)].sort_values("year")

recent = recent.rename(
    columns={
        "year": "Year",
        "fires": "Fires",
        "total_acres": "Total acres",
        "avg_acres": "Avg. acres",
        "structures": "Structures damaged",
    }
)

gt_tbl = (
    GT(recent)
    .tab_header(
        title=md("California Wildfire Summary (last 10 years)"),
        subtitle=md("Fires, acres burned, and structures damaged"),
    )
    .fmt_number(columns=["Fires", "Total acres", "Structures damaged"], decimals=0)
    .fmt_number(columns="Avg. acres", decimals=1)
    .opt_row_striping()
    .tab_source_note(
        source_note=md(
            "Source: BuzzFeed News wildfire trends dataset (CAL FIRE tables)."
        )
    )
)

OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
OUTPUT_PATH.write_text(gt_tbl.as_raw_html(make_page=True), encoding="utf-8")
