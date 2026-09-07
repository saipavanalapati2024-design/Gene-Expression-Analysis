"""Identify the top 10 highly expressed genes in a CSV dataset."""

from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd


PROJECT_ROOT = Path(__file__).resolve().parent
DATA_FILE = PROJECT_ROOT / "data" / "gene_expression.csv"
RESULTS_DIR = PROJECT_ROOT / "results"


def main() -> None:
    RESULTS_DIR.mkdir(exist_ok=True)

    data = pd.read_csv(DATA_FILE)
    if "Gene" not in data.columns:
        raise ValueError("The input CSV must contain a 'Gene' column.")

    expression_columns = [column for column in data.columns if column != "Gene"]
    if not expression_columns:
        raise ValueError("The input CSV must contain at least one sample column.")

    data[expression_columns] = data[expression_columns].apply(
        pd.to_numeric, errors="coerce"
    )
    data = data.drop_duplicates(subset="Gene")
    data["Mean_Expression"] = data[expression_columns].mean(axis=1)
    ranked_genes = data.dropna(subset=["Mean_Expression"]).sort_values(
        by="Mean_Expression", ascending=False
    )
    top_10_genes = ranked_genes.head(10)[["Gene", "Mean_Expression"]]

    output_file = RESULTS_DIR / "top_10_genes.csv"
    top_10_genes.to_csv(output_file, index=False)

    chart = top_10_genes.sort_values("Mean_Expression")
    plt.figure(figsize=(10, 6))
    plt.barh(chart["Gene"], chart["Mean_Expression"], color="#2878b5")
    plt.xlabel("Mean expression")
    plt.ylabel("Gene")
    plt.title("Top 10 Highly Expressed Genes")
    plt.tight_layout()
    plot_file = RESULTS_DIR / "top_10_genes.png"
    plt.savefig(plot_file, dpi=300)
    plt.close()

    print(f"Dataset shape: {data.shape[0]} genes x {len(expression_columns)} samples")
    print("\nTop 10 expressed genes:\n")
    print(top_10_genes.to_string(index=False))
    print(f"\nSaved table: {output_file}")
    print(f"Saved plot: {plot_file}")


if __name__ == "__main__":
    main()
