import pandas as pd

#1. CREATING A DATAFRAME

df = pd.read_csv('data/infant_mortality.csv', sep=',', skiprows=4)

#2. TAKING A LOOK AT DATAFRAME

df.head()

#3. CLEANING DATA 
   
      # renaming the columns

df= df.rename(columns={ 'Country Name':'country',
                       'Country Code':'country_code',
                       'Indicator Name':'indicator',
                       'Indicator Code':'indicator_code' } )

     # Identifying the years columns

year_cols = [c for c in df.columns if c.isdigit()]

     # keep relevant columns

df = df[["country", "country_code", "indicator"] + year_cols]

     # changing from wide to long format

df.melt(id_vars=['country','country_code','indicator','indicator_code'], var_name='year', value_name='value')
df_long= df.melt(id_vars=['country','country_code','indicator','indicator_code'], var_name='year', value_name='value')

    # remove null values

df_long.dropna()
df= df_long.dropna()

    # checking the data types of columns

df.dtypes

    # changing the 'year' column to integer

df['year'].astype(int)
df['year']= df['year'].astype(int)

    # save cleaned data
df_long.to_csv(
    "data/infant_mortality_clean.csv",
    index=False )
