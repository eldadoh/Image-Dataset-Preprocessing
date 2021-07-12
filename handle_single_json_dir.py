import json
import csv 
import pandas as pd
import numpy as np 
import os
import glob
import shutil 

import json
import csv
from pandas_utils import load_df, save_df 
import pandas as pd
import numpy as np 
import os
import glob
import shutil 

def preprocess_annotations_df(df : pd.DataFrame) -> pd.DataFrame:
    pass
    return df 

def handle_single_json_dir_func(dir_path : str,annotation_file_name_const : str) -> pd.DataFrame:

    annotation_file_path = os.path.join(dir_path,annotation_file_name_const)
    
    df = pd.read_csv(annotation_file_path)

    try : 
        df = preprocess_annotations_df(df)
    except Exception as e : 
        print(e)

    return df 


def handle_all_json_dirs(main_json_dir_path : str,verbose : bool = True) -> None:
    
    for single_dir_path in glob.glob(main_json_dir_path + '/*.json'):
        df = handle_single_json_dir_func(single_dir_path)
        # aggregate dfs to new one

    if verbose : 
        print(f'Done handling main_json_dir_path : {main_json_dir_path}')


if __name__ == '__main__':

    main_json_dir_path = 'Data/annotations/json'
    test_path_single_json_dir = ''

    annotation_file_name_const = 'annotations.csv' ##change , there are list of jsons files 
    df_name = 'Data/test.pkl'

    df = handle_single_json_dir_func(test_path_single_json_dir,annotation_file_name_const)
    save_df(df, df_name)
    df = load_df(df_name)
    handle_all_json_dirs(main_json_dir_path)
    pass 