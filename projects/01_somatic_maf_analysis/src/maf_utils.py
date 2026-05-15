from pathlib import Path
import pandas as pd


def find_maf_files(maf_dir):
    """
    Find compressed MAF files in a directory.

    Parameters
    ----------
    maf_dir : str or pathlib.Path
        Directory containing downloaded .maf.gz files.

    Returns
    -------
    list[pathlib.Path]
        Sorted list of MAF file paths.
    """
    maf_dir = Path(maf_dir)
    return sorted(maf_dir.rglob("*.maf.gz"))


def load_maf_files(maf_files):
    """
    Load and concatenate multiple MAF files.

    Parameters
    ----------
    maf_files : list[pathlib.Path]
        List of .maf.gz files.

    Returns
    -------
    pandas.DataFrame
        Combined MAF dataframe with a source_file column.
    """
    maf_list = []

    for file in maf_files:
        temp_maf = pd.read_csv(file, sep="\t", comment="#", low_memory=False)
        temp_maf["source_file"] = file.name
        maf_list.append(temp_maf)

    if not maf_list:
        return pd.DataFrame()

    return pd.concat(maf_list, ignore_index=True)


def summarize_maf(maf_df):
    """
    Summarize basic MAF dataset counts.
    """
    return {
        "n_variants": maf_df.shape[0],
        "n_samples": maf_df["Tumor_Sample_Barcode"].nunique(),
        "n_genes": maf_df["Hugo_Symbol"].nunique(),
    }


def mutation_classification_counts(maf_df):
    """
    Count mutation classifications.
    """
    counts = maf_df["Variant_Classification"].value_counts().reset_index()
    counts.columns = ["Variant_Classification", "Count"]
    return counts


def variant_type_counts(maf_df):
    """
    Count variant types.
    """
    counts = maf_df["Variant_Type"].value_counts().reset_index()
    counts.columns = ["Variant_Type", "Count"]
    return counts


def top_mutated_genes(maf_df, n=20):
    """
    Return the top mutated genes by mutation count.
    """
    counts = maf_df["Hugo_Symbol"].value_counts().head(n).reset_index()
    counts.columns = ["Gene", "Mutation_Count"]
    return counts


def mutation_counts_per_sample(maf_df):
    """
    Count mutation records per tumor sample.
    """
    return (
        maf_df
        .groupby("Tumor_Sample_Barcode")
        .size()
        .reset_index(name="Mutation_Count")
        .sort_values("Mutation_Count", ascending=False)
    )


def calculate_iqr_outlier_threshold(values):
    """
    Calculate an exploratory IQR-based outlier threshold.
    """
    q1 = values.quantile(0.25)
    q3 = values.quantile(0.75)
    iqr = q3 - q1
    threshold = q3 + 1.5 * iqr

    return {
        "q1": q1,
        "q3": q3,
        "iqr": iqr,
        "threshold": threshold,
    }


def filter_genes_of_interest(maf_df, genes_of_interest):
    """
    Filter a MAF dataframe for selected genes of interest.
    """
    goi_columns = [
        "Hugo_Symbol",
        "Chromosome",
        "Start_Position",
        "End_Position",
        "Reference_Allele",
        "Tumor_Seq_Allele2",
        "Variant_Classification",
        "Variant_Type",
        "Tumor_Sample_Barcode",
        "HGVSc",
        "HGVSp_Short",
        "Protein_position",
        "t_depth",
        "t_ref_count",
        "t_alt_count",
        "source_file",
    ]

    available_columns = [col for col in goi_columns if col in maf_df.columns]

    goi_variants = (
        maf_df[maf_df["Hugo_Symbol"].isin(genes_of_interest)][available_columns]
        .copy()
    )

    if {"t_depth", "t_alt_count"}.issubset(goi_variants.columns):
        goi_variants["Tumor_VAF"] = (
            goi_variants["t_alt_count"] / goi_variants["t_depth"]
        )

    return goi_variants


def summarize_genes_of_interest(goi_variants):
    """
    Summarize variant counts for selected genes of interest.
    """
    return (
        goi_variants
        .groupby("Hugo_Symbol")
        .size()
        .reset_index(name="Variant_Count")
        .sort_values("Variant_Count", ascending=False)
    )

##Potential importing method using predefined functions

## import sys
# from pathlib import Path

# project_dir = Path("..")
# src_dir = project_dir / "src"
# sys.path.append(str(src_dir))

# from maf_utils import (
    find_maf_files,
    load_maf_files,
    summarize_maf,
    mutation_classification_counts,
    variant_type_counts,
    top_mutated_genes,
    mutation_counts_per_sample,
    calculate_iqr_outlier_threshold,
    filter_genes_of_interest,
    summarize_genes_of_interest,
# )