import pathlib
import os.path

from decouple import config

main_folder = pathlib.Path(__file__).parent.parent.absolute()
MAIN_FOLDER = config('MAIN_FOLDER', default=main_folder)

annotated_dataset_directory = os.path.join(MAIN_FOLDER, 'annotated_dataset')
pkl_directory = os.path.join(MAIN_FOLDER, 'pkl_datasets', 'labels')
per_class_pkl_directory = os.path.join(pkl_directory, 'labels', 'per_class')
split_pkl_directory = os.path.join(pkl_directory, 'labels', 'split')
per_class_split_pkl_directory = os.path.join(pkl_directory, 'labels', 'per_class_split')

ANNOTATED_DATASET_DIRECTORY = config('ANNOTATED_DATASET_DIRECTORY', default=annotated_dataset_directory)
PKL_DIRECTORY = config('PKL_DIRECTORY', default=pkl_directory)
PER_CLASS_PKL_DIRECTORY = config('PER_CLASS_PKL_DIRECTORY', default=per_class_pkl_directory)
SPLIT_PKL_DIRECTORY = config('SPLIT_PKL_DIRECTORY', default=split_pkl_directory)
PER_CLASS_SPLIT_PKL_DIRECTORY = config('PER_CLASS_SPLIT_PKL_DIRECTORY', default=per_class_split_pkl_directory)
