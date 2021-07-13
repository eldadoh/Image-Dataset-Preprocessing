import pandas as pd
import numpy as np 
import os
import glob
import shutil 
import json
import csv
from pandas.core.frame import DataFrame
from pandas.io.parsers import read_csv 
from pandas_utils import save_df_as_csv

""" In this file I am running some analysis functions on the clear aggeregated annotations files data"""

def get_specific_class_samples(df_as_csv ,class_name: str,output_dir_path :str , save: bool = False , class_names_who_changed : list = None):

    df = pd.read_csv(df_as_csv,sep='\t')

    specific_class_df = df[df['annotation'] == class_name]
    
    if specific_class_df.empty:
        print(f'Could not get ==={class_name}=== samples from current dataframe because it\'s empty')
    
    if save : 
        output_path = os.path.join(output_dir_path , f'{class_name}.csv')
        try:
            save_df_as_csv(specific_class_df,output_path)
            print(f'\nSaved df samples from class === {class_name} === to : {output_path}\n')
        except:
            print(f'\nBad class name: {class_name}')
            class_name = class_name.replace("/", "@" , -1)
            output_path = os.path.join(output_dir_path , f'{class_name}.csv')
            save_df_as_csv(specific_class_df,output_path)
            print(f'\nChanged and Saved df samples from class === {class_name} === to : {output_path}\n')
            class_names_who_changed.append(class_name)
    
    return specific_class_df,class_names_who_changed

def get_all_dataset_specific_class_anotations(df_as_csv : pd.DataFrame,output_path :str , save : bool = False,class_names_who_changed : list = [],verbose :bool = True ):

    df = pd.read_csv(df_as_csv,sep='\t')
    class_names_list = df['annotation'].unique()

    for class_name in class_names_list : 
        _ , class_names_who_changed = get_specific_class_samples(df_as_csv,class_name,output_path,save,class_names_who_changed)

    if verbose : 
        print(f'The next classes names had changed:\n{class_names_who_changed}\n')

def main():     

    DF_AS_CSV_FILE_PATH = 'Output/clear_df.csv'
    ANNOTATIONS_BY_CLASS_DIR_PATH = 'Output/annotations_by_class'

    get_all_dataset_specific_class_anotations(DF_AS_CSV_FILE_PATH,output_path=ANNOTATIONS_BY_CLASS_DIR_PATH,save = True)

if __name__ == '__main__':
    main()