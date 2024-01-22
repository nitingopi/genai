import pandas as pd
class Dataframes:
    def __init__(self ):
        pass

    def create_dataframe(self,data):
        return pd.read_csv(data)
    
    def merge_inner_dataframes(self,df1,df2,on):
        return pd.merge(df1,df2,on=on)
  
