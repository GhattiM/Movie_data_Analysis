import unittest
import pandas as pd
from pandas.util.testing import assert_frame_equal # <-- for testing dataframes

class DFTests(unittest.TestCase):
""" class for running unittests """

	def setUp(self):
		""" My setUp """
		TEST_INPUT_DIR = 'D:\\'
		test_file_name =  'movie_metadata.csv'
		try:
			data = pd.read_csv(INPUT_DIR + test_file_name,
				sep = ',',
				header = 0)
		except IOError:
			print 'cannot open file'
		self.fixture = data

	def test_dataFrame_constrcutedAsExpected(self):
		""" Test that the dataframe read in equals our expected"""
		foo = pd.Dataframe()
		assert_frame_equal(self.fixture, foo,"oops, there's a bug...")

	def test_for_queries(self):
		query1 = self.fixture.sort_values(['profitability'], ascending=[False])
		query1 = query1[['genres','profitability']].head(10)
		assert_frame_equal(input_df, query1,"oops, there's a bug...")
		query2 = self.fixture.apply(best_actor_director,axis=1).head(10)
		assert_frame_equal(input_df, query2,"oops, there's a bug...")
	
if __name__ == '__main__':
    unittest.main()