import pandas as pd
import matplotlib.pyplot as plt

# load master dataset
df = pd.read_csv("data/mortality_merge.csv")

# Filter for Rwanda
rwanda = df[df["country"] == "Rwanda"].sort_values("year")

# Creating a plot
plt.figure()
plt.plot(rwanda["year"], rwanda["value_maternal"], label="Maternal mortality")
plt.plot(rwanda["year"], rwanda["value_infant"], label="Infant mortality")
plt.plot(rwanda["year"], rwanda["under5_mortality"], label="Under-5 mortality")

plt.xlabel("Year")
plt.ylabel("Mortality rate")
plt.title("Trends in Maternal and Child Mortality in Rwanda")
plt.legend()

# save figure
plt.savefig("figures/rwanda_mortality_trends.png", dpi=300, bbox_inches="tight")
plt.close()

print("Saved: figures/rwanda_mortality_trends.png")
