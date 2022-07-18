import pathlib
import os.path

from decouple import config

main_folder = pathlib.Path(__file__).parent.parent.absolute()
MAIN_FOLDER = config('MAIN_FOLDER', default=main_folder)

# labels
annotated_dataset_directory = os.path.join(MAIN_FOLDER, 'annotated_dataset')
pkl_directory = os.path.join(MAIN_FOLDER, 'pkl_datasets')
pkl_directory_labels = os.path.join(pkl_directory, 'labels')
per_class_pkl_directory = os.path.join(pkl_directory_labels, 'per_class')
split_pkl_directory = os.path.join(pkl_directory_labels, 'split')
per_class_split_pkl_directory = os.path.join(pkl_directory_labels, 'per_class_split')

ANNOTATED_DATASET_DIRECTORY = config('ANNOTATED_DATASET_DIRECTORY', default=annotated_dataset_directory)
PKL_DIRECTORY = config('PKL_DIRECTORY', default=pkl_directory)
PER_CLASS_PKL_DIRECTORY = config('PER_CLASS_PKL_DIRECTORY', default=per_class_pkl_directory)
SPLIT_PKL_DIRECTORY = config('SPLIT_PKL_DIRECTORY', default=split_pkl_directory)
PER_CLASS_SPLIT_PKL_DIRECTORY = config('PER_CLASS_SPLIT_PKL_DIRECTORY', default=per_class_split_pkl_directory)
PKL_DIRECTORY_LABELS = config('PKL_DIRECTORY_LABELS', default=pkl_directory_labels)

# features
features_dataset_directory = os.path.join('MAIN_FOLDER', 'feature_dataset')
video_features_dataset_directory = os.path.join(features_dataset_directory, 'video')

FEATURES_DATASET_DIRECTORY = config('FEATURES_DATASET_DIRECTORY', default=features_dataset_directory)
VIDEO_FEATURES_DATASET_DIRECTORY = config('VIDEO_FEATURES_DATASET_DIRECTORY', default=video_features_dataset_directory)
