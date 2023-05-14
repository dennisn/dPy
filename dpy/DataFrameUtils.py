"""
.. module:: DataFrameUtils
   :synopsis: utils and class related to Pandas's DataFrame

Module: DataFrameUtils

This module defined utils and class related to Pandas's DataFrame

"""
import pandas as pd
import numpy as np
import os, glob


#region CSVReading

def load_csv(file_name:str, base_dir:str=None, index_col:int=0, parse_dates:bool=True, dtype=None)->pd.DataFrame:
    """ Loading a CSV file given its name and path

    Args:
        file_name (str): the csv file name of the dataframe (may/may not included path)
        base_dir (str, optional): The base path to the file above. Defaults to None.
        index_col (int, optional): the 0-based index to the index column. Defaults to 0.
        parse_dates (bool, optional): whether we should parse date or not. Defaults to True.
        dtype (optional): The data type. Defaults to None.

    Returns:
        pd.DataFrame: The result dataframe
    """
    full_filename = file_name if base_dir is None else os.path.join(base_dir, file_name)
    print("Reading ", full_filename)
    return pd.read_csv(full_filename, index_col=index_col, parse_dates=parse_dates, dtype=dtype)


def glob_files(base_dir:str, file_name_pattern:str="*.csv"):
    """Search for files matching given pattern

    Args:
        base_dir (str): Search path
        file_name_pattern (str, optional): The search file pattern. Defaults to "*.csv".

    Returns:
        list of file paths
    """
    return glob.glob(os.path.join(base_dir, file_name_pattern))
    

def load_csv_in_dir(base_dir:str, index_col:int=0, parse_dates:bool=True, file_name_pattern:str="*.csv"):
    """Loading all csv matching given pattern in given directory

    Args:
        base_dir (str): Directory to search
        index_col (int, optional): the 0-based index to the index column. Defaults to 0.
        parse_dates (bool, optional): whether we should parse date or not. Defaults to True.
        file_name_pattern (str, optional): the filename pattern to search. Defaults to "*.csv".

    Returns:
        dictionary of file name to pandas dataframe
    """
    res = {}
    for file_path in glob_files(base_dir, file_name_pattern):
        file_name = os.path.split(file_path)[1]
        print("Loading file: ", file_name)
        df = pd.read_csv(file_path, index_col=index_col, parse_dates=parse_dates)
        res[file_name] = df
    return res

#endregion CSVReading
    
#region DataFrame resize
    
def inflate_series(data_s:pd.Series, ref_df:pd.DataFrame)->pd.DataFrame:
    """Inflate a data series to match the dimention of the reference dataframe

    Args:
        data_s (Series): main data series
        ref_df (DataFrame): reference dataframe

    Returns:
        A dataframe with same index as 'data_s', and same column as 'ref_df', all with value of 1
    """
    data_shape = (len(data_s.index), len(ref_df.columns))
    res_df = pd.DataFrame(data=np.ones(data_shape), index=data_s.index, columns=ref_df.columns)
    return res_df

def reindex_to_common(base_df:pd.DataFrame, target_df:pd.DataFrame)->pd.DataFrame:
    """Reindex the base_df to a new dataframe that has index as union of 2 indexes, columns as unions of 2 dataframe columns"""
    # get the common columns
    col_1 = set(base_df.columns)
    col_2 = set(target_df.columns)
    cols_common = list(col_1.union(col_2))
    cols_common.sort()
    
    # get the common index
    index_1 = set(base_df.index)
    index_2 = set(target_df.index)
    index_common = list(index_1.union(index_2))
    index_common.sort()
    
    # create a common dataframe
    common_df = pd.DataFrame(index=index_common, columns=cols_common)
    
    return base_df.reindex_like(common_df), target_df.reindex_like(common_df)

#endregion DataFrame resize

#region Ranking

def rank_func(df:pd.DataFrame, method:str='average')->pd.DataFrame:
    """
    Rank cross-sectional into percentile, ensure such that [1,2,3] will become [0, 0.5, 1]
    """
    rank_raw = df.rank(axis=1, method=method, pct=False) 
    return (rank_raw - 1).div(rank_raw.max(axis=1).sub(1), axis=0)
    
def discretize_by_quantile(src_df:pd.DataFrame, q_group:int=4)->pd.DataFrame:
    """Split the cross-sectional rank into groups"""
    # split the rank into groups
    res = src_df.apply(lambda x: pd.qcut(x, q_group, labels=False, duplicates='drop'), axis=1)
    res.columns = src_df.columns
    return res

#endregion Ranking

#region Excel-IO

def write_to_excel(dest_fullpath:str, dfs_map:dict, include_index:bool=True)->None:
    """Write each dataframe in the dataframe map as a separated tab in a excel file

    Args:
        dest_fullpath (str): full path to the destination excel file
        dfs_map (dict): dictionary of dataframe, key will be tab name in the result excel file
        include_index (bool, optional): whether we would write the index or not. Defaults to True.
    """
    with pd.ExcelWriter(dest_fullpath) as writer:
        for k, df in dfs_map.items():
            df.to_excel(writer, sheet_name=k, index=include_index)
            
#endregion Excel-IO