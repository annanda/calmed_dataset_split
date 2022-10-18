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
per_class_split_pkl_directory = os.path.join(pkl_directory_labels, 'per_class_split')
split_pkl_directory_labels = os.path.join(pkl_directory_labels, 'split')

ANNOTATED_DATASET_DIRECTORY = config('ANNOTATED_DATASET_DIRECTORY', default=annotated_dataset_directory)
PKL_DIRECTORY = config('PKL_DIRECTORY', default=pkl_directory)
PKL_DIRECTORY_LABELS = config('PKL_DIRECTORY_LABELS', default=pkl_directory_labels)
PER_CLASS_PKL_DIRECTORY = config('PER_CLASS_PKL_DIRECTORY', default=per_class_pkl_directory)
PER_CLASS_SPLIT_PKL_DIRECTORY = config('PER_CLASS_SPLIT_PKL_DIRECTORY', default=per_class_split_pkl_directory)
SPLIT_PKL_DIRECTORY_LABELS = config('SPLIT_PKL_DIRECTORY', default=split_pkl_directory_labels)

# features
features_dataset_directory = os.path.join(MAIN_FOLDER, 'features_dataset')
video_features_dataset_directory = os.path.join(features_dataset_directory, 'video')
audio_features_dataset_directory = os.path.join(features_dataset_directory, 'audio')

pkl_directory_features = os.path.join(pkl_directory, 'features')
pkl_directory_features_video = os.path.join(pkl_directory_features, 'video')
pkl_directory_features_audio = os.path.join(pkl_directory_features, 'audio')

FEATURES_DATASET_DIRECTORY = config('FEATURES_DATASET_DIRECTORY', default=features_dataset_directory)
VIDEO_FEATURES_DATASET_DIRECTORY = config('VIDEO_FEATURES_DATASET_DIRECTORY', default=video_features_dataset_directory)
AUDIO_FEATURES_DATASET_DIRECTORY = config('AUDIO_FEATURES_DATASET_DIRECTORY', default=audio_features_dataset_directory)
PKL_DIRECTORY_FEATURES = config('PKL_DIRECTORY_FEATURES', default=pkl_directory_features)
PKL_DIRECTORY_FEATURES_VIDEO = config('PKL_DIRECTORY_FEATURES_VIDEO', default=pkl_directory_features_video)
PKL_DIRECTORY_FEATURES_AUDIO = config('PKL_DIRECTORY_FEATURES_AUDIO', default=pkl_directory_features_audio)

LLD_PARAMETER_GROUP = {
    'frequency': ['pitch', 'jitter', 'formant_1-3_frequency', 'formant_1-3_bandwidth'],
    'energy_amplitude': ['shimmer', 'loudness', 'harmonics-to-noise_ratio'],
    'spectral_balance': ['alpha_ratio', 'hammarberg_index', 'spectral_slope',
                         'formant_1-3_relative_energy', 'harmonic_difference_H1–H2',
                         'Harmonic_difference_H1–A3', 'mfcc_1–4'],
    'temporal_features': ['temporal_features']
}
