from src.main import calculate_iqr, save_to_md
from src.lib import get_data
import os

remote_path = remote_path = (
    "https://raw.githubusercontent.com/Ramil-cyber/Ramil-Individual-Project-1/refs/heads/main/data/shanghai_ranking_2024.csv"
)


def test_main():
    df = get_data(remote_path)
    top_100_df = df.iloc[:100, :]
    print(int(calculate_iqr(top_100_df, column="Award"))) == 26

    save_to_md(df)
    assert os.path.exists("summary_statistics.md")
