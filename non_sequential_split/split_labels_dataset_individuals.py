"""
Splitting dataset into train, dev and test sets within the same individual, i.e. each individual will have a train, dev
and test sets of annotated data.
"""

import os.path
import pandas as pd

from non_sequential_split.conf import ANNOTATED_DATASET_DIRECTORY, \
    PKL_DIRECTORY, \
    SPLIT_PKL_DIRECTORY_LABELS, \
    PER_CLASS_PKL_DIRECTORY, \
    PER_CLASS_SPLIT_PKL_DIRECTORY, \
    PKL_DIRECTORY_LABELS


def concat_and_save_datasets(lst_datasets, session_number, annotation_type='parents'):
    df_list = []
    for dataset in lst_datasets:
        path_dataset = os.path.join(ANNOTATED_DATASET_DIRECTORY, annotation_type, session_number, dataset)
        df = pd.read_csv(path_dataset)
        df_list.append(df)
    result_df = pd.concat(df_list)
    if not os.path.exists(PKL_DIRECTORY):
        os.makedirs(PKL_DIRECTORY)
    output_dictory = os.path.join(PKL_DIRECTORY, 'labels', annotation_type, session_number + '.pkl')
    result_df.to_pickle(output_dictory)


def separate_annotation_classes(session_number, annotation_type):
    """
    Receive the participant data file and separate examples of each class into a different file and save them in
    pkl_datasets > per_class > session_xx_yy
    :param session_number: String name of the session
    :return: None
    """
    file = session_number + '.pkl'
    read_folder = os.path.join(PKL_DIRECTORY_LABELS, annotation_type)
    write_folder = os.path.join(read_folder, 'per_class', session_number)
    main_df = pd.read_pickle(os.path.join(read_folder, file))
    emotions = ['green', 'blue', 'yellow', 'red']
    for emotion in emotions:
        emotion_df = main_df.loc[main_df['emotion_zone'] == emotion]
        output_folder_path = os.path.join(write_folder, session_number)
        if not os.path.exists(write_folder):
            os.makedirs(write_folder)
        emotion_df.to_pickle(output_folder_path + '_' + emotion + '.pkl')


def split_classes_into_sets(session, annotation_type):
    folder = os.path.join(PKL_DIRECTORY_LABELS, annotation_type, 'per_class', session)
    classes_files = os.listdir(folder)
    output_folder = os.path.join(PKL_DIRECTORY_LABELS, annotation_type, 'per_class_split', session)
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


def concatenate_sets(session, annotation_type):
    folder = os.path.join(PKL_DIRECTORY_LABELS, annotation_type, 'per_class_split',
                          session)
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
    output_folder = os.path.join(PKL_DIRECTORY_LABELS, annotation_type, 'split', session)
    # if not os.path.exists(SPLIT_PKL_DIRECTORY_LABELS):
    #     os.makedirs(SPLIT_PKL_DIRECTORY_LABELS)
    # output_folder = os.path.join(SPLIT_PKL_DIRECTORY_LABELS, session)
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    df_train = add_frametime_key_to_labels(df_train, session)
    df_dev = add_frametime_key_to_labels(df_dev, session)
    df_test = add_frametime_key_to_labels(df_test, session)

    df_train = add_session_column_to_labels(df_train, session)
    df_dev = add_session_column_to_labels(df_dev, session)
    df_test = add_session_column_to_labels(df_test, session)

    df_train.to_pickle(output_folder + '/' + session + '_train.pkl')
    df_dev.to_pickle(output_folder + '/' + session + '_dev.pkl')
    df_test.to_pickle(output_folder + '/' + session + '_test.pkl')
    # CSV
    df_train.to_csv(output_folder + '/' + session + '_train.csv')
    df_dev.to_csv(output_folder + '/' + session + '_dev.csv')
    df_test.to_csv(output_folder + '/' + session + '_test.csv')


def add_session_column_to_labels(dataframe, session):
    dataframe['session'] = dataframe.apply(lambda row: session, axis=1)
    return dataframe


def add_frametime_key_to_labels(dataframe, session_number):
    dataframe['frametime'] = dataframe.apply(lambda row: create_frametime(row, session=session_number), axis=1)
    return dataframe


def create_frametime(row, session):
    time_value = row['time_of_video_seconds']
    video_part = row['video_part']
    return f'{session}_0{video_part}___{time_value}'


def main_split(session, annotation_type='parents'):
    separate_annotation_classes(session, annotation_type)
    split_classes_into_sets(session, annotation_type)
    concatenate_sets(session, annotation_type)


if __name__ == '__main__':
    ###################
    # 1. If the data of a session is not together into one file:

    list_datasets = ['session_04_01_01.csv',
                     'session_04_01_02.csv',
                     'session_04_01_03.csv',
                     'session_04_01_04.csv',
                     'session_04_01_05.csv',
                     ]
    concat_and_save_datasets(list_datasets, 'session_04_01', 'specialist')

    ###################
    # 2. To split into train, dev and test sets

    sessions = [
        'session_01_01',
        'session_02_01',
        'session_02_02',
        'session_03_01',
        'session_03_02',
        'session_04_01',
        'session_04_02',
    ]
    # For all the sessions at once
    # for session in sessions:
    #     main_split(session)
    # for session in sessions:
    #     concatenate_sets(session)
    #
    # For one specific session
    main_split('session_04_01', 'specialist')
