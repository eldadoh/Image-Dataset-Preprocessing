import pandas as pd
import numpy as np 
import os
import glob
import shutil 
import json
import csv 
from handle_single_csv_dir import get_one_class_specific_samples, handle_single_csv_dir_func
# from handle_single_json_dir import handle_single_json_dir_func
from pandas_utils import save_df_as_csv

# def handle_all_json_dirs(main_json_dir_path : str,verbose : bool = True) -> None:
    
#     for single_dir_path in glob.glob(main_json_dir_path + '/*.json'):
#         df = handle_single_json_dir_func(single_dir_path)
#         # aggregate dfs to new one

#     if verbose : 
#         print(f'Done handling main_csv_dir_path : {main_json_dir_path}')

def handle_all_csv_dirs(main_csv_dir_path : str,param_dict : dict , verbose : bool = True):
    
    small_dfs = []
    
    for dir_name in os.listdir(main_csv_dir_path):
        single_dir_path = os.path.join(main_csv_dir_path,dir_name)
        df = handle_single_csv_dir_func(single_dir_path,param_dict)
        small_dfs.append(df)
    
    large_df = pd.concat(small_dfs, ignore_index=True) 
    specific_class_df_samples = get_one_class_specific_samples(large_df,class_name=param_dict['one_class_specific_samples'])

    save_df_as_csv(large_df,'Output/large_df.csv')
    save_df_as_csv(specific_class_df_samples,'Output/specific_class_df_samples.csv')

    if verbose : 
        print(f'\nDone handling main_csv_dir_path : {main_csv_dir_path}\n')

def main(): 

    PARAM_DICT ={'annotation_file_name_const' : 'annotations.csv',
                'one_class_specific_samples' : '9702910116_THERABREATH ORAL RINSE MINT'}

    MAIN_ANNOTATIONS_DIR_PATH_CSV = 'Data/annotations/csv'
    MAIN_ANNOTATIONS_DIR_PATH_JSON = 'Data/annotations/json'

    handle_all_csv_dirs(MAIN_ANNOTATIONS_DIR_PATH_CSV,param_dict=PARAM_DICT)
    # handle_all_json_dirs(MAIN_ANNOTATIONS_DIR_PATH_JSON)
        
if __name__ == '__main__':
    main()