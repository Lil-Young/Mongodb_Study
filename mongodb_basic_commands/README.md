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
$eq    =    equal

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

#### 그 외 문법
##### 1. 정규 표현식을 이용한 검색($regex)
  1-1. "김"이라는 문자열이 들어간 모든 document 검색
   
    db.student.find({name:/김/})
    db.student.find({name: {$regex: /김/}})
   
  1-2. "김"으로 시작하는 모든 document 검색
   
    db.student.find({name:/^김/})
    db.student.find({name: {$regex: /^김/}})
   
##### 2. 정렬(sort)

  2-1. 오름차순 정렬

    db.student.find({age: {$gt:10}}).sort({age:1})
   
  2-2. 내림차순 정렬

    db.student.find({age: {$gt:10}}).sort({age:-1})
   
#### 3. document 개수 세기(count)
    db.student.count()
    db.student.find().count()

#### 4. 필드 존재 여부로 개수 세기($exists)
    db.student.count({name:{$exists:true}})
    db.student.find({name:{$exists:true}}).count()

#### 5. 중복 제거(distinct) - 따옴표("") 사용해야함
    db.student.distinct("name")
    
#### 6. 원하는 만큼 가져오기(limit)
    db.student.find().limit(4) - 4개의 document만 가져오기

#### 7. 배열과 $all, $in, $nin
    db.student.find({hobbies: {$all: ["음악", "영화"]}}) - "음악"과 "영화"를 모두 포함하는 모든 document를 검색
    db.student.find({hobbies: {$in: ["음악", "영화"]}}) - "음악", "영화" 중 하나라도 포함하는 모든 document를 검색
    db.student.find({hobbies: {$nin: ["음악", "영화"]}}) - "음악", "영화" 중 하나라도 포함하지않는 모든 document를 검색
    
## 3. updateOne/updateMany
### 1. updateOne: 매칭되는 한개의 document 수정
    pass
### 2. updateMany: 매칭되는 여러개의 document 수정
    db.student.find({age:{gt:10}}, {$set: {number:3333}}) - age가 10 이상인 모든 document의 number를 3333으로 수정
    db.student.find({age:{gt:30}}, {$inc: {age:3}}) - age가 30 이상인 모든 document의 age를 3씩 증가
    db.student.find({age:{gt:30}}, {$inc: {age:-3}}) - age가 30 이상인 모든 document의 age를 3씩 감소
### 3. 수정 관련 다양한 문법
#### 1. document를 replace 하기
    db.student.updateOne({name:"김이"}, {$set: {"name":"김이이", age:2222, number:1234}})

#### 2. 특정 필드 제거하기
    db.student.updateOne({name:"김삼"}, {$unset: {age:1}}) - name이 "김삼"인 document에서 age 필드 제거

#### 3. 특정 조건을 만족하는 document가 없을 경우 새로 추가하기
    db.student.updateOne({name:"김육"}, {$set: {name: "김육", age:66, number:6666}}, {upsert:true})

#### 4. 여러 document의 특정 필드를 수정하기
    db.student.updateMany({age:{$lte:20}}, {$set: {number:20}})

#### 5. 배열에 값 추가하기
    db.student.updateOne({name:"김일"}, {$push: {hobbies:"공부"}})

#### 6. 배열에서 값 제거하기
    db.student.updateOne({name:"김일"}, {$pull: {hobbies:"공부"}})

## 4. removeOne/removeMany
### 1. removeOne: 매칭되는 한개의 document 삭제
    pass
### 2. removeMany: 매칭되는 여러개의 document 삭제
    db.student.deleteMany({name:"김사"}) - name이 "김사"인 document 삭제
    db.student.deleteMany({}) - student collection에 있는 모든 document 삭제














