import tensorflow as tf
from tensorflow.keras.layers import Dense, Flatten, Conv2D
from tensorflow.keras.models import Sequential
import urllib.request as request
from zipfile import ZipFile
from pathlib import Path
from src.entity.config_entity import BaseModelConfig


class prepareBaseModel:
    def __init__(self, config: BaseModelConfig):
        self.config = config
    
    @staticmethod
    def save_model(path: Path, model: tf.keras.Model):
        model.save(path)
        
    def get_base_model(self):
        self.model = tf.keras.applications.vgg16.VGG16(
            input_shape=self.config.params_image_size,
            weights=self.config.params_weights,
            include_top=self.config.params_include_top
            )
        self.save_model(self.config.base_model_path, self.model)
    
    @staticmethod
    def _prepare_full_model(model, classes, learning_rate):
        full_model = Sequential([model,
                                 Flatten(),
                                 Dense(units=256, activation='relu'),
                                 Dense(units=classes, activation='softmax')])
        full_model.compile(
            optimizer=tf.keras.optimizers.SGD(learning_rate=learning_rate),
            loss=tf.keras.losses.CategoricalCrossentropy(),
            metrics=["accuracy"])

        full_model.summary()
        return full_model
    
    def update_base_model(self):
        self.full_model = self._prepare_full_model(
            model=self.model,
            classes=self.config.params_classes,
            learning_rate=self.config.params_learning_rate)
        
        self.save_model(self.config.updated_base_model_path,
                        model=self.full_model)