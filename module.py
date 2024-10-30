from tabulate import tabulate
from sklearn.cluster import KMeans


def print_df_in_chunks(df, n):
    """
    Prints the DataFrame in chunks of n columns using tabulate.

    Parameters:
    df (pd.DataFrame): The DataFrame to print.
    n (int): The number of columns per chunk.
    """
    start = 0
    end = n
    total_columns = df.shape[1]

    while start < total_columns:
        print(tabulate(df.iloc[:, start:end].head(), headers="keys", tablefmt="orgtbl"))
        start = end
        end += n
        print()  # Add an empty line between chunks for better readability


def elbow_method(K_range, df):

    # Range of K values to try
    K_range = range(1, K_range)

    # List to store the inertia values (sum of squared distances)
    inertia_values = []

    # Fit K-Means with different K values and calculate inertia
    for K in K_range:
        kmeans = KMeans(n_clusters=K, random_state=42)
        kmeans.fit(df)
        inertia_values.append(
            kmeans.inertia_
        )  # Inertia is the sum of squared distances

    # Preparing the data for printing in tabular format with inertia loss
    table = []
    for i, inertia in enumerate(inertia_values):
        if i == 0:
            table.append((i + 1, inertia, "N/A"))  # No previous inertia for K=1
        else:
            inertia_loss = inertia_values[i - 1] - inertia
            table.append((i + 1, inertia, inertia_loss))

    # Print the result in a formatted table
    headers = [
        "Number of Clusters (K)",
        "Inertia (Sum of Squared Distances)",
        "Inertia Loss (Compared to Previous K)",
    ]
    print(tabulate(table, headers, tablefmt="pretty"))
