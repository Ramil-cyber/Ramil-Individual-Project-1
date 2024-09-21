import pandas as pd
import matplotlib.pyplot as plt


def get_data(path):
    """Read and return the dataframe"""
    df = pd.read_csv(path)
    return df


def get_max_val(df, col):
    return df[col].max()


def get_min_val(df, col):
    return df[col].min()


def get_std_val(df, col):
    return df[col].std()


def get_summary(df):
    return df.describe()


def get_histogram(dataframe, col, img_path, show_image=False):
    """
    Return histogram from given column based on given dataframe
    """
    plt.hist(dataframe[col], bins=5, edgecolor="black")
    plt.title(f"Histogram of {col}")
    plt.xlabel("Values")
    plt.ylabel("Frequency")
    plt.savefig(img_path, dpi=300)
    if show_image:
        plt.show()
    return True


def get_line_graph(dataframe, x_col, y_col, img_path, show_image=False):
    """
    Return line graph from given x and y columns based on given dataframe
    """
    plt.close()
    dataframe.plot(kind="line", x=x_col, y=y_col, legend=True)

    plt.title("Line Graph of Value over Time")
    plt.xlabel(x_col)
    plt.ylabel(y_col)
    plt.savefig(img_path, dpi=300)
    # Show plot
    if show_image:
        plt.show()
    return True


def get_correlation_matrix(df, img_path, show_image=False):
    df = df.select_dtypes(float)
    plt.figure(figsize=(14, 10))
    plt.matshow(
        df.corr(),
        cmap="coolwarm",
    )
    plt.title("Correlation Matrix", pad=20)
    plt.colorbar()
    plt.savefig(img_path)
    if show_image:
        plt.show()
