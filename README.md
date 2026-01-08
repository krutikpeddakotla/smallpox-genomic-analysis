# Smallpox Genome: Mapping Viral Virulence
### Exploratory Data Analysis of the Variola Virus (India-1967)

## 🧬 Project Overview
This project applies Python and Pandas to analyze the 186kbp genome of the Variola virus. By mapping 197 genomic features, I identified spatial patterns that distinguish essential replication machinery from immune-evasion "attack" genes.

## 🛠️ Tech Stack
- **Language:** Python
- **Libraries:** Pandas (Data Wrangling), Matplotlib (Visualization)
- **Data Source:** NCBI (NC_001611.1)

## 📊 Key Analysis Steps
1. **Data Cleaning:** Standardized gene nomenclature and handled uncharacterized proteins.
2. **Feature Engineering:** Calculated gene density and genome occupancy percentages.
3. **Regex Filtering:** Isolated Polymerase and Transcription factors using regular expressions.
4. **Spatial Mapping:** Visualized protein complexity vs. genomic position to identify "Virulence Zones."

## 📈 Key Findings
- **Structural Outliers:** Identified B26R (1,896aa) as the primary structural scaffolding protein.
- **Virulence Clustering:** Confirmed that immune-suppressing genes (like D12L/SPICE) are concentrated in the terminal 20kbp regions.
- **Genome Efficiency:** Observed high coding density with minimal intergenic spacing.

## 🚀 How to Run
1. Clone the repo.
2. Ensure `pandas` and `matplotlib` are installed.
3. Run `python smallpox_analysis.py`.