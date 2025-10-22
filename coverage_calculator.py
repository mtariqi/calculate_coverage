# Write a Python function that calculates the coverage of 10 million paired-end Illumina reads, 150bp long, for a yeast genome 5 Mbp long.
# Here is a clean, reusable Python function for any input:

"""
coverage_calculator.py
Author: Md Tariqul Islam
NUID: 002505253
Description:
    A simple Python function to calculate genome coverage
    for paired-end Illumina sequencing data.

Formula:
    Coverage (X) = (2 * num_pairs * read_length) / genome_size
"""

def calculate_coverage(num_pairs, read_length, genome_size):
    """
    Calculate sequencing coverage for paired-end reads.

    Parameters:
        num_pairs (int): Number of paired-end read pairs
        read_length (int): Length of each read (bp)
        genome_size (int): Size of the genome (bp)

    Returns:
        float: Sequencing coverage (X)
    """
    total_bases = 2 * num_pairs * read_length  # two reads per pair
    coverage = total_bases / genome_size
    return coverage

# Example: 10 million paired-end reads, 150 bp, yeast genome 5 Mb
if __name__ == "__main__":
    coverage = calculate_coverage(num_pairs=10_000_000, read_length=150, genome_size=5_000_000)
    print(f"Expected coverage: {coverage:.1f}x")
