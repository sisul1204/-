#coding=utf-8
from utils.operationJson import OperationJson
from utils.operationExcel import OperationExcel
import json
from utils.public import *

operationJson = OperationJson()

def setSo(kd='自动化测试工程师'):
	'''对搜索的数据重新赋值'''
	dici1 = operationJson.getRequestData(1)
	print(type(dici1))
	dici1['kd']=kd
	return dici1


def writePositionId(content):
	'''把职位的ID写到文件中'''
	with open(data_dir(fileName='positionId'),'w') as f:
		f.write(content)

def getPositionId():
	'''获取职位招聘信息'''
	with open(data_dir(fileName='positionId'), 'r') as f:
		return json.loads(f.read())
print(getPositionId(),type(getPositionId()))


def setpositionInfo(row):
	dict1 = json.load(operationJson.getRequestData(row=row))
	dict1['positionId'] = getPositionId()[0]
	return dict1


#print(setSo('性能测试工程师'))