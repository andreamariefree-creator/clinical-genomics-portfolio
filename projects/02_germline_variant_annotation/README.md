# Project 02: Germline Variant Annotation Using ClinVar

## Project Overview

This project analyzes public ClinVar variant summary data to demonstrate a reproducible germline variant annotation workflow.

The workflow uses a selected clinical gene panel spanning multiple areas of germline genetics, including hereditary breast and ovarian cancer, Lynch syndrome and colorectal cancer predisposition, familial hypercholesterolemia, cardiomyopathy, cystic fibrosis, and hereditary hearing loss.

The project is designed for educational and portfolio purposes. It does not perform clinical variant classification and should not be used for diagnosis, treatment decisions, or clinical reporting.

## Data Source

This project uses the public NCBI ClinVar `variant_summary.txt.gz` file.

The raw downloaded ClinVar file is stored locally and excluded from GitHub. Processed summary outputs are exported to the `results/` folder.

These genes were selected to represent clinically recognizable germline testing contexts, including hereditary cancer, cardiovascular genetics, cystic fibrosis, and hearing loss.

## Analysis Workflow

The notebook performs the following steps:

Load the public ClinVar variant_summary.txt.gz dataset
Select clinically relevant annotation columns
Filter records to the GRCh38 assembly
Filter to a selected germline clinical gene panel
Summarize ClinVar records by gene
Summarize clinical significance labels
Identify pathogenic and likely pathogenic records
Calculate pathogenic/likely pathogenic representation by gene
Summarize ClinVar review status
Create an educational ClinVar-based prioritization score
Assign educational priority tiers
Generate record-level and unique variant-level prioritization tables
Export summary CSV files and figures
Key Concepts Demonstrated
Public clinical genomics data analysis
ClinVar variant summary parsing
Germline gene panel filtering
Clinical significance summarization
Review status assessment
Pathogenic/likely pathogenic variant record summaries
Record-level versus unique variant-level analysis
Educational variant prioritization
Reproducible notebook-based workflow
Git/GitHub project organization

## Repository Structure
projects/02_germline_variant_annotation/
├── data/
│   └── README.md
├── notebooks/
│   └── 02_1_clinvar_germline_variant_annotation.ipynb
├── results/
├── src/
│   └── README.md
└── README.md

## Outputs

The workflow exports processed summary files to the results/ folder. Outputs may include:

clinvar_gene_panel_counts.csv
clinvar_clinical_significance_counts.csv
clinvar_clinsig_simple_counts.csv
clinvar_gene_clinsig_counts.csv
clinvar_pathogenic_likely_pathogenic_by_gene.csv
clinvar_gene_pathogenic_summary.csv
clinvar_review_status_counts.csv
clinvar_pathogenic_review_status_counts.csv
clinvar_pathogenic_review_status_by_gene.csv
clinvar_educational_variant_priority_table.csv
clinvar_educational_priority_tier_counts.csv
clinvar_educational_priority_by_gene.csv
clinvar_educational_unique_variant_priority_table.csv

Depending on the notebook version, exported filenames may vary slightly.

## Interpretation Summary

This project demonstrates how public ClinVar annotations can be organized into an interpretable germline variant annotation workflow.

The selected gene panel contains many records across uncertain, conflicting, benign, likely benign, pathogenic, and likely pathogenic categories. This highlights the importance of variant-level review rather than assuming that all variants in a clinically important gene have the same significance.

The educational prioritization table ranks ClinVar records using submitted clinical significance, review status, and gene context. Higher-priority records are enriched for pathogenic or likely pathogenic interpretations with stronger review status, while lower-priority records include uncertain, conflicting, benign, or lower-review annotations.

The workflow also distinguishes record-level ClinVar data from unique variant-level summaries by creating a deduplicated table using ClinVar VariationID.

## Limitations

This project does not perform independent ACMG/AMP clinical classification.

The educational priority tiers are not diagnostic conclusions. True clinical variant classification would require structured evidence review, disease-specific gene validity, inheritance context, phenotype correlation, population frequency thresholds, segregation data, functional evidence, laboratory validation, and expert review.

ClinVar annotations may change over time as new submissions and evidence are added. Results should be interpreted as a snapshot of the downloaded ClinVar file used at the time of analysis.

## Intended Use

This project is intended to demonstrate clinical genomics data analysis skills for educational, portfolio, and training purposes only.

## Selected Gene Panel

The analysis focuses on the following genes:

```text
BRCA1, BRCA2,
MLH1, MSH2, MSH6, PMS2, EPCAM, APC, MUTYH,
LDLR, APOB, PCSK9,
MYH7, MYBPC3, TNNT2, TNNI3,
CFTR,
GJB2