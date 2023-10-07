# MONGODB 기본 명령어

## 1. 전체 데이터베이스 확인
    show dbs
## 2. 데이터베이스 선택과 생성
### 데이터베이스가 없으면 생성 및 선택 있으면 선택
    show [DB 이름]
## 3. 선택한 데이터베이스 collection 확인
    show collections
## 4. collection 활용 방법
    db.[collection 이름].함수()
    ex) db.test.find()
## 5. 데이터베이스 상세 정보 확인
    db.stats()
## 6. 데이터베이스 또는 collection 삭제
    db.dropDatabase()
    db.[collection 이름].drop()
## 7. collection 생성
    db.createCollection(name, options)
options에는 capped, size, max 등이 있음
## 8. collection 이름 변경
    db.[collection 이름].renameCollection([변경할 collection 이름])
