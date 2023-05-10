'''
Data ingestion is the process of importing large, assorted data files from multiple sources into a 
single, cloud-based storage medium—a data warehouse, data mart or database—where it can be accessed and analyzed.
'''

import os
import sys
from src.exception import CustomException
from src.logger import logging

import pandas as pd
from sklearn.model_selection import train_test_split
from dataclasses import dataclass

#for defining variables, can use dataclass
@dataclass
class DataIngestionConfig:
    #given config to the data ingestion components
    #so data injestion knows where to save the train, test, raw data path under artifacts folder
    train_data_path: str=os.path.join('artifacts','train.csv')
    test_data_path: str=os.path.join('artifacts','test.csv')
    raw_data_path: str=os.path.join('artifacts','data.csv')

class DataIngestion:
    def __init__(self):
         # stores train_data_path,test_data_path,raw_data_path in ingestion_config
        self.ingestion_config = DataIngestionConfig() 

    def initial_data_ingestion(self):
        logging.info("entered the data ingesion method or component")
        try:
            #reading the dataset
            df= pd.read_csv("notebook\data\stud.csv")
            logging.info("Read the dataset as dataframe")

            #saving the train data to the specific artifact path
            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path),exist_ok=True)

            #saving the raw data to the specific artifact path
            df.to_csv(self.ingestion_config.raw_data_path,index=False,header=True)

            logging.info("Train Test split Initiated")
            train_set,test_set = train_test_split(df,test_size=0.2,random_state=42)
            
            #saving the train set and test set to the artifact folder 
            train_set.to_csv(self.ingestion_config.train_data_path,index=False,header=True)
            test_set.to_csv(self.ingestion_config.test_data_path,index=False,header=True)

            logging.info("Ingestion of the data completed")

            #Returns the file paths of the train and test data
            return(
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path

            )

        except Exception as e:
            raise CustomException(e,sys)


if __name__=="__main__":
    obj = DataIngestion()
    obj.initial_data_ingestion()

            