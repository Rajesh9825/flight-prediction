import os
import sys
import pandas as pd

from dataclasses import dataclass
from src.exception import CustomException
from src.logger import logging
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import LabelEncoder,OneHotEncoder,StandardScaler
from sklearn.impute import SimpleImputer
from sklearn.compose import ColumnTransformer
from src.utils import save_object
import numpy as np



@dataclass
class DataTransformationConfig:
    preprocessor_obj_file_path = os.path.join('artifacts','preprocessor.pkl')


class DataTransformation():
    def __init__(self):
        self.data_transformation_config = DataTransformationConfig()



    def get_data_transformer_object(self):
        '''
        This function is responsible for data transformation
        '''

        try:
            numerical_columns = ["duration","days_left"]
            categorical_column = [
                "airline",
                "source_city",
                "stops",
                "destination_city",
                "departure_time",
                "Class",
                "arrival_time"
                
            ]
        
            num_pipeline = Pipeline(
                steps=[
                    ("imputer", SimpleImputer(strategy="median")),
                    #("scaler", StandardScaler())
                ]
            )

            cat_pipeline = Pipeline(
                steps=[
                    ("one_hot_encoder",OneHotEncoder()),
                    #("scaler",StandardScaler())
                ]
            )

            logging.info(f"Categorical column: {categorical_column}")
            logging.info(f"Numerical column: {numerical_columns}")
            
            preprocessor = ColumnTransformer(
                [
                    ("num_pipeline", num_pipeline, numerical_columns),
                    ("cat_pipeline",cat_pipeline,categorical_column)
                ]
            )

            logging.info("Categorical column encoding completed")

            return preprocessor
        

        except Exception as e:
            raise CustomException(e,sys)
        

    def initiate_data_transformation(self,train_data,test_data):
        try:
            train_df = pd.read_csv(train_data)
            test_df = pd.read_csv(test_data)

            #train_df.head(5)
            logging.info("data loaded as train and test df")

            preprocessor_obj = self.get_data_transformer_object()

            target_feature = 'price'
            input_feature_train_df = train_df.drop(columns=[target_feature],axis=1)
            target_feature_train_df = train_df[target_feature]
           
            input_feature_test_df = test_df.drop(columns=[target_feature],axis=1)
            target_feature_test_df = test_df[target_feature]

            logging.info(
                f"Applying preprocessing object on training dataframe and testing dataframe"
            )

            input_feature_train_arr = preprocessor_obj.fit_transform(input_feature_train_df).toarray()
            input_feature_test_arr = preprocessor_obj.transform(input_feature_test_df).toarray()

            #print(input_feature_train_arr.toarray())
            logging.info("Preprocessing done")
            #print(input_feature_train_arr)
            print("Shape of input_feature_train_arr:", input_feature_train_arr.shape)

            train_arr = np.c_[
                input_feature_train_arr,np.array(target_feature_train_df)
            ]

            test_arr = np.c_[
                input_feature_test_arr,np.array(target_feature_test_df)
            ]

            save_object(
                file_path=self.data_transformation_config.preprocessor_obj_file_path,
                obj = preprocessor_obj
            )

            logging.info(f"Saved Preprocessing objects.")

            return (train_arr,
                test_arr,)
        
        except Exception as e:
            raise CustomException(e,sys)





