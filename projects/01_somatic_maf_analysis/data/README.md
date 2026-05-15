# Data

Raw or large downloaded data files are not stored in this repository.

This project uses open-access somatic mutation data from the National Cancer Institute Genomic Data Commons (GDC). Analyses currently include:

- TCGA-SKCM: skin cutaneous melanoma
- TCGA-COAD: colon adenocarcinoma

## Data Source

- Source: NCI Genomic Data Commons (GDC)
- Data Category: Simple Nucleotide Variation
- Data Type: Masked Somatic Mutation
- Experimental Strategy: WXS
- File Format: MAF / TSV
- Access Level: Open access
- Workflow Type: Aliquot Ensemble Somatic Variant Merging and Masking

## Download Instructions

Use the GDC Data Transfer Tool from the repository root to download MAF files.

## Included Manifest Files

This repository includes GDC manifest files documenting the downloaded data:

```text
gdc_manifest_skcm_maf.txt
gdc_manifest_coad_maf.txt

