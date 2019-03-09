#coding=utf-8

import unittest
class TestMethod(unittest.TestCase):
	@classmethod
	def setUpClass(cls):
		print('类执行之前的方法')

	def setUp(self):
		print('test---->setUp')
	@classmethod
	def tearDownClass(cls):
		print('类执行之后的方法')

	def tearDown(self):
		print('test---->tearDown')


	def test_01(self):
		print('test01')
	def test_02(self):
		print('test02')

if __name__ == '__main__':
	unittest.main()