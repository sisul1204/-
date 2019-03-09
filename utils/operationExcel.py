#coding=utf-8
import xlrd

from utils.public import *
from utils.excel_data import *
class OperationExcel:
	def getExcel(self):
		db = xlrd.open_workbook(data_dir('data','data.xlsx'))
		sheet = db.sheet_by_index(0)
		return sheet

	def get_rows(self):
		'''获取excel的行数'''
		return self.getExcel().nrows

	def get_row_cel(self,row,col):
		'''获取单元格的内容'''
		return self.getExcel().cell_value(row,col)

	def getCaseID(self,row):
		self.get_row_cel(row,getCaseID())

	def get_url(self,row):
		return self.get_row_cel(row,getUrl())

	def get_request_data(self,row):
		return self.get_row_cel(row,get_request_data())

	def getExpect(self,row):
		return self.get_row_cel(row,get_expect())

	def getResult(self,row):
		return self.get_row_cel(row,get_result())
'''
opera = OperationExcel()
print(opera.get_request_data(1))
'''