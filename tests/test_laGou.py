#coding=utf-8
import unittest
from base.method import Method,IsAssert
from page.laGou import *
from utils.public import *
import json




class LaGou(unittest.TestCase):
	def setUp(self):
		self.obj = Method()
		self.p = IsAssert()

	def statusCode(self,r):
		self.assertEqual(r.status_code, 200)
		self.assertEqual(r.json()['code'], 0)

	def isContent(self,r,row):
		self.statusCode(r=r)
		self.assertTrue(self.p.isContent(row=row,str2=r.text))


	def lltest_laGou_001(self):

		r = self.obj.post(1)
		self.isContent(row=1,r=r)


	def test_laGou_002(self):
		'''拉钩:测试关键字的职位搜索'''
		r = self.obj.post(row=1,data=setSo('架构师'))
		list1 = []
		for i in range(0,15):
			positionId = r.json()['content']['positionResult']['result'][i]['positionId']
			list1.append(positionId)
		writePositionId(json.dumps(list1))
		print(list1)

	def test_laGou_003(self):
		'''测试搜索Python开发工程师查看第一页第一个公司的招聘信息'''
		r = self.obj.post(row=2,data=setpositionInfo(row=2))
		print(r.text)







if __name__ == '__main__':
	unittest.main(verbosity=2)

