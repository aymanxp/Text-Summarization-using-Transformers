from src.TextSummarizer.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from src.TextSummarizer.pipeline.stage_02_data_validation import DataValidationTrainingPipeline
from src.TextSummarizer.logging import logger

STAGE_NAME = "Data Ingestion Stage"

try : 
    logger.info(f">>>> stage {STAGE_NAME} started <<<<")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>> stage {STAGE_NAME} completed <<<<\n\nx=========x")

except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Data Validation Stage"

try : 
    logger.info(f">>>> stage {STAGE_NAME} started <<<<")
    data_validation = DataValidationTrainingPipeline()
    data_validation.main()
    logger.info(f">>>> stage {STAGE_NAME} completed <<<<\n\nx=========x")

except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Data Transformation"

try : 
    logger.info(f">>>> stage {STAGE_NAME} started <<<<")
    data_validation = DataIngestionTrainingPipeline()
    data_validation.main()
    logger.info(f">>>> stage {STAGE_NAME} completed <<<<\n\nx=========x")

    
except Exception as e:
    logger.exception(e)
    raise e
