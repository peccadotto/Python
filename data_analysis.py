from scripts.convert_excel import convert_excel
from scripts.create_df import create_df
from scripts.save_rds import save_rds

## # Crea file(s) CSV da file XLS
input_file = "input_data/test.xlsx"  # <—— Da modificare all'occorrenza
convert_excel(input_file)

## # Per ogni file CSV crea dataframe
dfs = create_df()
globals().update(dfs)

## # Per ogni dataframe crea file RDS
save_rds(dfs)

## # Pulisci environment
for key in list(globals().keys()):
    if not key.startswith("_"):
        del globals()[key]
if 'key' in globals():
    del key