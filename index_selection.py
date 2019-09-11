# imports
import pandas as pd
from pandas import ExcelFile
from pandas import ExcelWriter
import matplotlib.pyplot as plt
from intermine.webservice import Service
import numpy as np

# select the index to base queries off of using pattern matching
# index will be Ensembl gene ID
def index():
    df = pd.read_csv('c_elegans_gene_data.csv')
    df_filter = df.filter(like='WBGene')
    print(df_filter)
index()

# select rows from dataframe where 'WBGene*' is present
def selection():
    
