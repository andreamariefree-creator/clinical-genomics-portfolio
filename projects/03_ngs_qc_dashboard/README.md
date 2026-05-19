# Project 03: NGS QC Dashboard

## Project Overview

This project demonstrates a reproducible next-generation sequencing quality-control workflow using public FASTQ test data, FastQC, MultiQC, and Python-based dashboard reporting.

The workflow is designed to show how sequencing QC outputs can be summarized into interpretable tables and figures for sample-level review.

## Data Source

This project uses small public paired-end FASTQ test data from the Hartwig Medical Foundation public test data repository.

The raw FASTQ files are stored locally and excluded from GitHub. Processed summary tables and dashboard figures are exported to the `results/summary_tables/` and `results/figures/` folders.

## Workflow

The workflow includes:

1. Download public paired-end FASTQ test data
2. Run FastQC on FASTQ files
3. Aggregate FastQC reports using MultiQC
4. Parse MultiQC output tables in Python
5. Clean and summarize FASTQ-level QC metrics
6. Aggregate QC metrics by biological sample
7. Visualize read counts, GC content, duplication rate, and sample-level metrics
8. Interpret QC patterns and dataset limitations
9. Export summary CSV files and figures

## Command-Line QC Tools

FastQC and MultiQC were run locally before notebook analysis.

Example commands:

```bash
fastqc data/fastq/*.fastq.gz -o results/fastqc
multiqc results/fastqc -o results/multiqc

```

On Windows, FastQC may require a manual installation or wrapper script depending on the local setup.

## Key Concepts Demonstrated
FASTQ-level quality-control workflow
FastQC report generation
MultiQC aggregation
Python parsing of MultiQC output tables
FASTQ-level and sample-level QC summaries
Read count, GC content, sequence length, duplication, and FastQC failure summaries
Dashboard-style visualization
Reproducible project organization
Git/GitHub documentation workflow

## Repository Structure
projects/03_ngs_qc_dashboard/
├── data/
│   └── README.md
├── notebooks/
│   └── 03_1_ngs_qc_dashboard.ipynb
├── results/
│   ├── figures/
│   └── summary_tables/
├── src/
│   └── README.md
└── README.md

## Outputs

Processed outputs may include:

multiqc_cleaned_fastq_level_summary.csv
multiqc_sample_level_summary.csv
estimated_total_sequences_per_fastq.png
gc_content_per_fastq.png
duplicate_percentage_per_fastq.png
total_estimated_sequences_by_sample.png

Output filenames may vary slightly depending on notebook version.

## Interpretation Summary

The first notebook uses a small public test dataset with highly similar FASTQ files across samples, lanes, and read directions. This makes the dataset useful for demonstrating a reproducible QC workflow, but less useful for identifying dramatic sample-specific QC differences.

The dashboard shows that the tested files have similar read counts, GC content, sequence length, duplication rate, and FastQC failure percentage.

A companion extension notebook may later introduce a mixed-quality dataset or intentionally modified FASTQ files to demonstrate stronger QC contrasts.

## Limitations

This project uses small public test data rather than a production sequencing cohort.

The QC summaries and flags are educational and are not clinical laboratory acceptance criteria. Real clinical QC review would require assay-specific validation, laboratory-defined thresholds, instrument/run metadata, library preparation context, and downstream analysis requirements.

## Intended Use

This project is intended to demonstrate NGS QC workflow skills for educational, portfolio, and training purposes only.