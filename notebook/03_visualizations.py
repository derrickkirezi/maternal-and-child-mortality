import pandas as pd
import matplotlib.pyplot as plt

# load master dataset
df = pd.read_csv("data/mortality_merged.csv")

# Filter for Rwanda
rwanda = df[df["country"] == "Rwanda"].sort_values("year")

# Creating a plot
fig, ax1 = plt.subplots()

# Left axis: infant & under-5
ax1.plot(rwanda["year"], rwanda["value_infant"], label="Infant mortality")
ax1.plot(rwanda["year"], rwanda["under5_mortality"], label="Under-5 mortality")
ax1.set_xlabel("Year")
ax1.set_ylabel("Mortality rate (per 1,000 live births)")

# right axis: maternal
ax2 = ax1.twinx()
ax2.plot(rwanda["year"], rwanda["value_maternal"], linestyle="--", label="Maternal mortality")
ax2.set_ylabel("Maternal mortality (per 100,000 live births)")

# Title
plt.title("Trends in Maternal and Child Mortality in Rwanda")

# legends
lines_1, labels_1 = ax1.get_legend_handles_labels()
lines_2, labels_2 = ax2.get_legend_handles_labels()
ax1.legend(lines_1 + lines_2, labels_1 + labels_2)

# save figure
plt.savefig("figures/rwanda_mortality_trends.png", dpi=300, bbox_inches="tight")
plt.close()

print("Saved: figures/rwanda_mortality_trends.png")
