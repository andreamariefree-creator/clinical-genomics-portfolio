# Project 01: Somatic MAF Analysis
## Purpose

This project analyzes open-access somatic cancer mutation data in Mutation Annotation Format (MAF) to summarize mutation patterns, identify recurrently altered genes, and practice oncology-focused variant prioritization.

## Clinical Genomics Relevance

Somatic MAF files are commonly used in cancer genomics research and can support workflows related to molecular oncology, biomarker discovery, targeted therapy relevance, and tumor mutation profiling.

## Project Overview

This project analyzes open-access somatic mutation data from The Cancer Genome Atlas (TCGA) using Mutation Annotation Format (MAF) files downloaded from the National Cancer Institute Genomic Data Commons (GDC).

The project is divided into two cancer-specific analyses:

1. TCGA-SKCM skin cutaneous melanoma
2. TCGA-COAD colon adenocarcinoma

The goal is to practice clinically oriented cancer genomics analysis by summarizing mutation classifications, variant types, recurrently mutated genes, mutation counts per sample, high-mutation outlier samples, and selected genes of clinical or biological interest.

This project is for educational and portfolio purposes only. It is not intended for diagnosis, treatment decisions, or clinical reporting.

## Part 1: TCGA-SKCM Melanoma Analysis

The SKCM analysis combines open-access GDC masked somatic mutation MAF files and summarizes mutation patterns across melanoma tumor samples.

This analysis focuses on:

- melanoma-associated recurrently mutated genes
- mutation classifications and variant types
- mutation counts per tumor sample
- high-mutation outlier samples
- melanoma and immunotherapy-relevant genes

Genes of interest include `BRAF`, `NRAS`, `NF1`, `KIT`, `TP53`, `PTEN`, `CDKN2A`, `B2M`, `JAK1`, and `JAK2`.

## Part 2: TCGA-COAD Colon Adenocarcinoma Analysis

The COAD analysis combines open-access GDC masked somatic mutation MAF files and summarizes mutation patterns across colon adenocarcinoma tumor samples.

This analysis focuses on:

- colorectal cancer driver genes
- mismatch repair and MSI-relevant genes
- polymerase proofreading-associated genes
- mutation burden heterogeneity
- high-mutation outlier samples

Genes of interest include `APC`, `TP53`, `KRAS`, `BRAF`, `PIK3CA`, `SMAD4`, `MLH1`, `MSH2`, `MSH6`, `PMS2`, `POLE`, and `POLD1`.

## Methods Summary

For each cancer type, compressed MAF files were downloaded locally using a GDC manifest and the GDC Data Transfer Tool. The MAF files were concatenated into a single dataframe for analysis.

The workflow includes:

1. Loading and concatenating downloaded MAF files
2. Inspecting dataset structure
3. Counting variants, samples, and mutated genes
4. Summarizing mutation classifications
5. Summarizing variant types
6. Identifying top mutated genes
7. Calculating mutation counts per tumor sample
8. Identifying high-mutation outliers using an exploratory IQR-based threshold
9. Summarizing variants in selected genes of interest
10. Exporting summary tables and figures

## Repository Structure

```text
projects/01_somatic_maf_analysis/
├── data/
│   ├── README.md
│   ├── gdc_manifest_skcm_maf.txt
│   └── gdc_manifest_coad_maf.txt
├── notebooks/
│   ├── 01_1_skcm_somatic_maf_analysis.ipynb
│   └── 01_2_coad_somatic_maf_analysis.ipynb
├── results/
│   ├── skcm/
│   └── coad/
└── README.md

## Data Policy
Downloaded MAF files are not stored in this GitHub repository. They are kept locally and ignored using .gitignore.

The repository includes documentation, manifests, notebooks, summary tables, and figures, but not large downloaded mutation data files.

No private, employer-owned, protected health information, or patient-identifiable data are included in this repository.

##Limitations
Mutation counts per sample are used as simplified exploratory tumor mutational burden-style proxies. They are not clinically validated TMB values.

Clinically reportable TMB would require normalization to a validated assay footprint or callable genomic territory, quality-control thresholds, and laboratory-specific validation.

High-mutation outliers are exploratory and are not classified as MSI-high, mismatch repair-deficient, or polymerase proofreading-deficient based on these notebooks alone. Confirming those categories would require additional molecular, clinical, or orthogonal annotation data.