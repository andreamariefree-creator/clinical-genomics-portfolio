# Data

Raw downloaded sequencing data files are not stored in this repository.

This project uses small public FASTQ test data to demonstrate a reproducible NGS quality-control workflow using FastQC, MultiQC, and Python-based dashboard reporting.

## Data Source

The FASTQ files used for this project come from the Hartwig Medical Foundation public test data repository.

The `100k_reads_hiseq` test dataset contains paired-end FASTQ files for three technical test samples:

```text
TESTX
TESTY
TESTZ
```

Each sample includes two lanes and paired-end read files, resulting in 12 FASTQ files total.

## Local Data Folder

Raw FASTQ files should be stored locally in:

projects/03_ngs_qc_dashboard/data/fastq/

Downloaded test-data folders and raw FASTQ files are intentionally excluded from GitHub.

## Reproducibility Notes

FastQC was run locally on the FASTQ files, and MultiQC was used to aggregate FastQC outputs.

The notebook parses MultiQC output tables from:

projects/03_ngs_qc_dashboard/results/multiqc/multiqc_data/
Repository Data Policy

This repository does not include raw FASTQ files, downloaded test-data folders, FastQC HTML/ZIP outputs, or full MultiQC reports.

The repository includes notebooks, documentation, processed summary tables, and generated figures.

No private, employer-owned, protected health information, patient-identifiable data, or personally identifiable genomic data are included in this repository.

## Project Scope

This project is for educational and portfolio purposes only. The QC summaries are not clinical laboratory acceptance criteria and should not be used for clinical reporting.