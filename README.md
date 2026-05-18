# Clinical Genomics and Molecular Bioinformatics Portfolio

This repository contains independent portfolio projects focused on clinical genomics, molecular diagnostics, variant annotation, oncology genomics, and NGS quality-control workflows.

## Background

I am a molecular biology technician and computational biologist with experience in PCR-based workflows, molecular assay development, biological data analysis, Python, R, SQL, and translational research. This portfolio is intended to demonstrate practical skills relevant to clinical genomics, molecular diagnostics, and bioinformatics-adjacent laboratory roles.

## Portfolio Projects

### 01. Somatic MAF Analysis

Analysis of open-access cancer mutation data using Mutation Annotation Format files. This project focuses on mutation burden, recurrently altered genes, variant classes, and oncology-relevant variant prioritization.

## Overview

This portfolio documents projects in clinical genomics, cancer genomics, molecular diagnostics, and computational biology. The goal is to demonstrate practical skills in public biomedical data analysis, reproducible coding workflows, clinical genomics interpretation, and biologically grounded data storytelling.

The projects are designed to reflect a transition from molecular biology laboratory work into clinical computational genomics and bioinformatics.

## Technical Skills Demonstrated

- Python-based biomedical data analysis
- Pandas data cleaning and transformation
- Mutation Annotation Format (MAF) file analysis
- Public cancer genomics data acquisition from the NCI Genomic Data Commons
- Reproducible project organization
- Git and GitHub version control
- Markdown documentation
- Exploratory clinical genomics interpretation
- Data visualization and summary table generation

### MAF Analysis

This project analyzes open-access somatic mutation data from The Cancer Genome Atlas (TCGA) using Mutation Annotation Format (MAF) files downloaded from the National Cancer Institute Genomic Data Commons (GDC).

The project currently includes two cancer-specific analyses:

1. **TCGA-SKCM skin cutaneous melanoma**
2. **TCGA-COAD colon adenocarcinoma**

The analysis workflow includes:

- loading and concatenating downloaded MAF files
- summarizing mutation classifications and variant types
- identifying recurrently mutated genes
- calculating mutation counts per tumor sample
- flagging high-mutation outlier samples
- exploring selected cancer-relevant and immunotherapy/MSI-related genes
- exporting reproducible CSV outputs and figures

#### Clinical Genomics Relevance

The SKCM analysis emphasizes melanoma biology, mutation burden, and immunotherapy-relevant genes such as `BRAF`, `NRAS`, `NF1`, `B2M`, `JAK1`, and `JAK2`.

The COAD analysis emphasizes colorectal cancer driver biology, mismatch repair/MSI-related genes, polymerase proofreading genes, and hypermutation concepts, including genes such as `APC`, `TP53`, `KRAS`, `BRAF`, `PIK3CA`, `MLH1`, `MSH2`, `MSH6`, `PMS2`, `POLE`, and `POLD1`.

This project is intended to show how public cancer genomics data can be transformed into clinically oriented exploratory analyses while maintaining clear limitations around non-clinical use.

[View Project 01](projects/01_somatic_maf_analysis/)

### Project 02: Germline Variant Annotation Using ClinVar

This project analyzes public NCBI ClinVar variant summary data to demonstrate a reproducible germline variant annotation workflow.

The project focuses on a selected clinical gene panel representing hereditary breast and ovarian cancer, Lynch syndrome and colorectal cancer predisposition, familial hypercholesterolemia, cardiomyopathy, cystic fibrosis, and hereditary hearing loss.

The analysis workflow includes:

- loading the public ClinVar `variant_summary.txt.gz` dataset
- filtering records to GRCh38
- filtering to a selected germline clinical gene panel
- summarizing ClinVar records by gene
- summarizing clinical significance labels
- identifying pathogenic and likely pathogenic records
- summarizing ClinVar review status
- creating an educational ClinVar-based prioritization score
- generating record-level and unique variant-level prioritization tables
- exporting reproducible summary outputs

#### Clinical Genomics Relevance

This project demonstrates how public clinical genomics annotations can be organized into an interpretable workflow for germline variant review.

The workflow emphasizes the difference between gene-level relevance and variant-level interpretation. Clinically important genes can contain pathogenic, likely pathogenic, uncertain, conflicting, benign, and likely benign records, which reinforces the need for structured variant-level review.

The educational prioritization table is not a clinical classification. It is intended to demonstrate how ClinVar annotations, review status, and gene context can be used to organize public variant records for exploratory analysis.

[View Project 02](projects/02_germline_variant_annotation/)

### 03. NGS QC Dashboard (In Development)

Prototype sequencing quality-control dashboard for evaluating sample and run-level metrics relevant to targeted sequencing workflows.

### 04. Variant SQL Database (In Development)

SQLite-based system for storing, querying, and filtering variant annotation data in a reproducible format.

## Skills Demonstrated

- Python
- pandas
- SQL / SQLite
- Jupyter notebooks
- VCF/MAF-style genomic data
- Variant annotation concepts
- Germline and somatic variant interpretation concepts
- NGS QC metrics
- Reproducible analysis documentation
- Clinical genomics workflow design
- ClinVar variant summary analysis
- Germline variant annotation
- Clinical significance label summarization
- Review status and evidence-confidence assessment
- Educational variant prioritization
- Record-level versus unique variant-level data handling

## Disclaimer

These projects are for educational and portfolio purposes only. They are not intended for clinical diagnosis, treatment decisions, or patient reporting.

## Repository Structure for Projects 1 and 2

```text
clinical-genomics-portfolio/
├── docs/
├── projects/
│   ├── 01_somatic_maf_analysis/
│   │   ├── data/
│   │   ├── notebooks/
│   │   ├── results/
│   │   ├── src/
│   │   └── README.md
│   ├── 02_germline_variant_annotation/
│   │   ├── data/
│   │   ├── notebooks/
│   │   ├── results/
│   │   ├── src/
│   │   └── README.md
│   ├── 03_ngs_qc_dashboard/
│   └── 04_variant_sql_database/
├── resources/
├── README.md
├── requirements.txt
└── environment.yml

