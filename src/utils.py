import os
import sys
import pandas as pd
from src.exception import CustomException


def tranform_data(df):
    try: 
        df = df.drop(['Unnamed: 0','flight'],axis=1)
        df['class'] = df['class'].apply(lambda x: 1 if x == 'Business' else 0 )
        df['stops'] = pd.factorize(df['stops'])[0]
        df = df.join(pd.get_dummies(df['airline'],prefix='airline',dtype=int)).drop('airline',axis=1)
        df = df.join(pd.get_dummies(df['source_city'],prefix='source',dtype=int)).drop('source_city',axis=1)
        df = df.join(pd.get_dummies(df['destination_city'],prefix='dest',dtype=int)).drop('destination_city',axis=1)
        df = df.join(pd.get_dummies(df['departure_time'],prefix='departure',dtype=int)).drop('departure_time',axis=1)
        df = df.join(pd.get_dummies(df['arrival_time'],prefix='arrival',dtype=int)).drop('arrival_time',axis=1)

        return df
    
    except Exception as e:
        raise CustomException(e,sys)


    