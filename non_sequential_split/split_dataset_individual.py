"""
Splitting dataset into train, dev and test sets within the same individual, i.e. each individual will have a train, dev
and test sets of annotated data.
"""
import pathlib
import os.path
import pandas as pd

main_folder = pathlib.Path(__file__).parent.parent.absolute()
path_annotated_dataset_directory = os.path.join(main_folder, 'annotated_dataset')
pkl_folder = os.path.join(main_folder, 'pkl_datasets')


def concat_and_save_datasets(list_datasets, session_number):
    df_list = []
    for dataset in list_datasets:
        path_dataset = os.path.join(path_annotated_dataset_directory, session_number, dataset)
        df = pd.read_csv(path_dataset)
        df_list.append(df)
    result_df = pd.concat(df_list)
    result_df.to_pickle(pkl_folder + '/' + session_number + '.pkl')


if __name__ == '__main__':
    list_datasets = ['session_01_01_01.csv',
                     'session_01_01_02.csv',
                     'session_01_01_03.csv',
                     'session_01_01_04.csv',
                     'session_01_01_05.csv',
                     'session_01_01_06.csv']
    concat_and_save_datasets(list_datasets, session_number='session_01_01')
