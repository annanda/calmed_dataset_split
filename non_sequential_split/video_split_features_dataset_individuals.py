import os.path
import pandas as pd

from non_sequential_split.conf import FEATURES_DATASET_DIRECTORY, \
    VIDEO_FEATURES_DATASET_DIRECTORY, PKL_DIRECTORY_LABELS, PKL_DIRECTORY_FEATURES_VIDEO, PKL_DIRECTORY_FEATURES


def generate_split_per_feature(session, feature, annotation_type):
    """
    It receives a feature name and generate the split train, dev, test sets for the dataset of the given feature.
    :param feature:
    :param annotation_type: str 'parents' or 'specialist' to tell which annotation to use.
    :return:
    """
    train_label = pd.read_pickle(
        os.path.join(PKL_DIRECTORY_LABELS, annotation_type, 'split', session, f'{session}_train.pkl'))
    dev_label = pd.read_pickle(
        os.path.join(PKL_DIRECTORY_LABELS, annotation_type, 'split', session, f'{session}_dev.pkl'))
    test_label = pd.read_pickle(
        os.path.join(PKL_DIRECTORY_LABELS, annotation_type, 'split', session, f'{session}_test.pkl'))

    features_folder_read = os.path.join(VIDEO_FEATURES_DATASET_DIRECTORY, feature, session)
    all_feature_files = os.listdir(features_folder_read)
    all_feature_files = [file for file in all_feature_files if '.csv' in file]
    features_folder_write = os.path.join(PKL_DIRECTORY_FEATURES, annotation_type, 'video', feature, session)
    if not os.path.exists(features_folder_write):
        os.makedirs(features_folder_write)

    for feature_file in all_feature_files:
        name = feature_file.replace('.csv', '')
        feature_pd = pd.read_csv(os.path.join(features_folder_read, feature_file))

        result_train = train_label.merge(feature_pd, on="frametime", how='inner')
        result_train = result_train.drop(columns=['session'])
        result_train.to_pickle(os.path.join(features_folder_write, f'{name}_train.pkl'))
        # result_train.to_csv(os.path.join(features_folder_write, f'{name}_train.csv'))

        result_dev = dev_label.merge(feature_pd, on="frametime", how='inner')
        result_dev = result_dev.drop(columns=['session'])
        result_dev.to_pickle(os.path.join(features_folder_write, f'{name}_dev.pkl'))
        # result_dev.to_csv(os.path.join(features_folder_write, f'{name}_dev.csv'))

        result_test = test_label.merge(feature_pd, on="frametime", how='inner')
        result_test = result_test.drop(columns=['session'])
        result_test.to_pickle(os.path.join(features_folder_write, f'{name}_test.pkl'))
        # result_test.to_csv(os.path.join(features_folder_write, f'{name}_test.csv'))


def generate_split_all_video_features():
    sessions = [
        'session_01_01',
        'session_02_01',
        'session_02_02',
        'session_03_01',
        'session_03_02',
        'session_04_01',
        'session_04_02',
    ]
    video_features = [
        '2d_eye_landmark',
        '3d_eye_landmark',
        'AU',
        'face_2d_landmarks',
        'face_3d_landmarks',
        'gaze',
        'head_pose',
    ]

    for session in sessions:
        for feature in video_features:
            generate_split_per_feature(session, feature, 'specialist')


if __name__ == '__main__':
    feature_name = 'AU'
    # generate_split_per_feature('session_01_01', feature_name, 'specialist')
    # testing_split_by_frametime()

    generate_split_all_video_features()
