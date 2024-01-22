import unittest
from dataframes import Dataframes

class DataframesTest(unittest.TestCase):
    def test_create_dataframe(self):
        df = Dataframes()
        df1 = df.create_dataframe('data1.csv')
        self.assertEqual(len(df1), 2)

    def test_merge_inner_dataframes(self):
        df = Dataframes()
        df1 = df.create_dataframe('data1.csv')
        df2 = df.create_dataframe('data2.csv')
        on = ['id']
        df3 = df.merge_inner_dataframes(df1, df2,on)
        print(df3.head())
        self.assertEqual(len(df3), 3)