"""
Splitting dataset into train, dev and test sets within the same individual, i.e. each individual will have a train, dev
and test sets of annotated data.
"""

import os.path
import pandas as pd

from setup.conf import ANNOTATED_DATASET_DIRECTORY, \
    PKL_DIRECTORY, \
    PER_CLASS_PKL_DIRECTORY, \
    SPLIT_PKL_DIRECTORY, \
    PER_CLASS_SPLIT_PKL_DIRECTORY


def concat_and_save_datasets(lst_datasets, session_number):
    df_list = []
    for dataset in lst_datasets:
        path_dataset = os.path.join(ANNOTATED_DATASET_DIRECTORY, session_number, dataset)
        df = pd.read_csv(path_dataset)
        df_list.append(df)
    result_df = pd.concat(df_list)
    if not os.path.exists(PKL_DIRECTORY):
        os.makedirs(PKL_DIRECTORY)
    result_df.to_pickle(PKL_DIRECTORY + '/' + session_number + '.pkl')


def separate_annotation_classes(session_number):
    """
    Receive the participant data file and separate examples of each class into a different file and save them in
    pkl_datasets > per_class > session_xx_yy
    :param session_number: String name of the session
    :return: None
    """
    file = session_number + '.pkl'
    read_folder = PKL_DIRECTORY
    write_folder = os.path.join(PER_CLASS_PKL_DIRECTORY, session_number)
    main_df = pd.read_pickle(os.path.join(read_folder, file))
    emotions = ['green', 'blue', 'yellow', 'red']
    for emotion in emotions:
        emotion_df = main_df.loc[main_df['emotion_zone'] == emotion]
        output_folder_path = os.path.join(write_folder, session_number)
        if not os.path.exists(write_folder):
            os.makedirs(write_folder)
        emotion_df.to_pickle(output_folder_path + '_' + emotion + '.pkl')


def split_classes_into_sets(session):
    folder = os.path.join(PER_CLASS_PKL_DIRECTORY, session)
    classes_files = os.listdir(folder)
    output_folder = os.path.join(PER_CLASS_SPLIT_PKL_DIRECTORY, session)
    for class_file in classes_files:
        emotion = class_file.split('_')[-1]
        emotion = emotion.replace('.pkl', '')
        df = pd.read_pickle(folder + '/' + class_file)
        df = df.reset_index(drop=True)
        df = df.iloc[:, 1:]
        train_df = df.sample(frac=0.8, random_state=25)
        dev_test_df = df.drop(train_df.index)
        dev_df = dev_test_df.sample(frac=0.5, random_state=25)
        test_df = dev_test_df.drop(dev_df.index)
        if not os.path.exists(output_folder):
            os.makedirs(output_folder)
        train_df.to_pickle(output_folder + '/' + session + '_' + emotion + '_' + 'train.pkl')
        dev_df.to_pickle(output_folder + '/' + session + '_' + emotion + '_' + 'dev.pkl')
        test_df.to_pickle(output_folder + '/' + session + '_' + emotion + '_' + 'test.pkl')


def concatenate_sets(session):
    folder = os.path.join(PER_CLASS_SPLIT_PKL_DIRECTORY, session)
    files_in_folder = os.listdir(folder)
    train = []
    test = []
    dev = []
    for file in files_in_folder:
        df_file = pd.read_pickle(folder + '/' + file)
        if 'train' in file:
            train.append(df_file)
            continue
        elif 'dev' in file:
            dev.append(df_file)
            continue
        elif 'test' in file:
            test.append(df_file)
    df_train = pd.concat(train)
    df_dev = pd.concat(dev)
    df_test = pd.concat(test)
    if not os.path.exists(SPLIT_PKL_DIRECTORY):
        os.makedirs(SPLIT_PKL_DIRECTORY)
    output_folder = os.path.join(SPLIT_PKL_DIRECTORY, session)
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    df_train.to_pickle(output_folder + '/' + session + '_train.pkl')
    df_dev.to_pickle(output_folder + '/' + session + '_dev.pkl')
    df_test.to_pickle(output_folder + '/' + session + '_test.pkl')


def main_split(session):
    separate_annotation_classes(session)
    split_classes_into_sets(session)
    concatenate_sets(session)


if __name__ == '__main__':
    ###################
    # 1. If the data of a session is not together into one file:

    # list_datasets = ['session_04_02_01.csv',
    #                  'session_04_02_02.csv',
    #                  'session_04_02_03.csv',
    #                  'session_04_02_04.csv',
    #                  'session_04_02_05.csv',
    #                  ]
    # concat_and_save_datasets(list_datasets, session_number='session_04_02')

    ###################
    # 2. To split into train, dev and test sets

    main_split('session_04_02')
