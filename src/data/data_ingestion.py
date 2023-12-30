import zipfile
import gdown
import os
from src import logger


class dataIngestion:
    def __init__(self, config: dict):
        self.config = config
        
    def download_data(self) -> None:
        try:
            dataset_url = self.config.source_url
            zip_path = self.config.zip_path
            logger.info(f"Downloading dataset from url: {dataset_url}")

            os.makedirs("data/raw", exist_ok=True)
            file_id = dataset_url.split("/")[-2]
            prefix = 'https://drive.google.com/uc?/export=download&id='
            gdown.download(prefix+file_id, output=zip_path)
            logger.info(f"Dataset Downloaded to path: {zip_path}")
        except Exception as e:
            logger.info(e)

    def extract_data(self):
        try:
            extract_path = self.config.extract_path
            os.makedirs(extract_path, exist_ok=True)
            with zipfile.ZipFile(self.config.zip_path, 'r') as zip_ref:
                zip_ref.extractall(extract_path)
            logger.info(f'Data is extracted to path: {extract_path}')
        except Exception as e:
            logger.exception(e)