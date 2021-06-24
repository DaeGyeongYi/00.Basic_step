# GITHUB 정리 - 1. CLI

### CLI?

Command Line Interface -> Command(명령어)를 활용하여 컴퓨터에게 작업을 지시하는 환경

- Command는 OS, 프로그램별로 조금씩 다름
- CLI의 핵심개념은 경로(Path)와 명령어(Command)

### 경로

- 파일이나 폴더의 고유한 위치를 나타내는 주소 (상대경로와 절대경로가 있다.)

  상대경로:  현재 내가 위치한 디렉토리(워킹 디렉토리)를 기준으로 하는 경로

  절대경로:  최상위 디렉토리부터 파일명에 이르는 경로

- OS별로 다르게 표현되기도 한다.

  windows - <span style="color:red">`C:\Users\Document`</span>

  mac - <span style="color:red">`/Users/Document`</span>

### 디렉토리(Directory)

- 폴더라고 생각하면 편함. 정확한 정의는 운영체제에서 배웠는데 기억이 안나요 미안!

#### 루트 디렉토리

- 모든 파일이나 폴더를 담고 있는 디렉토리
- windows 기준으로는 보통 C 드라이브



### 워킹 디렉토리(Working Directory)

- 현재 작업중인 디렉토리 = 현재 위치

- 상대 경로를 계산하는 기준이 됩니다.

- <span style="color:red">`pwd`</span> 명령어를 통해 현재 워킹 디렉토리를 확인할 수 있음

- 상대 경로에서 <span style="color:red">`.`</span> 은 워킹 디렉토리를 의미 

  ex)<span style="color:red">`git add  .`</span> 명령어를 통해 워킹 디렉토리 내의 파일들을 add하는 것처럼!

#### 부모/자식 디렉토리

- 디렉토리 안에 디렉토리가 있는 경우 상위 디렉토리를 부모 디렉토리, 하위 디렉토리를 자식 디렉토리라고 함
- 상대경로에서 <span style="color:red">`..`</span> 으로 부모 디렉토리를 나타낼 수 있다.

#### <span style="color:red">`~`</span>틸드(Tilde)

- 현재 사용자의 홈 디렉토리를 의미
- 현재 사용자란 컴퓨터를 켰을 때 로그인 하는 계정! 



## Command(명령어)

### cd

- Change Directory

- 현재 워킹 디렉토리를 변경할 때 사용한다.

- <span style="color:red">`cd..`</span> 명령어를 입력하면 부모 디렉토리로 이동할 수 있다.

- <span style="color:red">`C:\Users\User\바탕 화면`</span> -> <span style="color:red">`C:\Users\User`</span>

  

### date

```

Wed Jun 23 15:39:15     2021

```

- 컴퓨터 상의 현재 시각이 출력됨
- OS마다 시간을 기록하는 방법이 다르기 때문에 실제와 약간 차이



#### ls

- 워킹 디렉토리 내의 폴더/파일 확인하기

- <span style="color:red">`ls -al`</span> 명령어를 사용해서 숨김폴더와 자세한 정보를 알 수 있다.

  

#### touch

<span style="color:red">`touch a.txt`</span>  형식으로 폴더를 만들 수 있다.



#### mkdir

- `mkdir 디렉토리이름` 형식으로 폴더를 만들 수 있다.

- 만약 폴더 이름(happy hacking)에 공백이 있다면? `mkdir happy hacking` 이라고 명령어를 사용하면 `happy` 와 `hacking` 2개의 폴더가 생긴다. 이를 방지하기 위해서는 따옴표를 사용해서 폴더 이름을 묶어줘야 한다. `mkdir 'happy hacking'`

  

### **Command TIP**

- 과거 명령어 불러오기(위, 아래 방향키)
- 자동 완성(tab)
- `ctrl + a` 커서가 명령어 맨 앞으로 이동
- `ctrl + e` 커서가 명령어 맨 뒤로 이동
- `ctrl + w` 커서 앞에 단어 지워줌





