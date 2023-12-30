from pathlib import Path
import os
from src.common import read_yaml, config_path, params_path
from src.entity.config_entity import (DataIntegrationConfig, 
                                      BaseModelConfig,
                                      TrainModelConfig,
                                      EvaluationConfig)


#  config_path, params_path
class ConfigurationManager:
    def __init__(self):
        self.config_path = config_path
        self.params_path = params_path
        # read config params
        self.config = read_yaml(self.config_path)
        self.params = read_yaml(self.params_path)
  
    def get_data_ingestion_prams(self) -> DataIntegrationConfig:
        config = self.config.data_ingestion
        return DataIntegrationConfig(
            root_dir=config.root_dir,
            source_url=config.source_url,
            zip_path=config.zip_path,
            extract_path=config.extract_path
        )

    def get_prepare_base_model_config(self) -> BaseModelConfig:
        config = self.config.prepare_base_model
        
        return BaseModelConfig(
            root_dir=Path(config.root_dir),
            base_model_path=Path(config.base_model_path),
            updated_base_model_path=Path(config.updated_base_model_path),
            params_agumentation=self.params.AUGMENTATION,
            params_image_size=self.params.IMAGE_SIZE,
            params_learning_rate=self.params.LEARNING_RATE,
            params_include_top=self.params.INCLUDE_TOP,
            params_weights=self.params.WEIGHTS,
            params_classes=self.params.CLASSES
            )

    def get_training_config(self) -> TrainModelConfig:
        print(self.config)
        training = self.config.training
        prepare_base_model = self.config.prepare_base_model
        params = self.params
        training_data = os.path.join(self.config.data_ingestion.extract_path,
                                     "data") 
        
        return TrainModelConfig(
            root_dir=Path(training.root_dir),
            trained_model_path=Path(training.trained_model_path),
            updated_base_model_path=Path(
                                prepare_base_model.updated_base_model_path),
            training_data=Path(training_data),
            params_epochs=params.EPOCHS,
            params_batch_size=params.BATCH_SIZE,
            params_is_augmentation=params.AUGMENTATION,
            params_image_size=params.IMAGE_SIZE
            )
        
    def get_evaluation_config(self) -> EvaluationConfig:
            return EvaluationConfig(
                    path_of_model = self.config.prepare_base_model,
                    validation_path = self.config.data_ingestion.validation_path,
                    all_params = self.params,
                    mlflow_uri = "https://dagshub.com/goldirana1111/kidney_scans.mlflow",
                    params_image_size = self.params.IMAGE_SIZE,
                    params_batch_size = self.params.BATCH_SIZE
            )