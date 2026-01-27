import pandas as pd
import matplotlib.pyplot as plt

# Load master dataset
df = pd.read_csv("data/mortality_master.csv")

# select relevant columns
maternal = df[["country","year","value_maternal"]].dropna()

# get most recent year per country
latest_year = maternal.groupby("country")["year"].max().reset_index()
latest_maternal = maternal.merge(latest_year, on=["country","year"])

#Sort by maternal mortality
latest_maternal = latest_maternal.sort_values("value_maternal", ascending=False)

top10 = latest_maternal.head(10)
bottom10 = latest_maternal.tail(10)

# plot top 10 countries
plt.figure(figsize=(10,6))
plt.barh(top10["country"], top10["value_maternal"], color="salmon")
plt.xlabel("Maternal Mortality (per 100,000 live births)")
plt.title(f"Top 10 Countries with Highest Maternal Mortality ({top10['year'].iloc[0]})")
plt.gca().invert_yaxis()  # largest at top
plt.grid(axis="x")
plt.tight_layout()
plt.savefig("figures/top10_maternal.png")
plt.close()

# Plot bottom 10
plt.figure(figsize=(10,6))
plt.barh(bottom10["country"], bottom10["value_maternal"], color="lightgreen")
plt.xlabel("Maternal Mortality (per 100,000 live births)")
plt.title(f"Top 10 Countries with Lowest Maternal Mortality ({bottom10['year'].iloc[0]})")
plt.gca().invert_yaxis()
plt.grid(axis="x")
plt.tight_layout()
plt.savefig("figures/bottom10_maternal.png")
plt.close()

print("Saved: top10_maternal.png and bottom10_maternal.png")
