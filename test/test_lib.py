from src.lib import (
    get_data,
    get_max_val,
    get_min_val,
    get_std_val,
    get_histogram,
    get_line_graph,
    get_correlation_matrix,
)

import os
import pandas as pd

remote_path = "https://raw.githubusercontent.com/Ramil-cyber/Ramil-Individual-Project-1/refs/heads/main/data/shanghai_ranking_2024.csv"


def test_df():
    df = get_data(remote_path)

    assert df.shape[0] == 1000
    assert df.shape[1] == 9
    assert isinstance(df, pd.DataFrame)


def test_funcs():
    df = get_data(remote_path)

    assert int(get_max_val(df, "N&S")) == 100
    assert int(get_std_val(df, "N&S")) == 10
    assert int(get_min_val(df, "PUB")) == 9


def test_visualization():
    df = get_data(remote_path)

    get_histogram(df, "PCP", img_path="data/test_histogram.png")
    assert os.path.exists("data/test_histogram.png")
    os.remove("data/test_histogram.png")

    get_line_graph(df, x_col="Alumni", y_col="PUB", img_path="data/test_line_graph.png")
    assert os.path.exists("data/test_line_graph.png")
    os.remove("data/test_line_graph.png")

    get_correlation_matrix(df, img_path="data/test_correlation_matrix.png")
    assert os.path.exists("data/test_correlation_matrix.png")
    os.remove("data/test_correlation_matrix.png")


test_funcs()
