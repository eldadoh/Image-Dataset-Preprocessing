import pandas as pd 

def save_df(df : pd.DataFrame , name : str , verbose = True) -> None :
    
    df.to_pickle(name)
    
    if verbose : 
        print (f'\nSaved {name}')

def load_df(name : str) -> pd.DataFrame :
    
    return pd.read_pickle(name)
    

def save_df_as_csv(df : pd.DataFrame,name:str):

    """float_format='{:5f}'"""
    
    df.to_csv(f'{name}', sep = '\t' , float_format='{:5f}'.format, encoding='utf-8')

def xl_to_pandas(file_name,sheet_name = None):
    
    xl_file = pd.ExcelFile(file_name)

    dfs = {sheet_name: xl_file.parse(sheet_name) 
          for sheet_name in xl_file.sheet_names}

    if sheet_name:
          
          return dfs[f'{sheet_name}']

    return dfs 

# def remove_scientific_notation(df,col_name, new_dtype = 'int32'):

#       if not isinstance(col_name,str):
#             print('col_name is not a string')
#             return False

#       df[col_name] =  df[col_name].astype(new_dtype)
#           df['SKU'] = df['SKU'].astype(np.int64)
#     pd.DataFrame.to_csv(df,'_.csv', sep = '\t' , float_format='{:f}'.format, encoding='utf-8') 
#       return df 