### # CREATE DATAFRAME FROM CSV FILES FUNCTION
### # create_df()

import os
import pandas as pd

def create_df():
    input_dir = "output_csv"
    dataframes = {}
    
    for filename in os.listdir(input_dir):
        if filename.endswith(".csv"):
            file_base_name = os.path.splitext(filename)[0]
            var_name = f"df_{file_base_name}"
            file_path = os.path.join(input_dir, filename)
            
            dataframes[var_name] = pd.read_csv(file_path, sep=";")
            num_rows, num_cols = dataframes[var_name].shape
            size_kb = dataframes[var_name].memory_usage(deep=True).sum() / 1024
            print(f"[✓] Dataframe '{var_name}' created | {num_rows} rows x {num_cols} cols | {size_kb:.2f} kB")
            
    return dataframes