import csv
from pandas_utils import load_df, save_df 
import pandas as pd
import numpy as np 
import os
import glob
import shutil 

def sort_annotations_df_by_class(df : pd.DataFrame,dir_path : str) -> pd.DataFrame:
    
    df = df[['image_name','annotation','x','y','width','height']]
    df = df.sort_values('annotation')
    df['full_img_path'] = dir_path +'/' + df['image_name']
    df = df[['full_img_path','annotation','x','y','width','height']]
    
    return df 

def handle_single_csv_dir_func(dir_path : str,annotation_file_name_const : str, verbose : bool = True) -> pd.DataFrame:

    annotation_file_path = os.path.join(dir_path,annotation_file_name_const)
    
    basic_raw_df = pd.read_csv(annotation_file_path)

    try : 
        df_by_class = sort_annotations_df_by_class(basic_raw_df,dir_path)
        print
    except Exception as e : 
        print(e)

    if verbose : 
        print ('\nDone with single_dir_csv ===> ' + f'{os.path.dirname(annotation_file_path)}')

    return df_by_class 

if __name__ == '__main__':

    main_csv_dir_path = 'Data/annotations/csv'
    test_path_single_csv_dir = 'Data/annotations/csv/06-20 Product1'

    ANNOTATION_FILE_NAME_CONST = 'annotations.csv'
    df_name = 'Data/test.pkl'

    df = handle_single_csv_dir_func(test_path_single_csv_dir,ANNOTATION_FILE_NAME_CONST)

    pass 