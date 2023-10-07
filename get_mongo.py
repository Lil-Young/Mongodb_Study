import os
from dotenv import load_dotenv
from pymongo import MongoClient

# .env 파일을 로드합니다.
load_dotenv()

# MongoDB 연결 정보를 .env 파일에서 가져옵니다.
mongo_uri = os.getenv("MONGO_URI")
mongo_db = os.getenv("MONGO_DB")
mongo_col = os.getenv("MONGO_COL")

# MongoDB에 연결합니다.
conn = MongoClient(mongo_uri)
db = conn[mongo_db]
col = conn[mongo_col]
print(conn)

# # 연결된 MongoDB 데이터베이스를 선택합니다.
# db = conn.get_database(db)



# 여기에서 MongoDB를 사용하여 작업을 수행할 수 있습니다.
