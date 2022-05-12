import akshare as ak
from pandas import DataFrame
from datetime import date
import pandas as pd
import random
from openpyxl import load_workbook
import xlrd
import numpy as np

df_stock = pd.read_excel(r'D:\py\py2022\data\source_data\Table111.xlsx')
v_industry = df_stock['涨停分析']
# print(v_industry)
l_industry = v_industry.str.split('+')
# print(l_industry)
base_industry = set()
for item in l_industry:  # ['零售', '预制菜', '社区团购']
    base_industry = base_industry.union(set(item))
l_ind = df_stock[df_stock['涨停分析'].str.contains('零售')]['    名称']
print(set(l_ind))



