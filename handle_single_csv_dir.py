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

def get_specific_class_samples(df : pd.DataFrame,class_name:str) -> pd.DataFrame:

    df = df[df['annotation'] == class_name]
    
    if df.empty:
        print(f'Could not get ==={class_name}=== samples from current dataframe')
    
    return df 

def handle_single_csv_dir_func(dir_path : str,annotation_file_name_const : str, verbose : bool = True) -> pd.DataFrame:

    annotation_file_path = os.path.join(dir_path,annotation_file_name_const)
    
    df = pd.read_csv(annotation_file_path)
    df_sorted_class = sort_annotations_df_by_class(df,dir_path)
    specific_class_df_samples = get_specific_class_samples(df_sorted_class,class_name='9702910116_THERABREATH ORAL RINSE MINT')

    if verbose : 
        print ('\nDone with single_dir_csv ===> ' + f'{os.path.dirname(annotation_file_path)}')

    return specific_class_df_samples 

if __name__ == '__main__':

    main_csv_dir_path = 'Data/annotations/csv'
    test_path_single_csv_dir = 'Data/annotations/csv/06-20 Product1'

    ANNOTATION_FILE_NAME_CONST = 'annotations.csv'
    df_name = 'Data/test.pkl'

    df = handle_single_csv_dir_func(test_path_single_csv_dir,ANNOTATION_FILE_NAME_CONST)
    
    df.to_csv('_.csv', sep = '\t' , float_format='{:5f}'.format, encoding='utf-8') 
    pass 