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
file_name = str(date.today()) + '_'+ str(random.randint(0, 10000)) + '_Astock.xlsx'
gb_file_name_01 = str(date.today()) + '_'+ str(random.randint(0, 10000)) + '_Astock_ana.xlsx'

# print(file_name)
# df.to_excel('./data/'+file_name)
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
df2 = pd.DataFrame.from_dict(info, orient='index', columns=['股票'])


"""
读取表格，得到涨停分析数据
"""
df_stock = pd.read_excel(r'D:\py\py2022\data\source_data\Table111.xlsx')
v_industry = df_stock['涨停分析']
# print(v_industry)
l_industry = v_industry.str.split('+')
# print(l_industry)
base_industry = set()
for item in l_industry:  # ['零售', '预制菜', '社区团购']
    base_industry = base_industry.union(set(item))
    # print(base_industry)

#
for item in base_industry:
    df2[item] = ''
    for zt_item in df2.index:
        l_zt = df[df['连板数'] == int(zt_item)]['名称']
        l_industry = df_stock[df_stock['涨停分析'].str.contains(item)]['    名称']
        df2[item][zt_item] = "，".join(set(l_zt).intersection(set(l_industry)))
df2.sort_index(axis=0,ascending=False).to_excel('./data/' + gb_file_name_01)   #11

""" 
df2['111'] = ""
df2['111'][2] = 'b'
print(df2)
"""