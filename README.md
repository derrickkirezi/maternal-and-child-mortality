# Maternal and Child Mortality Analysis

## Overview

This project analyzes maternal, infant, and under-5 mortality trends across countries using publicly available datasets. The goal is to compare under-5 children mortality rates between East African states, analyse the top/bottom maternal mortality rates across the world, then provide insights.

The analysis was done using Python, Pandas, and Matplotlib, with cleaned and merged datasets prepared for visualization.

## Datasets

Maternal Mortality – Maternal deaths per 100,000 live births
Infant Mortality – Infant deaths per 1,000 live births
Under-5 Mortality – Deaths of children under 5 per 1,000 live births

All datasets were downloaded from the World Bank/UN public health repositories and cleaned for analysis.

## Tools & Libraries

`Python 3`
`Pandas (data cleaning and manipulation)`
`Matplotlib (visualizations)`
`Jupyter/Colab notebooks`

## Project structure

── `data/`                            # data files
   ├── raw 
     ├── maternal_mortality.csv
     ├── infant_mortality.csv
     └── under5_mortality.csv
   ├── cleaned     
     ├── maternal_mortality_clean.csv
     ├── infant_mortality_clean.csv
     ├── under5_mortality_clean.csv
     └── mortality_merged.csv
── `notebook/`                        # Scripts
    ├── 01_datacleaning/          
    ├── 02_merge_datasets.py      
    └── 03_visualizations/
── `figures/  `                       # generated visualizations
    ├── under5_trends_east_africa.png
    ├── top10_under5_improvement.png
    ├── top10_maternal.png
    └── bottom10_maternal.png
── `README.md`

## Insights

    Under-5 Mortality Trends in East Africa

Steady decline is observed in Rwanda, Kenya, Uganda, and Tanzania over the last two decades. 
In 1994, the rates spiked most likely because of the Genocide against the Tutsi.
After 1994, Rwanda shows the biggest improvement, reflecting effective child health policies.

    Maternal Mortality 

I observed that huge contrasts exist globally.
Top 10 countries have maternal mortality above 400 per 100,000 live births, while the lowest 10 are below 50. 
It's worth noting that 80% of the countries in top 10 highest mortality rates are from Africa, indicating weak health systems.
