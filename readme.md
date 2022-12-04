# SQL_Maker
-------
# 손쉽게 csv, xlsx파일을 저장하자
- csv, xlsx를 손쉽게 Database table로 제작하자!
- database table에 손쉽게 데이터를 삽입하자!
- MySQL 으로 데이터를 원하는대로 조회하고 csv파일로 저장하자!

------
## 운영체제
- ubuntu 20.04

## 필요한 모듈
- python 3.8.1
- pandas
- PyQt
- mysql
- xlrd

## 사용법
### 파이썬 사용시 초기설정이 필요합니다.
- https://kimbrain.tistory.com/169
- database를 만들어야 접속이 가능합니다.

### 초기화면
![image](https://user-images.githubusercontent.com/110883172/205497212-dbfb6c95-cb35-476e-a03c-efb0b576bc11.png)

### 접속
![image](https://user-images.githubusercontent.com/110883172/205497627-bf3aac2f-9fd9-4956-b7d8-7e44599ecd99.png)
1. Username을 입력합니다.
2. password를 입력합니다.
3. host을 입력합니다. 
  - aws의 경우 database주소를 입력합니다. 
  - local의 경우 localhost를 입력합니다.
4. database를 입력합니다.
5. connect를 눌러 접속을 합니다. state가 YES! 일경우 접속이 된 것이고, NO일 경우 접속이 안된 것입니다.


### 테이블 제작
![image](https://user-images.githubusercontent.com/110883172/205497758-64f7ef3b-2205-4e19-97ab-eb7fc443ffbd.png)
- csv나 xlsx파일을 준비합니다.
- table제작 버튼을 클릭합니다.

![image](https://user-images.githubusercontent.com/110883172/205497787-6fdf16bb-ebc8-4194-9ea1-1d5fdefd9d05.png)
- 원하는 csv나 xlsx파일을 선택합니다.

![image](https://user-images.githubusercontent.com/110883172/205497828-25d29aed-dd60-4154-a0a2-fbff87a3dc25.png)
- 테이블의 이름을 입력합니다.

![image](https://user-images.githubusercontent.com/110883172/205497845-1c90177e-0c7e-483b-995d-ebd762a146f1.png)
- 다음의 mysql syntax가 실행됩니다.
- 제작버튼을 누르면 테이블이 만들어집니다.

![image](https://user-images.githubusercontent.com/110883172/205497887-b190d1b5-ee38-442b-8201-6fa273dbd4d0.png)
- 테이블이 성공적으로 만들어졌습니다.


