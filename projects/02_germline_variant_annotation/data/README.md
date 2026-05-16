# Data

Raw downloaded data files are not stored in this repository.

This project uses public ClinVar variant summary data from the National Center for Biotechnology Information (NCBI). The raw ClinVar file is kept locally and excluded from GitHub because it is a large downloaded reference file.

## Data Source

- Source: NCBI ClinVar
- File used: `variant_summary.txt.gz`
- Format: compressed tab-delimited text file
- Access level: public
- Primary use in this project: germline variant annotation, clinical significance summarization, review status assessment, and educational prioritization

## Local Data Folder

The downloaded ClinVar file should be stored locally in:

```text
projects/02_germline_variant_annotation/data/clinvar/variant_summary.txt.gz