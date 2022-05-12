import akshare as ak
from pandas import DataFrame
from datetime import date
import pandas as pd
import random

"""
1、获得所有涨停的股票，对应的连板情况，概念类型，板块类型
"""

# 东方财富网-行情中心-涨停板行情-涨停股池
# df: DataFrame = ak.stock_zt_pool_em(date=str(date.today()))
df: DataFrame = ak.stock_zt_pool_em(date='20220511')
writer = pd.ExcelWriter(r'D:\py\py2022\data\2022-05-11_179_Astock_ana.xlsx',mode='a', engine='openpyxl',if_sheet_exists='new')
df.to_excel(writer, sheet_name='xxxx')
writer.save()
writer.close()