# Gene Expression Analysis

This project analyzes a sample gene-expression CSV and identifies the top 10 expressed genes by average expression across all sample columns.

## Method

1. Load `data/gene_expression.csv`.
2. Convert sample values to numeric values.
3. Remove duplicate gene identifiers.
4. Calculate the mean expression for each gene.
5. Sort genes from highest to lowest mean expression.
6. Save the top 10 genes as a CSV table and a bar chart.

## Run

From this project folder:

```text
py -3 -m pip install -r requirements.txt
py -3 gene_expression_analysis.py
```

## Outputs

- `results/top_10_genes.csv`: ranked genes and mean expression values.
- `results/top_10_genes.png`: visualization of the ranking.

This is a descriptive expression-ranking exercise, not a differential-expression analysis. Research-grade RNA-seq analysis would additionally require quality control, normalization, statistical testing, and multiple-testing correction.
