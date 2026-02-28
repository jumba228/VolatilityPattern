from pathlib import Path
import pandas as pd


class DataLoader:
    REQUIRED_COLUMNS = {"open", "high", "low", "close"}

    def __init__(self, filepath: str | Path):
        self.filepath = Path(filepath)

    def load(self) -> pd.DataFrame:
        if not self.filepath.exists():
            raise FileNotFoundError(f"File not found: {self.filepath}")

        df = pd.read_csv(self.filepath)

        if df.empty:
            raise ValueError("Loaded dataframe is empty.")

        df.columns = [c.lower() for c in df.columns]

        missing = self.REQUIRED_COLUMNS - set(df.columns)
        if missing:
            raise ValueError(f"Missing required columns: {missing}")

        return df