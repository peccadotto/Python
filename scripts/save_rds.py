import os
import pyreadr

def save_rds(dfs, output_dir = "output_rds"):

    os.makedirs(output_dir, exist_ok = True)
    
    for df_name, df in dfs.items():
        clean_name = df_name[3:] if df_name.startswith("df_") else df_name
        out_file = os.path.join(output_dir, f"{clean_name}.rds")
        pyreadr.write_rds(out_file, df)
        print(f"[✓] File '{out_file}' created")