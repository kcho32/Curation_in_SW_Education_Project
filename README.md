## 멀티캠퍼스 융복합 프로젝트형 클라우드(MSA) 서비스 개발 과정 PROJECT #1

### 요약
- Django를 이용한 MTV 패턴 기반의 웹사이트 구축

![main](https://user-images.githubusercontent.com/52156247/129450255-12cf04b5-6e02-4e89-9434-7f9b72710876.png)

- [시연 영상](https://youtu.be/UiiuZNOMpVA)

- [PDF](https://drive.google.com/file/d/1MT9G0pTpsDtuoIORccpu5iGNpnIjz-94/view?usp=sharing)

--- 

### 프로젝트 기간
2021/07/29 ~ 2021/08/13

### 팀원
- 김건우(팀장) - 강의 페이지 구현, 크롤링 및 디자인 적용
- 김명찬 - 질의답변 게시판 및 추천 기능 구현
- 성재윤 - 내정보 페이지, 강의 수강 및 위시리스트 기능 구현
- 장윤진 - 반응형 웹 디자인 및 서비스 컨셉 기획 총괄
- 조규원 - 회원 관련, 지도 api 및 검색어 기능 구현

--- 

### 사용한 기술
- FrontEnd
  - HTML / CSS  
  - JavaScript
  - Bootstrap4

- BackEnd
  - Python
  - Django
  - Selenium
  - BeautifulSoup
  - Pandas
  - SQLite3
  
- 협업
  - Git
  
- 배포
  - (추가)
--- 


### 기능 구현
- 회원가입 & 로그인 페이지
  - 아이디 & 이메일 중복 체크 기능 
  - 아이디 & 비밀번호 찾기 
- 메인 페이지
  - 카카오 지도 api
- 강의 목록 페이지
  - 검색 기능을 통해 원하는 강의 목록 필터링 기능 
  - slug 기능을 이용한 카테고리 기능 
  - 강의별 고유의 경로를 가진 상세 페이지
  - selenium을 이용해 Udacity의 강의 크롤링
  - 권한에 따른 CRUD
- 질의답변 게시판
  - 권한에 따른 CRUD
  - 추천 기능
- 내정보 페이지 
  - 내정보 수정
  - 수강 목록 & 위시리스트 
  - 작성 글 & 작성 댓글
  - 회원탈퇴 기능

---

### Django MTV 와 ERD

- Django MTV 패턴
![프로젝트구조_UNEDUCATEDSYSTEM](https://user-images.githubusercontent.com/52156247/129448241-dbbaf45b-abf8-4b62-bdd3-2be12658b52c.png)

- ERD
![Model설계](https://user-images.githubusercontent.com/52156247/129477210-f4ff2df2-bfeb-4ddc-8de4-7fda2abeb683.png)

### 

---

### 프로젝트 실행 방법
- git clone 

- 가상환경 설정 

- django, pillow 라이브러리 설치
- python manage.py makemigrations common
- python manage.py makemigrations
- python manage.py migrate

- 데이터 추가 
    - pandas 라이브러리 설치
    - python data.py 명령어 실행
    - 사진, 카테고리는 임의로 수정 필요
  
- 서버 실행
    
--- 

#### README.md
작성 : 김건우
