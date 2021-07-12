import pandas as pd
import numpy as np 
import os
import glob
import shutil 
import json
import csv 
from handle_single_csv_dir import handle_all_csv_dirs

def main(): 

    ANNOTATIONS_DIR_PATH_CSV = 'Data/annotations/csv'
    ANNOTATIONS_DIR_PATH_JSON = 'Data/annotations/json'

    handle_all_csv_dirs(ANNOTATIONS_DIR_PATH_CSV)
        
if __name__ == '__main__':
    main()