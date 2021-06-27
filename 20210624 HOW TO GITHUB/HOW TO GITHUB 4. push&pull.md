집 ↔ 강의장 (clone & pull ↔ push) 시나리오

- 준비

  - 폴더로 공간 분리

    ```
    # 강의장 컴퓨터라고 가정하는 임의의 폴더
    강의장/
    
    # 집 컴퓨터라고 가정하는 임의의 폴더
    집/
    ```

  - GitHub에서 연습용 레포지토리를 생성한다.

    ```
    TIL-test
    ```

- 강의장 (init, commit, push)

  - `TIL-test`

  - 강의장에서 수업 내용을 정리하고 원격 저장소에 푸쉬!

    - TIL-test 폴더 생성하기

      ```
      강의장/
          TIL-test/
      ```

    - `git init` + 개발 진행

      ```
      # 강의장/TIL-Test/
      
      $ git init
      $ touch a.txt
      ```

      ```
      강의장/
          TIL-test/
              a.txt
      ```

    - `git add + git commit + git push`

      ```
      # 강의장/TIL-Test/
      
      $ git add .
      $ git commit -m "a.txt 파일 추가"
      $ git remote add origin {url}
      $ git push origin main
      ```

    - Github 접속해서 원격 저장소에 업로드 되었는지 확인

- 집 (clone, commit, push)

  - 집으로 가서 강의장에서 올려둔 내용 clone!

    - 처음이기에 clone!

    - 다음부터는 pull!

    - `git clone`

      Github 레포지토리로 가서 `Clone or Download` 메뉴를 눌러서 URL 주소 복사-붙여넣기

      .을 붙여서 한다.

      ```
      # 집/
      
      $ git clone {url} .
      ```

      ```
      집/
      TIL-test/
      a.txt
      ```

  - 집에서 새로운 내용을 추가하고 원격 저장소에 업로드하기

    - `git push`

      ```
      # 집/TIL-Test
      
      $ touch b.txt
      ```

      ```
      집/
      TIL-test/
      a.txt
      b.txt
      ```

      ```
      # 집/TIL-Test
      
      $ git add .
      $ git commit -m "b.txt 파일 추가"
      $ git push origin master
      ```

  - 다음날 강의장으로 가서 집에서 작업한 내용을 가져오기

    - `git pull`

      ```
      강의장/
          TIL-test/
              a.txt
      ```

      ```
      # 강의장/TIL-Test
      
      $ git pull origin main
      ```

      ```
      강의장/
          TIL-test/
              a.txt
              b.txt
      ```

- 강의장 (pull, commit, push)

- 집 (pull, commit, push)

- (반복!)

## **push가 안돼요!**

1. GitHub 사이트에서 직접 작성한 커밋이 있는 경우

   → GitHub 사이트 통해서 파일을 수정하는 것도 commit으로 기록된다!

2. 집에서 push한 commit이 있는데, 강의장 와서 pull 안하고 commit한 경우

   → 두 상황 모두, 하나의 브랜치에 부모가 같은 서로 다른 commit이 존재해서

   → `A - B` & `A - C`

   → (상황 만들어서 보여주기)

   → pull을 하면 된다!

   2-1. B와 C에서 서로 다른 파일을 수정한 경우

   → pull 해서 `A - B - C - A'(Merge)` 이런 식으로 만들어주면 된다.

   2-2. 같은 파일을 수정한 경우

   → 일이 복잡해짐 → Merge Conflict를 수정해야 한다.

   