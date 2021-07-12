import pandas as pd
import numpy as np 
import os
import glob
import shutil 
import json
import csv 
from handle_single_csv_dir import handle_single_csv_dir_func
from handle_single_json_dir import handle_single_json_dir_func

def handle_all_json_dirs(main_json_dir_path : str,verbose : bool = True) -> None:
    
    for single_dir_path in glob.glob(main_json_dir_path + '/*.json'):
        df = handle_single_json_dir_func(single_dir_path)
        # aggregate dfs to new one

    if verbose : 
        print(f'Done handling main_csv_dir_path : {main_json_dir_path}')

def handle_all_csv_dirs(main_csv_dir_path : str,verbose : bool = True) -> None:
    
    for single_dir_path in glob.glob(main_csv_dir_path + '/*.csv'):
        df = handle_single_csv_dir_func(single_dir_path)
        # aggregate dfs to new one

    if verbose : 
        print(f'Done handling main_csv_dir_path : {main_csv_dir_path}')

def main(): 

    MAIN_ANNOTATIONS_DIR_PATH_CSV = 'Data/annotations/csv'
    MAIN_ANNOTATIONS_DIR_PATH_JSON = 'Data/annotations/json'

    # handle_all_csv_dirs(MAIN_ANNOTATIONS_DIR_PATH_CSV)
    # handle_all_json_dirs(MAIN_ANNOTATIONS_DIR_PATH_JSON)
        
if __name__ == '__main__':
    main()