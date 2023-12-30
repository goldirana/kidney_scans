from dataclasses import dataclass
from pathlib import Path


@dataclass
class DataIntegrationConfig:
    root_dir: Path
    source_url: str
    zip_path: Path
    extract_path: Path


@dataclass
class BaseModelConfig:
    root_dir: Path
    base_model_path: Path
    updated_base_model_path: Path
    params_agumentation: bool
    params_image_size: list
    params_learning_rate: float
    params_include_top: bool
    params_weights: str
    params_classes: int


@dataclass
class TrainModelConfig:
    root_dir: Path
    trained_model_path: Path
    updated_base_model_path: Path
    training_data: Path
    params_epochs: int
    params_batch_size: int
    params_is_augmentation: bool
    params_image_size: list