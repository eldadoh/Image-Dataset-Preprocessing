import pandas as pd 

def save_df(df : pd.DataFrame , name : str , verbose = True) -> None :
    
    df.to_pickle(name)
    
    if verbose : 
        print (f'\nSaved {name}')

def load_df(name : str) -> pd.DataFrame :
    
    return pd.read_pickle(name)
    
    