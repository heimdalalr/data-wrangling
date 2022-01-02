import pandas as pd
import numpy as np
from pandas.io.formats.format import return_docstring

df = pd.read_csv('Film_Locations.csv')

# print(df.shape)
print(df.info())
# print(df.head())
# print(df.tail())

# print(df.describe())
# print(df.mean())
# print(df['Release Year'].max())


# Step 2: Select, Filter, Sort
# Using dataframes in pandas, write 2-3 functions that filter and sort your dataset. Another example: write a function that sorts the rows alphabetically based on a texual column.

# write a function that produces a subset of data that inclues a numeric value that is higher than average
def find_above_avg_year():
    avg = df['Release Year'].mean()
    return df[ df['Release Year'] > avg]

# print(find_above_avg_year())

# write a function that sorts the rows alpabetically based on a textual column.
def sort_by_locale():
    columns = df[['Locations', 'Fun Facts', 'Production Company', 'Director', 'Actor 1']]
    return columns.sort_values(by='Locations', ascending=True)

# print(sort_by_locale())


# Step 3: Clean Data
# Identify whether your dataset has any missing or null value using pandas. If there are null values in a numeric column, determine whether you should remove the data, or if there is a reasonable replacement for null, such as replacing it with a 0 value. Additionally, identify if there are any low/high outliers in your dataset using pandas.

#detect missing values
# print(df.isnull())
#will show true if any missing values appear in the column and false if all items are filled in with a value
print(df.isnull())
#detect if any column is completely empty, would come up as True if empty
print(df.isnull().all())


# Step 4: Transform Data
# Conduct 1-2 data tranformations on your dataset, such as indexing your data with a useful numeric value, or combining multiple columns into a new column.

#index data with useful numeric value
years = df['Release Year']
q1 = years.quantile(.25)
q3 = years.quantile(.75)

print(q1)
print(q3)
