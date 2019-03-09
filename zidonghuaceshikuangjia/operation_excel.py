#coding=utf-8
import xlrd
data = xlrd.open_workbook('../dataconfig/interface.xlsx')
table = data.sheet_by_index(0)
print(table.nrows)
print(table.cell_value(2,2))

