import pandas as pd
import openpyxl

df = pd.ExcelFile(r'D:\Python_Practice-1\18-03-2021\Train_Data.xlsx')
# sheet_to_df_map = {}
# for sheet_name in xls.crime:
# sheet_to_df_map[sheet_name] = xls.parse(sheet_name)
abc = input("enter number : ")
for sheet in df.sheet_names:
    y = pd.read_excel(r'D:\Python_Practice-1\18-03-2021\Train_Data.xlsx', sheet_name=sheet)
    y.set_index('TRAIN_NUMBER',inplace = True)
    value = y.loc[abc]
    print(value)

