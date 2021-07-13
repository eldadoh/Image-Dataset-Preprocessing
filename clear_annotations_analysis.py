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

def get_specific_class_samples(df_as_csv ,class_name: str,save: bool = False):

    df = pd.read_csv(df_as_csv,sep='\t')

    specific_class_df = df[df['annotation'] == class_name]
    
    if specific_class_df.empty:
        print(f'Could not get ==={class_name}=== samples from current dataframe')
    
    if save : 
        save_df_as_csv(specific_class_df,'Output/specific_class_df_samples.csv')
        print(f'\nSaved df samples from class === {class_name} === to : Output/specific_class_df_samples.csv\n')

    return specific_class_df

def main():     

    DF_AS_CSV_FILE_PATH = 'Output/clear_df.csv'
    CLASS_NAME = '9702910116_THERABREATH ORAL RINSE MINT'

    get_specific_class_samples(DF_AS_CSV_FILE_PATH ,class_name = CLASS_NAME ,save = True)
        
if __name__ == '__main__':
    main()