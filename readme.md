# csv, xlsx 파일을 읽어와 mysql을 이용하여 자동으로 테이블을 만들고 데이터를 저장하는 코드입니다.

## 사용팁
- 사용하기전 pandas로 데이터를 가공하시길 바랍니다.  

- 현재 코드는 local로 되어있습니다. AWS의 접속을 원한다면 다음의 동작을 따라합니다.
![화면 캡처 2022-11-08 005408](https://user-images.githubusercontent.com/110883172/200355037-7e1e8ea5-7e6e-464c-a018-19310b5f9fa2.png)
  - 빨간색 밑줄친 부분을 AWS의 주소로 수정합니다.

- aws 데이터베이스 유저이름과 비밀번호를 입력하여 접속합니다.
  - 과금이 걱정된다면 localhost의 root으로 접속하면 됩니다.

- 연결이 완료되면 다음과 같은 작업을 수행할 수 있습니다.
  - 테이블 생성
  - 데이터 삽입
  - 테이블 삭제
  - 조회
  
## 사용법
- 우선 터미널을 이용해 데이터베이스를 생성해야합니다.

- 그 후 코드를 VS코드로 실행시켜 username, 비밀번호, 데이터베이스를 입력합니다.
![화면 캡처 2022-11-09 004054](https://user-images.githubusercontent.com/110883172/200609555-9bcf8349-18c5-45d1-9141-f2f39684152d.png)


### 1. 테이블을 제작하는 방법
![화면 캡처 2022-11-09 004958](https://user-images.githubusercontent.com/110883172/200611679-5f73a9e9-8b0f-446c-bb5c-e111fe8ecf3e.png)

- 메인메뉴에서 1을 입력합니다.
- csv나 xlxs를 참고할지 아니면 참고하지 않고 제작할지 결정합니다.

#### 1.1  csv나 xlxs를 참고하지 않고 제작하는 경우
![화면 캡처 2022-11-09 005215](https://user-images.githubusercontent.com/110883172/200612897-e2ecbee1-997a-48dd-b575-5fb6708276f6.png)

- 2번을 입력합니다. 
- 테이블의 이름을 입력합니다.
- 컬럼의 개수를 입력합니다.
- 각 컬럼의 타입을 입력하고 각 컬럼 이름을 입력합니다.
- 모두 입력되면 입력될 명령어를 보여줍니다. 1을 입력하는 경우 테이블이 제작되며, SQL 명령어에 오류가 발생하는 경우 테이블 제작에 실패합니다.

#### 1.2 csv나 xlxs를 참고하여 제작하는 경우
![image](https://user-images.githubusercontent.com/110883172/200616680-8ba55ef4-96a4-477b-969e-d4d85c9ef123.png)
- 엑셀을 사용할 경우 필수적으로 pip install openpyxl 을 하여야한다.
- 파일명을 입력합니다.
- 위의 그림은 따라만들지 않을 경우를 보여줍니다.
  - 따라만들지 않는 경우 데이터 이름은 유지되나 데이터 타입은 직접 타이핑 해주어야합니다.
  - 변수타입을 모두 입력해주면 테이블을 만드는 명령어가 생성됩니다.
  
 
![화면 캡처 2022-11-09 005215](https://user-images.githubusercontent.com/110883172/200617259-4b0a0734-d766-4382-96d3-88d4fd1fd93a.png)


- 따라만드는 경우

![화면 캡처 2022-11-09 005215](https://user-images.githubusercontent.com/110883172/200617612-63b5eef0-308c-45cb-b3ad-4847494684b4.png)

  - int, varchar(100), float 타입 중에서 컬럼과 맞는 타입을 지정하여 자동으로 테이블 명령어를 생성합니다.
  
  - 그렇기 때문에 날짜형(date)를 지정할 수 없습니다. 이는 sql에 올린 후 type을 직접 변환해주셔야 합니다.
  
  - 만약 파일의 문자열의 길이가 너무 길다면, 153번줄을 수정하십쇼.

### 2. 데이터를 삽입하는 방법
- 손수 타이핑하는 기능은 지원하지 않습니다. 요청시 만들 순 있으나, 터미널에서 입력하는 것이 더 빠릅니다.

![화면 캡처 2022-11-09 005215](https://user-images.githubusercontent.com/110883172/200619555-60acf77a-3ce6-4fcc-af5a-482a9da6b8e5.png)
- 메인 메뉴에서 2번을 입력하고
- 테이블을 선택하면 desc table 명령어로 컬럼의 타입들 확인할 수 있습니다.

![화면 캡처 2022-11-09 005215](https://user-images.githubusercontent.com/110883172/200620087-09914225-c8cb-4c67-b75d-bb9e996ef20f.png)
- 테이블을 만들 때 활요했던 csv 파일을 입력하세요.
- 입력하는 순간 데이터 삽입이 진행됩니다.
- 프로젝트에서 다루는 데이터는 기본 10만개 이상이기 때문에 1000개마다 진행상황을 출력하도록 만들었습니다.
- 삽입 중 종료되면 테이블에는 데이터가 삽입된 채로 남아있습니다. 주의 하시길 바랍니다.

#### 3. 테이블 삭제

![화면 캡처 2022-11-09 005215](https://user-images.githubusercontent.com/110883172/200621156-3a1ead4b-7d9b-4368-b7cb-4515606a321b.png)
- 메인메뉴에서 3을 입력하고
- 테이블 명을 입력하고 1을 입력하면 삭제됩니다.

#### 4. 테이블 조회
![화면 캡처 2022-11-09 012934](https://user-images.githubusercontent.com/110883172/200621345-5187b93a-1ea1-4c31-98a6-e614fff5f28a.png)
- 메인메뉴에서 4를 입력하면됩니다.

  
  
## 불편사항 발생시 슬랙으로 연락

- ver_0.2: csv파일만 받아올 수 있었던 기존과 달리, excel파일에 대응할 수 있게 하였습니다.

- ver_0.3: 인코딩 : EUC-KR에 대응할 수 있도록 수정하였습니다.

- ver_0.4 : csv, excel을 참고하여 테이블을 제작할 수 있도록 수정하였습니다.

- ver_0.5 : try_except으로 프로그램이 최대한 종료되지 않도록 조치하였습니다.

- ver_0.6 : 테이블 자동완성 기능을 추가하였습니다. 만세~!

- ver_0.7 : 데이터가 날아갔다

- ver_0.8 : 뛰어쓰기가 있는 컬럼명을 받아올 수 있게 하였습니다.

- ver_0.9 : 엑셀파일을 제대로 받아올 수 있게 수정합니다.

- ver_1.0 : 배포를 시작합니다.


## 예시 파일을 같이 첨부합니다. (파일은 모두 행의 개수를 줄여놓았습니다.) 
#### 출처 
- python_books.xlsx -> pinkLab
- seoul_bus_stop.csv -> 서울 공공 데이터 정류장별 승하차 인원 통계
