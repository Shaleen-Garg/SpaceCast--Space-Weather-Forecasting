# SpaceCast

SpaceCast is a time-series forecasting project that applies pretrained Time-Series Foundation Models (TSFMs) to real NASA space-weather observations.

## Project Goal
Solar-wind / geomagnetic observations -> TSFM -> future space-weather forecast -> evaluation -> visualization.

## Technologies
- Python 3.11+
- PyTorch & Hugging Face (Chronos-2)
- Pandas, NumPy, Scikit-learn
- Jupyter for exploration

## Project Structure
- `data/`: Raw, interim, and processed data (ignored by git).
- `notebooks/`: Jupyter notebooks for data exploration, analysis, and modeling.
- `src/spacecast/`: Reusable Python modules.
- `tests/`: Unit tests.
- `docs/`: Project documentation.
