import requests
import json
n = input("请输入查询股票类别关键词\n")
m = input("请输入想访问该股票第几页\n")
a = input("请输入像保存的文件名(文件名不可重复)\n")
url = 'http://ai.iwencai.com/urp/v7/landing/getDataList'
headers = {
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36',
}
data={
    'query': n,
    'urp_sort_way': 'desc',
    'urp_sort_index': '',
    'page': m,
    'perpage': 50,
    # 'condition': '[{"indexName":"所属指数类","indexProperties":["包含科技100"],"source":"new_parser","type":"index","indexPropertiesMap":{"包含":"科技100"},"reportType":"null","chunkedResult":"科技","valueType":"_所属指数类","domain":"abs_股票领域","uiText":"所属指数类是科技","sonSize":0,"queryText":"所属指数类是科技","relatedSize":0,"tag":"所属指数类"}]',
    'codelist': '',
    'logid': '6d918953e1d307b1a2981fb5e9334bec',
    'ret': 'json_all',
    'sessionid': '8281bea5d8ce6d509d732cb877609f2f',
    'date_range[0]': 20201130,
    # 'iwc_token': 'c0a8d1d716067400679515564',
    'urp_use_sort': 1,
    'user_id': 554665253,
    'uuids[0]': 24087,
    'query_type': 'stock',
    'comp_id': 5547544,
    'business_cat': 'soniu',
    'uuid': 24087,
}
response = requests.post(url,data).content
response = json.loads(response)
print(response)
list=[]
datas = response['answer']['components'][0]['data']['datas']
list.append(datas)
print(list)
with open(f'{a}.json','w') as f:
        for i in list[0]:
            info = json.dumps(i,ensure_ascii=False)
            f.write(info + '\n')
