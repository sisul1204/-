#coding=utf-8
import os

def data_dir(data='data',fileName=None):
	'''查看文件的路径'''
	return os.path.join(os.path.dirname(os.path.dirname(__file__)),data,fileName)

#print(data_dir('data','data.xls'))
