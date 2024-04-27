import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017")
db = client['test']
collection = db['daveshop']

## 크롤링을 이용하여 해당 데이터를 mongodb에 넣기
# for page_num in range(10):
#     if page_num == 0:
#         res = requests.get("https://davelee-fun.github.io/")
#     else:
#         res = requests.get("https://davelee-fun.github.io/page" + str(page_num + 1) + "/")
#     soup = BeautifulSoup(res.content, 'html.parser')
#     data = soup.select("div.card-body")
#     for item in data:
#         category = item.select_one("h2.card-title").get_text().replace("관련 상품 추천", "").strip()
#         product = item.select_one("h4.card-text").get_text().replace("상품명: ", "").strip()
#         collection.insert_one(
#             {"category": category, "product": product}
#         )

# 'category' 필드에 있는 모든 카테고리 종류를 조회하세요.
category_distinct = collection.distinct("category")
print(category_distinct)

# 모든 상품(product)을 조회하세요.
pipeline = [
    {"$project": {"_id":0, "product": 1}}
]
for product in collection.aggregate(pipeline):
    print(product)

# "매트리스커버" 카테고리의 모든 상품을 조회하세요. (find와 aggregation을 사용한 코드를 각각 작성해주세요)
# find 사용
matrix_list = collection.find({"category": "매트리스커버"}, {"_id":0, "product": 1})
for matrix in matrix_list:
    print(matrix)
# aggregation 사용
pipeline = [
    {"$match": {"category": "매트리스커버"}},
    {"$project": {"_id":0, "product":1}}
]
for matrix in collection.aggregate(pipeline):
    print(matrix)

# 각 카테고리별 상품 수를 조회하세요. 이를 위해 MongoDB의 aggregation 기능을 사용하세요.
pipeline = [
    {"$group": {"_id": "$category", "product": {"$sum": 1}}}
]
for cnt in collection.aggregate(pipeline):
    print(cnt)

# 상품명(product)에 "핑크"가 포함된 모든 상품을 조회하세요.
result = collection.find( {"product": {"$regex": ".*핑크.*"}}, {"_id":0, "product":1} )
for pink in result:
    print(pink)

# '매트리스커버' 카테고리의 상품 중, 상품명에 '차콜'이 포함된 상품을 조회하세요.
result = collection.find( {"category": "매트리스커버", "product": {"$regex": ".*차콜.*"}}, {"_id":0, "product":1})
for data in result:
    print(data)

# 'product' 필드에 대한 텍스트 인덱스를 생성하세요.
collection.create_index([('product', 'text')])

# 'product' 필드에서 '누빔' 이라는 단어를 포함하는 모든 문서를 텍스트 검색을 이용해 찾으세요.
# find 사용
result = collection.find( {"$text": {"$search": "누빔"}}, {"_id":0, "product":1} )
for i in result:
    print(i)

# aggergation 사용
pipeline = [
    {"$match": {"$text": {"$search": "누빔"}}},
    {"$project": {"_id":0, "product":1}}
]
for i in collection.aggregate(pipeline):
    print(i)

client.close()