import os
import sys
import pandas as pd

from dataclasses import dataclass
from src.exception import CustomException
from src.logger import logging
from src.utils import tranform_data


@dataclass
class DataTransformationConfig:
    encoded_data = os.path.join('artifacts','transformed_data.csv')



class DataTransformation():
    def __init__(self):
        self.data_transformation_config = DataTransformationConfig()

    def initiate_data_transformation(self,train_data,test_data):
        try:
            train_df = pd.read_csv(train_data)
            test_df = pd.read_csv(test_data)

            logging.info("data loaded as train and test df")


            target_feature = 'price'
            input_feature_train_df = train_df.drop(columns=target_feature,axis=1)
            target_feature_train_df = train_df[target_feature]

            input_feature_test_df = test_df.drop(columns=target_feature,axis=1)
            target_feature_test_df = test_df[target_feature]


            encode_input_train_features = tranform_data(input_feature_train_df)
            encode_input_test_features = tranform_data(input_feature_test_df)

            logging.info("Data Transformation Completed")
            encoded_train_df = pd.concat([encode_input_train_features,target_feature_train_df],axis=1)
            encoded_test_df = pd.concat([encode_input_test_features,target_feature_test_df],axis=1)

            encoded_train_df.to_csv(self.data_transformation_config.encoded_data,index=False,header=True)
            
            logging.info("Successfully done")
            return (encoded_train_df,encoded_test_df)
        
        except Exception as e:
            raise CustomException(e,sys)





