#coding=utf-8

import requests
from utils.excel_data import *
from utils.operationExcel import OperationExcel
from utils.operationJson import OperationJson

class Method:
	def __init__(self):
		self.operationJson = OperationJson()
		self.excel = OperationExcel()



	def post(self,row):
		try:
			r = requests.post(
				url=self.excel.get_url(row=row),
				data=self.operationJson.getRequestData(row=row),
				headers=getHeadersValue(),
				timeout=6)
			return r
		except Exception as e:
			raise RuntimeError('接口请求发生未知错误')


	def post(self,row,data):
		try:
			r = requests.post(
				url=self.excel.get_url(row=row),
				data=data,
				headers=getHeadersValue(),
				timeout=6)
			return r
		except Exception as e:
			raise RuntimeError('接口请求发生未知错误')

class IsAssert:
	def __init__(self):
		self.excel = OperationExcel()
	def isContent(self,row,str2):
		flag = None
		if self.excel.getExpect(row=row) in str2:
			flag = True
		else:
			flag = False
		return flag