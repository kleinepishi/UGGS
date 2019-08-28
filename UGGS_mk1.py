# takes in "low-hanging fruit" in sub-groups of genes, segregated by "easy" variables
# for inputs, take in organism taxonomy id from ncbi
# additionally, use gene_sets comprised of smaller groups

# imports
import pandas as pd
from pandas import ExcelFile
from pandas import ExcelWriter
import numpy as np

# excel file

data_file = pd.read_csv('jesse_data.csv')

def load(data_file):
    # load in dataframe
    df = data_file
    # display column headings
    print("Column headings:")
    print(df.columns)
load(data_file)

# print out all genes where value is > 0
def threshold():
    df = data_file
    thresh_df = df[['gene_id',
        '531 genes where translation is promoted by GLH-1 (-.2 difference, see old table for details)',
        '587 genes where translation is inhibited by GLH-1 (.2 difference, see old table for details)',
        '97 genes where translation is promoted by GLH-1 (-.5 difference, see old table for details)',
        '99 genes where translation is inhibited by GLH-1 (.5 difference, see old table for details)']]
    thresh_val = thresh_df.loc[
        (thresh_df['531 genes where translation is promoted by GLH-1 (-.2 difference, see old table for details)'] > 0) &
        (thresh_df['587 genes where translation is inhibited by GLH-1 (.2 difference, see old table for details)'] > 0) &
        (thresh_df['97 genes where translation is promoted by GLH-1 (-.5 difference, see old table for details)'] > 0) &
        (thresh_df['99 genes where translation is inhibited by GLH-1 (.5 difference, see old table for details)'] > 0)]
    print(thresh_val()

#def seg(data_file):
    # load in dataframe
 #   df = pd.read_excel(data_file, index_col=None, na_values=['NA'], usecols="A,C,D,E,F")
  #  print(df.columns)
#seg(data_file)
