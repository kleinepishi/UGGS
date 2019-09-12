import argparse
import pandas as pd
import numpy as np 

parser = argparse.ArgumentParser(description='allow for user input of master gene filepath')
parser.add_argument('filename')
args = parser.parse_args()
with open(args.filename) as file:
    df = pd.DataFrame(file)
    print(df)