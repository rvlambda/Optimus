from pyspark.sql.types import *
from optimus import Optimus
from optimus.helpers.json import json_enconding 
from pyspark.ml.linalg import Vectors, VectorUDT, DenseVector
import numpy as np
nan = np.nan
import datetime
from pyspark.sql import functions as F
from optimus.ml import distancecluster as dc
op = Optimus(master='local')
class Testdf_distance_cluster(object):
	@staticmethod
	def test_levenshtein_filter():
		actual_df =dc.levenshtein_filter(source_df,'STATE')
		expected_df = op.create.df([('STATE_FROM', StringType(), True),('STATE_LEVENSHTEIN_DISTANCE', IntegerType(), True),('STATE_TO', StringType(), True)], [('estadodemexico', 11, 'distritofederal'), ('distritofederal', 11, 'estadodemexico')])
		assert (expected_df.collect() == actual_df.collect())
	@staticmethod
	def test_levenshtein_matrix():
		actual_df =dc.levenshtein_matrix(source_df,'STATE')
		expected_df = op.create.df([('STATE_LEVENSHTEIN_1', StringType(), True),('STATE_LEVENSHTEIN_2', StringType(), True),('STATE_LEVENSHTEIN_DISTANCE', IntegerType(), True)], [('estadodemexico', 'estadodemexico', 0), ('estadodemexico', 'distritofederal', 11), ('distritofederal', 'estadodemexico', 11), ('distritofederal', 'distritofederal', 0)])
		assert (expected_df.collect() == actual_df.collect())