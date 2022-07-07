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


def concat_and_save_datasets(lst_datasets, session_number):
    df_list = []
    for dataset in lst_datasets:
        path_dataset = os.path.join(path_annotated_dataset_directory, session_number, dataset)
        df = pd.read_csv(path_dataset)
        df_list.append(df)
    result_df = pd.concat(df_list)
    if not os.path.exists(pkl_folder):
        os.makedirs(pkl_folder)
    result_df.to_pickle(pkl_folder + '/' + session_number + '.pkl')


def separate_annotation_classes(session_number):
    """
    Receive the participant data file and separate examples of each class into a different file and save them in
    pkl_datasets > per_class > session_xx_yy
    :param session_number: String name of the session
    :return: None
    """
    file = session_number + '.pkl'
    read_folder = pkl_folder
    write_folder = os.path.join(pkl_folder, 'per_class', session_number)
    main_df = pd.read_pickle(os.path.join(read_folder, file))
    emotions = ['green', 'blue', 'yellow', 'red']
    for emotion in emotions:
        emotion_df = main_df.loc[main_df['emotion_zone'] == emotion]
        output_folder_path = os.path.join(write_folder, session_number)
        if not os.path.exists(write_folder):
            os.makedirs(write_folder)
        emotion_df.to_pickle(output_folder_path + '_' + emotion + '.pkl')


if __name__ == '__main__':
    list_datasets = ['session_04_02_01.csv',
                     'session_04_02_02.csv',
                     'session_04_02_03.csv',
                     'session_04_02_04.csv',
                     'session_04_02_05.csv',
                     ]
    # concat_and_save_datasets(list_datasets, session_number='session_04_02')
    separate_annotation_classes('session_01_01')
