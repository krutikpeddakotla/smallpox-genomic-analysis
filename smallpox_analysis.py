import pandas as pd
import matplotlib.pyplot as plt

# Use Pandas to analyze the organizational structure of the Variola virus and
# identify the genes responsible for its extreme virulence compared to other viruses.

df = pd.read_csv("output.csv")
print(df.to_string())
#print(df.iloc[11])

#df = pd.read_csv("output.csv", index_col="Symbol")
#print(df.loc["D12L"])

# Data Cleanup 
df["Gene_Size"] = df["End"] - df["Begin"]
print(df.head())

df["% of Genome"] = df["Gene_Size"] / df["Gene_Size"].sum() * 100
print(df.head())
print(df["% of Genome"].sum())

search_terms = "polymerase|transcription"
Polymerase = df[df["Name"].str.contains(search_terms, case=False)] #case=False makes code case-insensitive
print(Polymerase.to_string())

df["Name"] = df["Name"].replace({"hypothetical protein":"uncharacterized"})
minus_proteinLength = df[(df["Orientation"].str.contains("minus", case=False)) &
                       (df["Protein length"] >= 500)]
print(minus_proteinLength.sort_values(by="Protein length", ascending=False).to_string())

orientation = df.groupby("Orientation")["Protein length"].count()
print(orientation)

name = df.groupby("Name")["Protein length"].max()
print(name)
print("---------------------------------------------")
symbol = df.groupby("Symbol")["Protein length"].max()
print(symbol.loc["B26R"])

# Visualization
plt.figure(figsize=(12,6))
plt.scatter(df["Begin"], df["Protein length"],
            alpha=0.6, color="teal", edgecolor="w", s=60)

plt.axvspan(0, 20000, color='green', alpha=0.1, label='Virulence Zone (Left)')
plt.axvspan(165000, df['End'].max(), color='green', alpha=0.1, label='Virulence Zone (Right)')
plt.title('Smallpox Architecture: Gene Position vs. Protein Length', fontsize=14)
plt.xlabel('Genomic Position (Base Pairs)', fontsize=12)
plt.ylabel('Protein Length (Amino Acids)', fontsize=12)
plt.grid(True, linestyle='--', alpha=0.5)
plt.legend()

plt.tight_layout()

plt.show()
