# takes in "low-hanging fruit" in sub-groups of genes, segregated by "easy" variables
# for inputs, take in organism taxonomy id from ncbi
# additionally, use gene_sets comprised of smaller groups

# imports
import pandas as pd
from pandas import ExcelFile
from pandas import ExcelWriter
import matplotlib.pyplot as plt
from intermine.webservice import Service
import numpy as np

# wormmine parameter query
def wmquery():
    service = Service("http://intermine.wormbase.org/tools/wormmine/service")
    query = service.new_query("Gene")
    query.add_view(
        "biotype", "length", "symbol", "primaryIdentifier",
        "downstreamIntergenicRegion.primaryIdentifier",
        "downstreamIntergenicRegion.organism.name",
        "downstreamIntergenicRegion.locations.feature.primaryIdentifier",
        "downstreamIntergenicRegion.locations.start",
        "downstreamIntergenicRegion.locations.end",
        "downstreamIntergenicRegion.locations.strand", "homologues.dataSets.name",
        "upstreamIntergenicRegion.primaryIdentifier",
        "upstreamIntergenicRegion.organism.name",
        "upstreamIntergenicRegion.locations.feature.primaryIdentifier",
        "upstreamIntergenicRegion.locations.start",
        "upstreamIntergenicRegion.locations.end",
        "upstreamIntergenicRegion.locations.strand",
        "transcripts.primaryIdentifier", "transcripts.symbol"
    )

    for row in query.rows():
        print (row["biotype"], row["length"], row["symbol"], row["primaryIdentifier"], \
            row["downstreamIntergenicRegion.primaryIdentifier"], \
            row["downstreamIntergenicRegion.organism.name"], \
            row["downstreamIntergenicRegion.locations.feature.primaryIdentifier"], \
            row["downstreamIntergenicRegion.locations.start"], \
            row["downstreamIntergenicRegion.locations.end"], \
            row["downstreamIntergenicRegion.locations.strand"], row["homologues.dataSets.name"], \
            row["upstreamIntergenicRegion.primaryIdentifier"], \
            row["upstreamIntergenicRegion.organism.name"], \
            row["upstreamIntergenicRegion.locations.feature.primaryIdentifier"], \
            row["upstreamIntergenicRegion.locations.start"], \
            row["upstreamIntergenicRegion.locations.end"], \
            row["upstreamIntergenicRegion.locations.strand"], row["transcripts.primaryIdentifier"], \
            row["transcripts.symbol"])
wmquery()

# define primary data file
df = pd.read_excel('jesse_data.xlsx')

def load(df):
    # load in dataframe
    # display column headings
    print("Column headings:")
    print(df.columns)
load(df)

# print out all gene_id's where value is > 0
# unneeded, safe to remove
def threshold():
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
    print(thresh_val())

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
ana_threshold()

# load in dataset to use for analysis selection
# "master" gene file for c. elegans
# create dataframe
def master_dict():
    df = pd.read_csv('c_elegans_gene_data.csv')
    ref_df = pd.DataFrame(df)
    # use [:,3] to load column 3 of the dataframe
    ref_gene_id = ref_df.iloc[:,3]
    print(ref_gene_id)
    #print(ref_df)
master_dict()

