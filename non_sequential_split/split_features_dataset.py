import os.path
import pandas as pd

from setup.conf import FEATURES_DATASET_DIRECTORY, \
    VIDEO_FEATURES_DATASET_DIRECTORY


def generate_split_per_feature(feature):
    """
    It receives a feature name and generate the split train, dev, test sets for the dataset of the given feature.
    :param feature:
    :return:
    """
    pass


def testing_split_by_frametime():
    label_train = pd.read_pickle(
        '/Users/annanda/PycharmProjects/dataset_split/pkl_datasets/labels/split/session_01_01/session_01_01_train.pkl')
    one_feature_example = pd.read_csv(
        '/Users/annanda/PycharmProjects/dataset_split/features_dataset/video/2d_eye_landmark/session_01_01_02.csv')
    # result = one_feature_example.merge(label_train, on="frametime", how='inner')
    result = label_train.merge(one_feature_example, on="frametime", how='inner')
    result.to_pickle(
        '/Users/annanda/PycharmProjects/dataset_split/pkl_datasets/features/video/2d_eye_landmark/session_01_01/session_01_01_02_train.pkl')
    print('hi!')


if __name__ == '__main__':
    feature_name = '2d_eye_landmark'
    # generate_split_per_feature(feature_name)
    testing_split_by_frametime()
