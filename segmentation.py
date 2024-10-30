import pandas as pd
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
import matplotlib.pyplot as plt
import seaborn as sns
import module

# Load the CSV file and clean col names
file_path = "data/member-demo-data.xlsx"
df = pd.read_excel(file_path, sheet_name="Data Clean for ML")
df.columns = (
    df.columns.astype(str)
    .str.replace(" ", "_")
    .str.replace(",", "")
    .str.replace(":", "")
    .str.replace("&", "and")
    .str.lower()
)


# Preprocessing Function
def preprocess_data(df):
    df = df.dropna(axis="columns", how="all")
    df = df.dropna(axis="rows", how="all")
    df = df.drop(columns="child_name")

    # Separate numerical and categorical columns
    numerical_cols = df.select_dtypes(include=["float64", "int64"]).columns
    categorical_cols = df.select_dtypes(include=["object", "category"]).columns

    # Encoding categorical columns
    encoder = OneHotEncoder(
        sparse_output=False, drop="first"
    )  # drop='first' to avoid multicollinearity (optional)
    encoded_cols = encoder.fit_transform(df[categorical_cols])
    encoded_df = pd.DataFrame(
        encoded_cols, columns=encoder.get_feature_names_out(categorical_cols)
    )
    df = pd.concat([df, encoded_df], axis=1)
    df = df.drop(columns=categorical_cols)

    # Feature Scaling using Standard Scaler
    scaler = StandardScaler()
    col_names = df.columns
    df = pd.DataFrame(scaler.fit_transform(df), columns=col_names)

    return df


# Preprocess the data
df_processed = preprocess_data(df)

# Elbow method
module.elbow_method(11, df_processed)

# Define the number of clusters (you can change this based on elbow method)
n_clusters = 3

# K-Means Clustering
kmeans = KMeans(n_clusters=n_clusters, random_state=42)
clusters = kmeans.fit_predict(df_processed)

# Add cluster labels to the original dataframe
df["Cluster"] = clusters

# Evaluate clustering with Silhouette Score
sil_score = silhouette_score(df_processed, clusters)
print(f"Silhouette Score: {sil_score:.3f}")

# Save the resulting file with cluster labels
output_file = "output/segmented_customers.xlsx"
df.to_excel(output_file, index=False)
print(f"Results saved to {output_file}")
# Save the resulting file with cluster labels to csv to be read by CHatGPT
output_file = "output/segmented_customers.csv"
df.to_csv(output_file, index=False, sep="\t")
print(f"Results saved to {output_file}")
