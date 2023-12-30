from src import logger
from src.config.configuration import ConfigurationManager
from src.data.data_ingestion import dataIngestion

STAGE_NAME = "Data Ingestion Stage"


class dataIngestionTrainingPipeline:
    def __init__(self):
        pass
    
    def main(self):
        config = ConfigurationManager()
        data_ingestion_config = config.get_data_ingestion_prams()
        data_ingestion = dataIngestion(data_ingestion_config)
        data_ingestion.download_data()
        data_ingestion.extract_data()

       
if __name__ == "__main__":
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = dataIngestionTrainingPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e