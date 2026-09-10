"""
Replace Plot 5 cells in 07_playground.ipynb:
- Cell 11 (md-p5): new markdown for the 10-year Dst time series
- Cell 12 (cell-plot5): new code for the 10-year Dst full time series plot
"""
import json

with open('notebooks/07_playground.ipynb', encoding='utf-8') as f:
    nb = json.load(f)

cells = nb['cells']

# ── New markdown cell (cell 11) ──────────────────────────────────────────────
cells[11]['source'] = [
    "## Plot 5 \u2014 10-Year Dst Time Series (2016\u20132025)\n",
    "Full hourly Dst record across the entire dataset. "
    "Severe storms (Dst < \u2212100\u202fnT) are shaded red; "
    "the May\u202f2024 G5 superstorm (\u2212406\u202fnT) is the deepest dip in the record. "
    "The rising activity toward solar maximum (~2024\u20132025) is visually clear."
]

# ── New code cell (cell 12) ──────────────────────────────────────────────────
new_code = """\
# ---------------------------------------------------------------------------
# Plot 5: Full 10-year Dst time series (2016-2025)
# ---------------------------------------------------------------------------
_dst_full = df["Dst_nT"].astype(float)
_t_full   = df.index

fig, ax = plt.subplots(figsize=(14, 4))

# Base line
ax.plot(_t_full, _dst_full, color="#555577", linewidth=0.55, alpha=0.85, rasterized=True)

# Shade severe storm periods (Dst < -100 nT)
_storm_mask = _dst_full < -100
ax.fill_between(
    _t_full, _dst_full, -100,
    where=_storm_mask,
    color="#d6604d", alpha=0.65, linewidth=0,
    label="Severe storm  (Dst < \\u2212100 nT)",
    rasterized=True,
)

# Shade moderate storm band (-50 to -100 nT) with lighter colour
_mod_mask = (_dst_full < -50) & ~_storm_mask
ax.fill_between(
    _t_full, _dst_full, -50,
    where=_mod_mask,
    color="#f4a582", alpha=0.35, linewidth=0,
    label="Moderate storm  (Dst < \\u221250 nT)",
    rasterized=True,
)

# Reference lines
ax.axhline(0,    color="#333333", linewidth=0.7, linestyle="--", alpha=0.5)
ax.axhline(-50,  color="#f4a582", linewidth=0.7, linestyle=":",  alpha=0.8)
ax.axhline(-100, color="#d6604d", linewidth=0.8, linestyle=":",  alpha=0.9)

# Annotate the May 2024 G5 minimum
_may24_t   = pd.Timestamp("2024-05-11 02:00")
_may24_val = int(_dst_full.loc[_may24_t])
ax.annotate(
    f"May 2024 G5\\nDst = {_may24_val}\\u202fnT",
    xy=(_may24_t, _may24_val),
    xytext=(pd.Timestamp("2022-06-01"), -310),
    arrowprops=dict(arrowstyle="->", color="#cc0000", lw=1.1),
    fontsize=8, color="#cc0000", fontweight="bold",
)

ax.set_xlim(_t_full.min(), _t_full.max())
ax.set_xlabel("Year")
ax.set_ylabel("Dst (nT)")
ax.set_title(
    "Full Dst Record  \\u2014  2016\\u20132025  (87\\u202f672 hourly observations)",
    fontsize=12, fontweight="bold",
)
ax.legend(loc="lower left", fontsize=8)
ax.xaxis.set_major_locator(matplotlib.dates.YearLocator())
ax.xaxis.set_major_formatter(matplotlib.dates.DateFormatter("%Y"))

fig.tight_layout()
_out = os.path.join(PLAYGROUND_DIR, "05_timesfm_covariate_benefit.png")
fig.savefig(_out)
plt.show()
print(f"Saved: {_out}")
"""

cells[12]['source'] = new_code.splitlines(keepends=True)
# Reset execution count and outputs so it runs clean
cells[12]['execution_count'] = None
cells[12]['outputs'] = []

# Also reset verification cell so it re-runs cleanly
cells[17]['execution_count'] = None
cells[17]['outputs'] = []

with open('notebooks/07_playground.ipynb', 'w', encoding='utf-8') as f:
    json.dump(nb, f, indent=1, ensure_ascii=False)

print("Cells 11 and 12 updated successfully.")
