import csv
import pandas as pd
import numpy as np

# load in dataset to use for analysis key
# "selection" gene file for c.elegans
# create dataframe
def ana_threshold():
    df = pd.read_csv('jesse_data.csv', index_col=0)
    ana_df = pd.DataFrame(df)
    # use [:,0] to load column 0 of the dataframe
    ana_gene_id = ana_df.iloc[:,0]
    print(ana_gene_id)
    # select only columns 1,2,3,4,5
    gene_groups = ana_df.iloc[:, [1,2,3,4,5]]
    print(gene_groups)
    # select gene group 1, where column value is > 0
    exp_gene_g1 = ana_df.iloc[ana_df[:, [2] > 0]]
    print(exp_gene_g1)

ana_threshold()

# load in dataset to use for analysis selection
# "master" gene file for c. elegans
# create dataframe
def ref_threshold():
    df = pd.read_csv('c_elegans_gene_data.csv')
    ref_df = pd.DataFrame(df)
    # use [:,3] to load column 3 of the dataframe
    ref_gene_id = ref_df.iloc[:,3]
    print(ref_gene_id)
ref_threshold()
    


