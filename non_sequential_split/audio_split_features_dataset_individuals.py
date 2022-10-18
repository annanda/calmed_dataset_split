import os.path
import pandas as pd

from non_sequential_split.conf import FEATURES_DATASET_DIRECTORY, \
    AUDIO_FEATURES_DATASET_DIRECTORY, SPLIT_PKL_DIRECTORY_LABELS, PKL_DIRECTORY_FEATURES_AUDIO, LLD_PARAMETER_GROUP


def generate_split_per_feature(session, feature_group, feature_level='functionals'):
    """
    It receives a feature name and generate the split train, dev, test sets for the dataset of the given feature.
    :param feature_group:
    :return:
    """
    train_label = pd.read_pickle(os.path.join(SPLIT_PKL_DIRECTORY_LABELS, session, f'{session}_train.pkl'))
    dev_label = pd.read_pickle(os.path.join(SPLIT_PKL_DIRECTORY_LABELS, session, f'{session}_dev.pkl'))
    test_label = pd.read_pickle(os.path.join(SPLIT_PKL_DIRECTORY_LABELS, session, f'{session}_test.pkl'))

    features_of_group = LLD_PARAMETER_GROUP[feature_group]

    for feature in features_of_group:
        features_folder_read = os.path.join(AUDIO_FEATURES_DATASET_DIRECTORY, feature_level, feature_group, feature,
                                            session)
        all_feature_files = os.listdir(features_folder_read)
        all_feature_files = [file for file in all_feature_files if '.csv' in file]
        features_folder_write = os.path.join(PKL_DIRECTORY_FEATURES_AUDIO, feature_level, feature_group, feature,
                                             session)
        if not os.path.exists(features_folder_write):
            os.makedirs(features_folder_write)

        for feature_file in all_feature_files:
            name = feature_file.replace('.csv', '')
            feature_pd = pd.read_csv(os.path.join(features_folder_read, feature_file))

            result_train = train_label.merge(feature_pd, on="frametime", how='inner')
            result_train.to_pickle(os.path.join(features_folder_write, f'{name}_train.pkl'))

            result_dev = dev_label.merge(feature_pd, on="frametime", how='inner')
            result_dev.to_pickle(os.path.join(features_folder_write, f'{name}_dev.pkl'))

            result_test = test_label.merge(feature_pd, on="frametime", how='inner')
            result_test.to_pickle(os.path.join(features_folder_write, f'{name}_test.pkl'))


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
    feature_group = [
        'frequency',
        'energy_amplitude',
        'spectral_balance',
        'temporal_features'
    ]

    for session in sessions:
        for feature in feature_group:
            generate_split_per_feature(session, feature)


if __name__ == '__main__':
    # feature_name = '2d_eye_landmark'
    # generate_split_per_feature('session_01_01', feature_name)
    # testing_split_by_frametime()

    generate_split_all_video_features()
