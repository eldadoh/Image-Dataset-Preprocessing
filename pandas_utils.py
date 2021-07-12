import pandas as pd 
import numpy as np

def change_col_dtype(df,col_name, new_dtype = 'int32'):

    df[col_name] =  df[col_name].astype(new_dtype)
    return df 

def save_df_as_csv(df : pd.DataFrame,name:str):

    """float_format='{:5f}'"""
    
    if '.csv' in name :
        df.to_csv(f'{name}', sep = '\t' , float_format='{:5f}'.format, encoding='utf-8')
    else: 
        print('\nError: You didnt entered \'.csv\'')

def save_df_as_pkl(df : pd.DataFrame , name : str , verbose = True) -> None :
    
    if '.pkl' in name : 

        df.to_pickle(name)
        
        if verbose : 
            print (f'\nSaved {name}')

def load_df_as_pkl(name : str) -> pd.DataFrame :

    if '.pkl' in name : 

        return pd.read_pickle(name)
    

def xl_to_pandas(file_name,sheet_name = None):
    
    xl_file = pd.ExcelFile(file_name)

    dfs = {sheet_name: xl_file.parse(sheet_name) 
          for sheet_name in xl_file.sheet_names}

    if sheet_name:
          
          return dfs[f'{sheet_name}']

    return dfs 

