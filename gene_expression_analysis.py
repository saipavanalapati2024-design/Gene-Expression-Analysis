"""Identify the top 10 highly expressed genes in a CSV dataset."""

from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd


PROJECT_ROOT = Path(__file__).resolve().parent
DATA_FILE = PROJECT_ROOT / "data" / "gene_expression.csv"
RESULTS_DIR = PROJECT_ROOT / "results"


def main():
    RESULTS_DIR.mkdir(exist_ok=True)

    df = pd.read_csv(DATA_FILE)

    print("\n========== DATASET INFORMATION ==========\n")
    print("Dataset shape:", df.shape)
    print("\nFirst 5 rows:")
    print(df.head())
    print("\nColumn names:")
    print(df.columns.tolist())

    print("\n========== MISSING VALUES ==========\n")
    print(df.isnull().sum())

    df = df.drop_duplicates(subset="Gene")
    expression_columns = df.columns[1:]
    df[expression_columns] = df[expression_columns].apply(
        pd.to_numeric, errors="coerce"
    )
    df["Mean_Expression"] = df[expression_columns].mean(axis=1)

    ranked_genes = df.sort_values(
        by="Mean_Expression", ascending=False
    )
    top_10_genes = ranked_genes.head(10)
    selected_columns = ["Gene", "Mean_Expression"]

    print("\n========== TOP 10 EXPRESSED GENES ==========\n")
    print(top_10_genes[selected_columns].to_string(index=False))

    output_file = RESULTS_DIR / "top_10_genes.csv"
    top_10_genes[selected_columns].to_csv(output_file, index=False)
    print("\nTop 10 results saved to:", output_file)

    plt.figure(figsize=(10, 6))
    plt.bar(top_10_genes["Gene"], top_10_genes["Mean_Expression"])
    plt.xlabel("Gene")
    plt.ylabel("Mean Expression")
    plt.title("Top 10 Highly Expressed Genes")
    plt.xticks(rotation=45)
    plt.tight_layout()

    plot_file = RESULTS_DIR / "top_10_genes.png"
    plt.savefig(plot_file, dpi=300)
    plt.close()
    print("Plot saved to:", plot_file)

    print("\n========== ANALYSIS COMPLETED ==========")
    print("Total genes analyzed:", len(df))
    print("Top 10 genes identified successfully.")
    print("\nResults available in the 'results' folder.")


if __name__ == "__main__":
    main()
