class ExcelVariable:
	caseID = 0
	url = 2
	request_data = 3
	expect = 4
	result = 5

def getCaseID():
	return ExcelVariable.caseID

def getUrl():
	return ExcelVariable.url

def get_request_data():
	return ExcelVariable.request_data

def get_expect():
	return ExcelVariable.expect

def get_result():
	return ExcelVariable.result

def getHeadersValue():
	'''获取请求头'''
	headers = {
		'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
		'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Mobile Safari/537.36',
		'Referer': 'https://www.lagou.com/jobs/list_%E8%87%AA%E5%8A%A8%E5%8C%96%E6%B5%8B%E8%AF%95%E5%B7%A5%E7%A8%8B%E5%B8%88?labelWords=&fromSearch=true&suginput=',
		'Cookie': '_ga=GA1.2.1553635082.1493274602; LGUID=20170427143011-f6fd4d43-2b12-11e7-b3e5-5254005c3644; user_trace_token=20181212211326-b5ccc45a-fe0f-11e8-907e-525400f775ce; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22167a28cf2912a6-052e7aaa6ccfb5-36664c08-2073600-167a28cf29238e%22%2C%22%24device_id%22%3A%22167a28cf2912a6-052e7aaa6ccfb5-36664c08-2073600-167a28cf29238e%22%2C%22props%22%3A%7B%22%24latest_utm_source%22%3A%22m_cf_cpt_baidu_pc%22%7D%7D; LG_LOGIN_USER_ID=03bfa2946451ac33bf7a7de4aaa006b025e23d6118f7e9432e86583a50bdf2d5; showExpriedIndex=1; showExpriedCompanyHome=1; showExpriedMyPublish=1; hasDeliver=0; index_location_city=%E6%9D%AD%E5%B7%9E; WEBTJ-ID=20181230165144-167fe4fd79e49d-005ddf299cb4cc-36664c08-2073600-167fe4fd79f212; _gid=GA1.2.520213567.1546159905; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1544938213,1545313846,1545826032,1546159905; LGSID=20181230165144-2253c326-0c10-11e9-ae7e-5254005c3644; PRE_UTM=m_cf_cpt_baidu_pc; PRE_HOST=www.baidu.com; PRE_SITE=https%3A%2F%2Fwww.baidu.com%2Fs%3Fwd%3D%25E6%258B%2589%25E5%258B%25BE%25E7%25BD%2591%26tn%3D98012088_5_dg%26ch%3D11; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2Flp%2Fhtml%2Fcommon.html%3Futm_source%3Dm_cf_cpt_baidu_pc; _putrc=AA201008DE879AF7123F89F2B170EADC; JSESSIONID=ABAAABAAAGGABCB01418C80E71D3810208B0AC0D0527E71; login=true; unick=%E6%9D%8E%E5%BF%97%E9%B9%8F; gate_login_token=8f1f527c69742ba5703a40bf590530e4d5af9d17f5a218c81a59e49e5a63179f; TG-TRACK-CODE=index_search; SEARCH_ID=aa2780d9f9664d96ba25567a6d65679c; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1546159939; LGRID=20181230165219-36e87b7a-0c10-11e9-ae7e-5254005c3644'
	}
	return headers