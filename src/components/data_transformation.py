'''
Data transformation is the process of changing the format, structure, or values of data. 
The main purpose is data cleaning, feature engineering, feature transforming etc
'''

import sys
import os
from dataclasses import dataclass
import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler

from src.exception import CustomException
from src.logger import logging
from src.utils import save_object

@dataclass
class DataTransformationConfig:
    #to store for data transformation
    preprocessor_obj_file_path = os.path.join('artifacts','preprocessor.pkl')

class DataTransformation:
    def __init__(self):
        self.data_transformation_config = DataTransformationConfig()

    def get_data_transformer_object(self):
        try:
            
            numerical_columns = ["writing_score", "reading_score"]
            categorical_columns = [
                "gender",
                "race_ethnicity",
                "parental_level_of_education",
                "lunch",
                "test_preparation_course",
            ]

            #creating a pipeline
            #for numerical features
            num_pipeline = Pipeline(
                steps = [
                    ("imputer",SimpleImputer(strategy='median')),  #for missing values
                    ('scaler',StandardScaler()) #scaling
                ]
            )

            cat_pipeline = Pipeline(
                steps = [
                    ("imputer",SimpleImputer(strategy='most_frequent')),
                    ("one_hot_encoder",OneHotEncoder()),
                    ('scaler',StandardScaler(with_mean=False))
                ]
            )

            preprocessor = ColumnTransformer(
                [
                    ("num_pipeline",num_pipeline,numerical_columns),
                    ("ncat_pipeline",cat_pipeline,categorical_columns)
                ]
            )

            return preprocessor

        except Exception as e:
            raise CustomException(e,sys)

    #getting data from data ingestion
    def initiate_data_transformation(self,train_path,test_path): 
        try:
            train_df = pd.read_csv(train_path)
            test_df = pd.read_csv(test_path)

            logging.info("Read train and test data completed")
            logging.info("Obtaining Preprocessing object")

            preprocessing_obj = self.get_data_transformer_object()

            #setting target column
            target_column_name = "math_score"
            numerical_columns = ["writing_score", "reading_score"]

            #setting dependent and independent features for training 
            input_feature_train_df = train_df.drop(columns=[target_column_name],axis=1)
            target_feature_train_df = train_df[target_column_name]

            #setting dependent and independent features for testing
            input_feature_test_df = test_df.drop(columns=[target_column_name],axis=1)
            target_feature_test_df = test_df[target_column_name]

            logging.info("Applying preprocessing object on training dataframe and testing dataframe")
            
            #applying preprocessing on training and testing dataset
            input_feature_train_arr=preprocessing_obj.fit_transform(input_feature_train_df)
            input_feature_test_arr=preprocessing_obj.transform(input_feature_test_df)

            #the np.c_ func used to concatenate two arrays, 1) input_feature_train_arr and np.array(target_feature_train_df)
            train_arr = np.c_[input_feature_train_arr, np.array(target_feature_train_df)]
            test_arr = np.c_[input_feature_test_arr, np.array(target_feature_test_df)]

            logging.info(f"Saved preprocessing object.")


            #saving transformation and preprocessing object as pkl file using save_object function from utils
            save_object(
                file_path=self.data_transformation_config.preprocessor_obj_file_path,
                obj=preprocessing_obj
                )
            
            return (
                train_arr,
                test_arr,
                self.data_transformation_config.preprocessor_obj_file_path,
            )

        except Exception as e:
            raise CustomException(e,sys)

