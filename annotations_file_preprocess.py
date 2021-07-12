import pandas as pd
import numpy as np 
import os
import glob
import shutil 
import json
import csv 
from handle_single_csv_dir import handle_single_csv_dir_func

def main(): 

    ANNOTATIONS_DIR_PATH_CSV = 'Data/annotations/csv'
    ANNOTATIONS_DIR_PATH_JSON = 'Data/annotations/json'

    for single_csv_dir_name in os.listdir(ANNOTATIONS_DIR_PATH_CSV):
        single_csv_dir_path = os.path.join(ANNOTATIONS_DIR_PATH_CSV,single_csv_dir_name)
        handle_single_csv_dir_func(single_csv_dir_path)
        
if __name__ == '__main__':
    main()