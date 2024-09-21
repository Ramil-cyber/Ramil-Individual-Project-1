import pandas as pd
from lib import (
    get_summary,
    get_histogram,
    get_line_graph,
    get_correlation_matrix,
)


remote_path = "https://raw.githubusercontent.com/Ramil-cyber/Ramil-Individual-Project-1/refs/heads/main/data/shanghai_ranking_2024.csv"


def calculate_iqr(df, column):
    """
    Calculate the Interquartile Range (IQR) of a given column in the DataFrame.
    Parameters:
    df (pandas.DataFrame): The input DataFrame.
    column (str): The name of the column for which to calculate the IQR.
    Returns:
    float: The calculated IQR of the column.
    """
    # Get the first quartile (25th percentile)
    Q1 = df[column].quantile(0.25)
    # Get the third quartile (75th percentile)
    Q3 = df[column].quantile(0.75)
    # Calculate the IQR
    IQR = Q3 - Q1
    return IQR


def save_to_md(data):
    """save summary report to markdown"""
    describe_df = get_summary(data)
    markdown_table1 = describe_df.to_markdown()
    # Write the markdown table to a file
    with open("summary_statistics.md", "w", encoding="utf-8") as file:
        file.write("Describe:\n")
        file.write(markdown_table1)
        file.write("\n\n")  # Add a new line
        file.write("![alt_text_histogram](data/histogram.png)\n")
        file.write("\n\n")  # Add a new line
        file.write("![alt_text_line_graph](data/line_graph.png)\n")
        file.write("\n\n")  # Add a new line
        file.write("![alt_text_correlation_matrix](data/correlation_matrix.png)\n")


if __name__ == "__main__":
    df = pd.read_csv(remote_path)

    top_100_df = df.iloc[:100, :]
    get_histogram(top_100_df, col="PCP", img_path="data/histogram.png")
    get_line_graph(
        top_100_df, x_col="Alumni", y_col="PUB", img_path="data/line_graph.png"
    )
    get_correlation_matrix(top_100_df, img_path="data/correlation_matrix")

    save_to_md(df)

    print(calculate_iqr(top_100_df, column="Award"))  # 26.650000000000006
