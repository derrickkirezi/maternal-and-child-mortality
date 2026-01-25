import pandas as pd

#1. CREATING A DATAFRAME

df3 = pd.read_csv('data/under5_mortality.csv', sep=',', skiprows=4)

#2. TAKING A LOOK AT DATAFRAME

df3.head()

#3. CLEANING DATA 
   
      # A. renaming the columns

df3= df3.rename(columns={ 'Country Name':'country',
                       'Country Code':'country_code',
                       'Indicator Name':'indicator',
                       'Indicator Code':'indicator_code' } )

     # B. identifying the years columns

year_cols = [c for c in df3.columns if c.isdigit()]

     # C. changing from wide to long format

df3.melt(id_vars=['country','country_code','indicator','indicator_code'], var_name='year', value_name='value')
df3_long= df3.melt(id_vars=['country','country_code','indicator','indicator_code'], var_name='year', value_name='value')

    # D. removing null values

df3_long.dropna()
df3= df3_long.dropna()

    # E. checking the data types of columns

df3.dtypes

    # F. changing the 'year' column to integer for future calculations

df3['year'].astype(int)
df3['year']= df3['year'].astype(int)
