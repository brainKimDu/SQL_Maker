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

### 테이블에 데이터 삽입
![image](https://user-images.githubusercontent.com/110883172/205498197-5366fa00-5411-49df-8999-a9e6e76c3f9a.png)
- 데이터 삽입 버튼을 클릭합니다.

![image](https://user-images.githubusercontent.com/110883172/205498217-aea46f60-bc51-4eaa-996f-21570a6c8df2.png)
- 데이터를 삽입할 테이블을 선택합니다.

![image](https://user-images.githubusercontent.com/110883172/205498230-8e1c70b0-db68-4d26-b933-42264eef2dca.png)
- 데이터파일을 선택합니다. 컬럼수와 타입이 일치해야합니다. (같은파일이여야 합니다)

![image](https://user-images.githubusercontent.com/110883172/205498254-95e7cd9a-4781-4ece-96e5-78a8e84652be.png)
- progress바가 100%가 될 때까지 기다리세요.

![image](https://user-images.githubusercontent.com/110883172/205498277-b1fd226c-4ecd-492a-94b3-ca6ec25fd096.png)
- 데이터 삽입이 완료되었습니다.


### 테이블 삭제
![image](https://user-images.githubusercontent.com/110883172/205498318-3431383f-454f-4d05-863d-244d415cb369.png)
- table 삭제 버튼을 클릭합니다.

![image](https://user-images.githubusercontent.com/110883172/205498327-f5882768-9a55-4055-a33e-92c766b87c53.png)
- 테이블을 선택하고 OK를 누릅니다.

![image](https://user-images.githubusercontent.com/110883172/205498347-6a53753e-daf1-43c9-9e87-0e993159e879.png)
- 성공적으로 테이블이 삭제되었습니다.


### 테이블 선택
![image](https://user-images.githubusercontent.com/110883172/205498408-5c54179d-c312-40a8-bb04-84ef318696f8.png)
- 테이블 선택 버튼을 클릭합니다.

![image](https://user-images.githubusercontent.com/110883172/205498423-c022272e-3da2-4a52-b29d-bd1ed314941a.png)
- 원하는 테이블을 선택합니다.



## advanced mode
![image](https://user-images.githubusercontent.com/110883172/205498444-5fdce9bb-007b-45c1-b0dd-d1baecd4a001.png)
- 테이블을 선택하고 advanced 버튼을 클릭합니다.


![image](https://user-images.githubusercontent.com/110883172/205498534-fc33b606-4ba1-415c-9fa4-cb0a6af07e6d.png)
- mySQL syntax를 입력하면됩니다.
- select와 from이 포함되는 문법이라면 조회가 가능합니다.
- 그러나 union과 join처럼 2개의 테이블이 필요한 경우는 아직 구현하지 못 했습니다.


- select 사용년월, 역명 from bus where 역명='원남동' 를 입력해보겠습니다.
![image](https://user-images.githubusercontent.com/110883172/205498570-8a03d3ee-d78d-4bea-8d65-f3b589bea049.png)
- 다음처럼 조회가 가능합니다.


## To csv..
![image](https://user-images.githubusercontent.com/110883172/205498570-8a03d3ee-d78d-4bea-8d65-f3b589bea049.png)
- 조회한 정보를 csv로 저장할 수 있습니다.
- To csv.. 버튼을 클릭합니다.

![image](https://user-images.githubusercontent.com/110883172/205498627-c33ab128-7f8e-4b8e-ad41-d8211514f7dc.png)
- 원남동으로 만들어보겠습니다.

![image](https://user-images.githubusercontent.com/110883172/205498656-e69bd9f8-2544-44eb-b559-5f76e40d2c8c.png)
- 성공적으로 csv파일로 만들어주었습니다.



# 앞으로 구현해야할 것
- Union, join을 구현할 예정입니다.
- 손쉬운 사용모드를 구현하여 mysql문법을 몰라도 데이터를 추출할 수 있게 만들려고 합니다.






