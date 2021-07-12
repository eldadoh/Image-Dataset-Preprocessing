import json
import csv
from pandas_utils import load_df, save_df 
import pandas as pd
import numpy as np 
import os
import glob
import shutil 

def handle_single_csv_dir_func(dir_path,annotation_file_name):

    annotation_file_path = os.path.join(dir_path,annotation_file_name)
    df = pd.read_csv(annotation_file_path)
    return df 

if __name__ == '__main__':

    test_path_single_csv_dir = 'Data/annotations/csv/06-20 Product1'
    annotation_file_name = 'annotations.csv'
    df_name = 'Data/test.pkl'

    df = handle_single_csv_dir_func(test_path_single_csv_dir,annotation_file_name)
    save_df(df, df_name)
    df = load_df(df_name)
    pass 