from cnnClassifier import logger
from cnnClassifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from cnnClassifier.pipeline.stage_02_prepare_base_model import PrepareBaseModelTrainingPipeline
from cnnClassifier.pipeline.stage_03_model_training import ModelTrainingPipeline
from cnnClassifier.pipeline.stage_04_model_evaluation import EvaluationPipeline




STAGE_NAME = "Data Ingestion"
try:
   logger.info(f">>>>>>> stage {STAGE_NAME} started <<<<<<<")
   data_ingestion = DataIngestionTrainingPipeline()
   data_ingestion.main()
   logger.info(f">>>>>>> stage {STAGE_NAME} completed <<<<<<<")
except Exception as e:
        logger.exception(e)
        raise e



STAGE_NAME = "Prepare base model"
try:
   logger.info(f">>>>>>> stage {STAGE_NAME} started <<<<<<<")
   prepare_base_model = PrepareBaseModelTrainingPipeline()
   prepare_base_model.main()
   logger.info(f">>>>>>> stage {STAGE_NAME} completed <<<<<<<")
except Exception as e:
        logger.exception(e)
        raise e


STAGE_NAME = "Model Training"
try:
   logger.info(f">>>>>>> stage {STAGE_NAME} started <<<<<<<")
   prepare_base_model = ModelTrainingPipeline()
   prepare_base_model.main()
   logger.info(f">>>>>>> stage {STAGE_NAME} completed <<<<<<<")
except Exception as e:
        logger.exception(e)
        raise e


STAGE_NAME = "Model Evaluation"
try:
   logger.info(f">>>>>>> stage {STAGE_NAME} started <<<<<<<")
   model_evaluation = EvaluationPipeline()
   model_evaluation.main()
   logger.info(f">>>>>>> stage {STAGE_NAME} completed <<<<<<<")
except Exception as e:
        logger.exception(e)
        raise e