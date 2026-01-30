# California Fire Crisis

## Project Overview
This project analyzes wildfire trends and impacts in California and the United States using public datasets from BuzzFeed News. The goal is to explore fire frequency, size, damage, and geographic patterns through data analysis and visualization.

The project includes exploratory notebooks, data processing scripts, and visual outputs that summarize wildfire behavior over time.

---

## Data Source

All data comes from BuzzFeed News:

https://github.com/BuzzFeedNews/2018-07-wildfire-trends

The dataset includes:
- `calfire_damage.csv` – property and structure damage data
- `calfire_frap.csv` – California fire perimeter data
- `us_fires/` – seven CSV files with national wildfire records

These files should be placed in:
- data/raw (and are ignored by github)

## uv Environment Setup

This project uses uv for fast and modern python managment.

### Install uv 
https://docs.astral.sh/uv/

On Windows (PS):
```bash 
irm https://astral.sh/uv/install.psi | iex
```

On macOS/Linux:

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### Create the Virtual environment
From the project root:
```bash
uv venv
```

### Activate the Environment

Windows:
```bash 
.venv\Scripts\activate
```

macOS/Linux:
```bash
source .venv/bin/activate
```

### Install dependencies
```bash 
uv pip install
```

## Running the project

To run the main analysis:
```bash 
python src/main.py
```

To explore the analysis yourself:
```bash
jupyter lab
```
and then open any notebook in the notebooks folder

## Dependencies
- numpy
- pandas
- matplotlib
- seaborn
- jupyter

All listed in pyproject.toml