import csv
import pandas as pd
import numpy as np
#pd.options.display.width = 0
# load in dataset to use for analysis key
# "selection" gene file for c.elegans
# create dataframe
def ana_threshold():
    df = pd.read_csv('jesse_data.csv', index_col=0)
    ana_df = pd.DataFrame(df)
    # select only columns 1,2,3,4,5
    gene_groups = ana_df.iloc[:, [0,1,2,3]]
    print(gene_groups)

    #gene_thresh = gene_groups.iloc[(gene_groups[:, [2,3,4,5] >=0 ])]
    #print(gene_thresh)
    #thresh_group_531 = group_531[group_531.iloc[:, [0]] >= 1]
    #print(thresh_group_531)

    for column, row in ana_df.iterrows():
        print(row)

ana_threshold()

# load in dataset to use for analysis selection
# "master" gene file for c. elegans
# create dataframe
def master_dict():
    df = pd.read_csv('c_elegans_gene_data.csv')
    ref_df = pd.DataFrame(df)
    # use [:,3] to load column 3 of the dataframe
    ref_gene_id = ref_df.iloc[:,3]
    #print(ref_gene_id)
    #print(ref_df)
master_dict()
    


