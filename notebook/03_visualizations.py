import pandas as pd
import matplotlib.pyplot as plt

# load merged dataset
df = pd.read_csv("data/mortality_merged.csv")

# I'm selecting countries and the under-5 indicator
countries = ["Rwanda", "Kenya", "Uganda", "Tanzania"]
df_sub = df[df["country"].isin(countries)].sort_values(["country","year"])

plt.figure(figsize=(10,6))

for country in countries:
    temp = df_sub[df_sub["country"] == country]
    plt.plot(temp["year"], temp["under5_mortality"], label=country)

plt.xlabel("Year")
plt.ylabel("Under-5 mortality (per 1,000 live births)")
plt.title("Under-5 Mortality Trends in East Africa")
plt.legend()
plt.grid(True)

plt.savefig("figures/under5_east_africa.png", dpi=300, bbox_inches="tight")
plt.close()

print("Saved: figures/under5_east_africa.png")
