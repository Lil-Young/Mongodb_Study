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
-----------------------------------------------------------------------
# MONGODB CRUD - student collection 생성했다고 가정

## 1. insertOne/insertMany
### insertOne: 한개의 document 생성
    db.student.insertOne(
        {name:"홍길동", age:35, number:1111}
    )
### insertMany: 여러개의 document 생성 - 리스트 사용
    db.student.insertOne(
    [
        {name:"김일", age:15, number:1111},
        {name:"김이", age:25, number:2222},
        {name:"김삼", age:35, number:3333},
        {name:"김사", age:45, number:4444},
        {name:"김오", age:55, number:5555}
    ])
## 2. findOne/find
### 1. findOne: 매칭되는 한개의 document 검색
    pass
### 2. find: 매칭되는 여러개의 document 검색
    db.student.find() - student collection의 모든 document 검색
    db.student.find({}, {name: 1, age: 1}) - student collection의 name, age _id 만 검색
    db.student.find({}, {name: 1, age: 1, _id: 0}) - student collection의 name, age 만 검색
    db.student.find({name:"김삼"}) - student collection에서 name이 "김삼"인 document 검색
#### 비교 문법
$eq    =    equal \n
$gt    >    greater than
$gte   >=   greater than or equal
$in         values in an array
$lt    <    less than
$lte   <=   less than or equal
$ne    !=   not equal
$nin        values not in an array
    db.student.find({age:{$gt:10}}) - age가 10보다 큰 모든 document 검색
    db.student.find({age:{$lt:30}}) - age가 30보다 작은 모든 document 검색
    db.student.find({age:{$gte:10, $lte:40}}) -age가 10 이상이고 40 이하인 모든 document 검색
#### 논리 연산 문법
$and - AND 조건
$or  - OR 조건
$not - NOT 조건
    db.student.find({$and: [{name:"김오"}, {age:{$eq:55}}]}) - name이 "김오" and age가 55인 document 검색
    db.student.find({$or: [{name:"김오"}, {age:{$eq:55}}]}) - name이 "김오" or age가 33인 document 검색
    db.student.find({age: {$not: {$eq:22}}}) - age != 22인 document 검색
























