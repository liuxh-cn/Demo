'''
Set Global Parameters for Pandas to Optimize Data Display
pd.set_option('key', value)
    key - value:
        display.
            max_rows
            max_columns
            width
'''
import pandas as pd



pd.set_option('display.max_rows', 10)
pd.set_option('display.max_columns', None)  #显示所有列
pd.set_option('display.width', 1000)