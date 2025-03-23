import sys
import pandas as pd
from src.exception import CustomException
from src.utils import load_object
from src.logger import logging


class PredictPipeline:
    def __init__(self):
        pass

    def predict(self,features):
        try:
            
            # Regular model pkl file
            #model_path = 'artifacts/model.pkl'

            preprocessor_path = 'artifacts/preprocessor.pkl'
            preprocessor = load_object(file_path=preprocessor_path)
            data_transformed = preprocessor.transform(features)
            # preds = model.predict(data_transformed)
            
            return data_transformed
        
        except Exception as e:
            raise CustomException(e,sys)
        

class CustomData:
    def __init__(self,
                 airline:str,
                 source_city:str,
                 departure_time:str,
                 stops:str,
                 arrival_time:str,
                 destination_city:str,
                 Class:str,
                 duration:float,
                 days_left:int):
        
        self.airline = airline
        self.source_city = source_city
        self.departure_time = departure_time
        self.stops = stops
        self.arrival_time = arrival_time
        self.destination_city = destination_city
        self.Class = Class
        self.duration = duration
        self.days_left = days_left

    def get_data_as_data_frame(self):
        try:
            custom_data_input_dict = {
                "airline" : [self.airline],
                "source_city" : [self.source_city],
                "departure_time" : [self.departure_time],
                "stops" : [self.stops],
                "arrival_time" : [self.arrival_time],
                "destination_city" : [self.destination_city],
                "Class" : [self.Class],
                "duration" : [self.duration],
                "days_left" : [self.days_left],
            }

            return pd.DataFrame(custom_data_input_dict)
        
        except Exception as e:
            raise CustomData(e,sys)