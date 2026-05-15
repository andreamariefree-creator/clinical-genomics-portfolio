# Clinical Genomics and Molecular Bioinformatics Portfolio

This repository contains independent portfolio projects focused on clinical genomics, molecular diagnostics, variant annotation, oncology genomics, and NGS quality-control workflows.

## Background

I am a molecular biology technician and computational biologist with experience in PCR-based workflows, molecular assay development, biological data analysis, Python, R, SQL, and translational research. This portfolio is intended to demonstrate practical skills relevant to clinical genomics, molecular diagnostics, and bioinformatics-adjacent laboratory roles.

## Portfolio Projects

### 01. Somatic MAF Analysis

Analysis of open-access cancer mutation data using Mutation Annotation Format files. This project focuses on mutation burden, recurrently altered genes, variant classes, and oncology-relevant variant prioritization.

# Clinical Genomics Portfolio

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

## Featured Project

### Project 01: Somatic MAF Analysis

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

### 02. Germline Variant Annotation

Educational workflow for parsing and annotating VCF-style variant data using public resources such as ClinVar-style clinical significance fields, population frequency, variant consequence, and candidate variant prioritization.

### 03. NGS QC Dashboard

Prototype sequencing quality-control dashboard for evaluating sample and run-level metrics relevant to targeted sequencing workflows.

### 04. Variant SQL Database

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

## Disclaimer

These projects are for educational and portfolio purposes only. They are not intended for clinical diagnosis, treatment decisions, or patient reporting.

## Repository Structure for Project 01

```text
clinical-genomics-portfolio/
├── docs/
├── projects/
│   └── 01_somatic_maf_analysis/
│       ├── data/
│       ├── notebooks/
│       ├── results/
│       └── README.md
├── resources/
├── README.md
├── requirements.txt
└── environment.yml

