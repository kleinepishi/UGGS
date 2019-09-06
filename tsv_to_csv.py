import pandas as pd

tsv_file = 'c_elegans_gene_data.tsv'
csv_table = pd.read_csv(tsv_file,sep='\t')
csv_table.to_csv('c_elegans_gene_data.csv',index=False)