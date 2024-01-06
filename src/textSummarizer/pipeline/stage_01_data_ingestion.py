from textSummarizer.config.configuration import ConfigurationManager
from textSummarizer.components.data_ingestion import DataIngestion
from textSummarizer.logging import logger

class DataIngestionPipeline:
    def __init__(self):
        pass
    def main(self):
        config=ConfigurationManager()
        data_ingestion_config = config.get_data_ingestion_config()
        data_ingestion = DataIngestion(config=data_ingestion_config)
        data_ingestion.download_data()
        data_ingestion.extract_zip_file()


if __name__ == "__main__":
    data_ingestion_pipeline = DataIngestionPipeline()
    data_ingestion_pipeline.main()