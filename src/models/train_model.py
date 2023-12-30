import tensorflow as tf
from src.entity.config_entity import TrainModelConfig
from pathlib import Path


class Training:
    def __init__(self, config: TrainModelConfig):
        self.config = config
  
    @staticmethod
    def save_model(path: Path, model: tf.keras.Model):
        model.save(path)
      
    def get_base_model(self):
        self.model = tf.keras.models.load_model(
            self.config.updated_base_model_path)
        
    def train_valid_generator(self):
       
        data_generator_kwargs = dict(
            target_size=self.config.params_image_size[:-1],
            batch_size=self.config.params_batch_size,
            interpolation="bilinear"
        )
        validation_data_gen = tf.keras.preprocessing.image.ImageDataGenerator(
            rescale=1./255,
            validation_split=0.20
        )
        
        self.valid_generator = validation_data_gen.flow_from_directory(
            directory=self.config.training_data,
            shuffle=False,
            **data_generator_kwargs)
        
        # keeping same as validataion data gen
        train_generator = validation_data_gen
        self.train_generator = train_generator.flow_from_directory(
            directory=self.config.training_data,
            shuffle=True,
            **data_generator_kwargs)
        
    def train(self):
        self.steps_per_epoch = 10
        self.validation_steps = 3
        
        self.model.fit(
            self.train_generator,
            epochs=self.config.params_epochs,
            steps_per_epoch=self.steps_per_epoch,
            validation_data=self.valid_generator,
        )
        
        self.save_model(path=self.config.trained_model_path,
                        model=self.model)
        
