# Somatic MAF Analysis

## Purpose

This project analyzes open-access somatic cancer mutation data in Mutation Annotation Format (MAF) to summarize mutation patterns, identify recurrently altered genes, and practice oncology-focused variant prioritization.

## Clinical Genomics Relevance

Somatic MAF files are commonly used in cancer genomics research and can support workflows related to molecular oncology, biomarker discovery, targeted therapy relevance, and tumor mutation profiling.

## Planned Workflow

1. Load and inspect an open-access MAF file.
2. Summarize mutation classes and variant types.
3. Identify frequently mutated genes.
4. Calculate mutation counts per sample.
5. Prioritize variants in selected oncology-relevant genes.
6. Export summary tables and figures.

## Skills Demonstrated

- Python
- pandas
- cancer genomics data analysis
- MAF file structure
- somatic variant interpretation concepts
- reproducible notebook documentation

## Limitations

This project is for educational and portfolio purposes only. It does not use private patient data and is not intended for diagnosis, treatment decisions, or clinical reporting.

## Part 1: TCGA-SKCM Melanoma Analysis

The SKCM analysis combines open-access GDC masked somatic mutation MAF files and summarizes mutation classifications, recurrently altered genes, mutation counts per sample, outlier/high-mutation samples, and selected melanoma/immunotherapy-relevant genes. The SKCM analysis combined 150 downloaded open-access GDC masked somatic mutation MAF files into a single working dataset containing 85,981 mutation records across 150 tumor samples.

Initial results showed that missense mutations were the most common mutation classification, followed by silent mutations and nonsense mutations. SNPs accounted for the large majority of variant types.

The top recurrently mutated genes included TTN, MUC16, DNAH5, PCLO, LRP1B, and BRAF. A focused melanoma/immunotherapy gene subset identified recurrent variants in BRAF, NF1, NRAS, TP53, CDKN2A, PTEN, KIT, JAK1, JAK2, and B2M.

An exploratory IQR-based outlier analysis identified 14 samples with unusually high mutation counts. These high-mutation samples may be useful for later exploration of hypermutation and tumor mutational burden-style biomarker concepts.

### Current Outputs

- `skcm_mutation_classification_counts.csv`
- `skcm_variant_type_counts.csv`
- `skcm_top_mutated_genes.csv`
- `skcm_mutation_counts_per_sample.csv`
- `skcm_hypermutated_outlier_samples.csv`
- `skcm_genes_of_interest_variant_table.csv`
- `skcm_genes_of_interest_variant_summary.csv`

### Clinical Genomics Relevance

This analysis demonstrates how public somatic mutation data can be used to explore tumor mutation patterns, melanoma-associated driver genes, and immune escape-related genes. Mutation count per sample is treated as an exploratory TMB-style proxy, not a clinically validated TMB calculation.