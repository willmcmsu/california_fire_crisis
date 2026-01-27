"""Run all plots in sequence.

This is intentionally informal: no argparse, no logging, just quick calls.
"""

import subprocess

# The scripts live in the same folder.
subprocess.run(["python", "make_damage_plot.py"], check=False)
subprocess.run(["python", "acres_burned_plot.py"], check=False)
subprocess.run(["python", "fire_size_stats.py"], check=False)
subprocess.run(["python", "fire_summary_table.py"], check=False)
