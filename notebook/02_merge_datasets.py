import pandas as pd

# Load cleaned datasets
maternal = pd.read_csv("data/maternal_mortality_clean.csv")
infant = pd.read_csv("data/infant_mortality_clean.csv")
under5 = pd.read_csv("data/under5_mortality_clean.csv")

# Merge step 1: maternal + infant
df = pd.merge(maternal, infant,
              on=["country","country_code","year"],
              how="outer",
              suffixes=("_maternal","_infant"))

# Merge step 2: add under5
df = pd.merge(df, under5,
              on=["country","country_code","year"],
              how="outer")

# Rename under5 column
df = df.rename(columns={"value":"under5_mortality"})

# Optional: reorder columns
df = df[["country","country_code","year","value_maternal","value_infant","under5_mortality"]]

# Save master table
df.to_csv("data/mortality_merged.csv", index=False)

print("Saved: data/mortality_merged.csv")
