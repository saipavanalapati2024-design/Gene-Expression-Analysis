# Gene Expression Analysis Using Python

## Project Overview

This beginner-level bioinformatics project analyzes a demonstration gene expression CSV file and identifies the top 10 genes by average expression across five samples.

The analysis uses Pandas for data processing and Matplotlib for visualization.

## Workflow

```text
Gene Expression CSV
        |
Data Loading and Inspection
        |
Missing Value Check and Cleaning
        |
Mean Expression Calculation
        |
Gene Ranking
        |
Top 10 Gene Identification
        |
Visualization and Result Export
```

## Project Structure

```text
gene-expression-analysis/
|
|-- data/
|   `-- gene_expression.csv
|
|-- results/
|   |-- top_10_genes.csv
|   `-- top_10_genes.png
|
|-- gene_expression_analysis.py
|-- requirements.txt
`-- README.md
```

## Dataset

The input CSV contains gene identifiers and expression values for five demonstration samples. The values are intended for learning and workflow demonstration only.

## How to Run

1. Install the dependencies:

        ```bash
        py -3 -m pip install -r requirements.txt
        ```

2. Run the analysis from the project folder:

        ```bash
        py -3 gene_expression_analysis.py
        ```

The script checks missing values, removes duplicate gene identifiers, converts expression columns to numeric values, calculates each gene's mean expression, selects the top 10 genes, and saves the results.

## Outputs

- `results/top_10_genes.csv` contains the top 10 genes and their mean expression values.
- `results/top_10_genes.png` contains a bar chart of the ranked genes.

## Important Note

This is not a differential gene expression pipeline. Research-grade RNA-seq or microarray analysis requires additional quality control, normalization, statistical testing, and multiple-testing correction. The demonstration values should not be used for biological conclusions.

## Google Colab

The same workflow can be run in Google Colab by uploading `data/gene_expression.csv`, installing or importing `pandas` and `matplotlib`, and executing the analysis steps in notebook cells.

## Author

Pavan Alapati  
M.Sc. Bioinformatics and Computational Biology
