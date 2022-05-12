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
# print(stock_zt_pool_em_df) +str(random.randint(0, 10000))
# print(df)
file_name = str(date.today()) + '_' + str(random.randint(0, 10000)) + '_Astock.xlsx'
gb_file_name_01 = str(date.today()) + '_' + str(random.randint(0, 10000)) + '_Astock_ana.xlsx'

# print(file_name)
df.to_excel('./data/'+file_name)
# 创建集合，存涨停行业
limit_type_1 = set(df['连板数'])
limit_type = set()
for item in limit_type_1:
    item_str = str(item)
    limit_type.add(item_str)

info = {}

for item in limit_type:
    data_list = list(df[df['连板数'] == int(item)]['代码'])

    info[item] = "，".join(data_list)
df2 = pd.DataFrame.from_dict(info, orient='index', columns=['value'])
df2.to_excel('./data/' + gb_file_name_01)
print(df2.index)