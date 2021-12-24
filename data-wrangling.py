import pandas as pd
import numpy as np

df = pd.read_csv('Film_Locations.csv')

# print(df.shape)
# print(df.info())
# print(df.head(11))

print(df.describe())
# print(df.mean())
# print(df.max())


# Step 2: Select, Filter, Sort
# Using dataframes in pandas, write 2-3 functions that filter and sort your dataset. For example, write a function that produces a subset of your data that includes a numeric value that is higher than the average numeric value for that column. Another example: write a function that sorts the rows alphabetically based on a texual column.

# Step 3: Clean Data
# Identify whether your dataset has any missing or null value using pandas. If there are null values in a numeric column, determine whether you should remove the data, or if there is a reasonable replacement for null, such as replacing it with a 0 value. Additionally, identify if there are any low/high outliers in your dataset using pandas.

# Step 4: Transform Data
# Conduct 1-2 data tranformations on your dataset, such as indexing your data with a useful numeric value, or combining multiple columns into a new column.

