# takes in "low-hanging fruit" in sub-groups of genes, segregated by "easy" variables
# for inputs, take in organism taxonomy id from ncbi
# additionally, use gene_sets comprised of smaller groups

# imports
import pandas as pd
from pandas import ExcelFile
from pandas import ExcelWriter
import numpy as np

# load in dataframe
df = pd.read_excel('jesse_data.xlsx', sheet_name='Sheet1')
# display column headings
print("Column headings:")
print(df.columns)