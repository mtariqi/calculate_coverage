# 🧬 Sequencing Coverage Calculator

A simple and efficient **Python tool** for calculating genome sequencing coverage for paired-end Illumina reads.

---

## 📘 Overview

This project helps compute the **sequencing coverage (depth)** based on:
- Number of read pairs  
- Read length (in base pairs)  
- Genome size (in base pairs)

This is useful for **planning sequencing experiments** or **validating yield** in genomics research.

**Formula:**

\[
\text{Coverage (X)} = \frac{2 \times \text{num_pairs} \times \text{read_length}}{\text{genome_size}}
\]

---

## 🚀 Usage

### 1️⃣ Clone the repository
```bash
git clone https://github.com/mtariqi/calculate_coverage.git
cd calculate_coverage

## 2️⃣ Run the script

python3 coverage_calculator.py


## 3️⃣ Example output.
Expected coverage: 600.0x

## 🧪 Testing

You can verify the calculation using the included test file:

python3 test_coverage_calculator.py

## ⚙️ Function Reference

calculate_coverage(num_pairs, read_length, genome_size)

## Parameters:

-- num_pairs (int): Number of paired-end reads

-- read_length (int): Read length in base pairs

-- genome_size (int): Genome size in base pairs

Returns:

-- Sequencing coverage (float)

## License

This project is released under the MIT License.

## ✨ Example (Yeast Genome)


from coverage_calculator import calculate_coverage

coverage = calculate_coverage(
    num_pairs=10_000_000,
    read_length=150,
    genome_size=5_000_000
)
print(f"Expected coverage: {coverage:.1f}x")


## Output:

Expected coverage: 600.0x


