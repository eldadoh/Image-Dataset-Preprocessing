import json
import csv
import pandas as pd
import numpy as np 
import os
import glob
import shutil 

# def preprocess_annotations_df(df : pd.DataFrame) -> pd.DataFrame:
#     pass
#     return df 

# def handle_single_csv_dir_func(dir_path : str,annotation_file_name_const : str, verbose : bool = True) -> pd.DataFrame:

#     annotation_file_path = os.path.join(dir_path,annotation_file_name_const)
    
#     df = pd.read_csv(annotation_file_path)

#     try : 
#         df = preprocess_annotations_df(df)
#     except Exception as e : 
#         print(e)

#     if verbose : 
#         print ('\nDone with single_dir_csv ===> ' + f'{os.path.dirname(annotation_file_path)}')

#     return df 

def convert_top_left_bottom_rigth_to_xywh(top_left,bottom_right):
    top,left = top_left[:]
    bottom,right = bottom_right[:]
    

    w = int(right - left)
    h = int(bottom - top)
    x = ((left + right) / 2) / w 
    y = ((top + bottom) / 2) / h 

    return x,y,w,h

if __name__ == '__main__':

    # main_csv_dir_path = 'Data/annotations/csv'
    # test_path_single_csv_dir = 'Data/annotations/csv/06-20 Product1'

    # ANNOTATION_FILE_NAME_CONST = 'annotations.csv'
    # df_name = 'Data/test.pkl'

    # df = handle_single_csv_dir_func(test_path_single_csv_dir,ANNOTATION_FILE_NAME_CONST)

    json_file = 'Data/annotations/json/0011110353986/IMG_20210616_201118.jpg.json'
    with open(json_file, 'r') as f:
        data = json.load(f)
        data = data['objects'][:]
        for item in data : 
            img_name = os.path.basename(json_file)[:-len('.json')]
            c = item['classTitle'] 
            top_left,bottom_right = item['points']['exterior'][:]
            x,y,w,h = convert_top_left_bottom_rigth_to_xywh(top_left,bottom_right)
            sample_dict = { 'img_name' : img_name,
                            'class' : c, 
                            'x' : x,
                            'y' : y,
                            'w' : w,
                            'h' : h}
            print()
    pass 