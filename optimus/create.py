import logging

from pyspark.sql.types import StructField, StructType

# Helpers
from optimus.helpers.constants import SPARK_DTYPES
from optimus.helpers.functions import parse_spark_dtypes
from optimus.spark import Spark


class Create:

    @staticmethod
    def data_frame(cols, rows):
        """
        Helper to create a Spark dataframe
        :param cols:
        :param rows:
        :return:
        """
        logger = logging.getLogger("analytics")
        logger.debug("data_frame")

        specs = []
        for c in cols:
            value = c[1]
            # Try to find if the type var is a Spark datatype
            if isinstance(value, SPARK_DTYPES):
                var_type = value
            # else, try to parse a str, int, float ......
            else:
                var_type = parse_spark_dtypes(c[1])

            specs.append([c[0], var_type, c[2]])

        struct_fields = list(map(lambda x: StructField(*x), specs))

        return Spark.instance.spark().createDataFrame(rows, StructType(struct_fields))

    df = data_frame
