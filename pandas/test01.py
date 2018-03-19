#! -*- coding: UTF-8 -*-
#
#   @author zhaoxin
#   @date 2018-03-19
#


import tensorflow as tf
import pandas as pd
import numpy as np


def basic_op():
    city_names = pd.Series(['San Francisco', 'San Jose', 'Sacramento'])
    population = pd.Series([852469, 1015785, 485199])
    pd.DataFrame({ 'City name': city_names, 'Population': population })

def read_csv():
    print("将整个文件加载到 DataFrame")
    california_housing_dataframe = pd.read_csv("california_housing_train.csv", sep=",")
    california_housing_dataframe.describe()


def main():

    print("BEGIN")
    basic_op()

    print("END")


if __name__ == '__main__':

    main()
