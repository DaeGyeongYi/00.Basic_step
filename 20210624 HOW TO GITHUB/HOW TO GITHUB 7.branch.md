# **branch command**

- 브랜치 생성

  ```
  $ git branch 브랜치명
  ```

- 브랜치 목록

  ```
  $ git branch
  ```

- 브랜치 이동

  ```
  $ git checkout 브랜치명
  (브랜치명) $
  ```

- 브랜치 생성 + 이동

  ```
  $ git checkout -b 브랜치명
  ```

- 브랜치 병합

  ```
  (master) $ git merge 브랜치명
  ```

  > 반드시 master 브랜치에 브랜치 를 병합

- 브랜치 삭제

  ```
  $ git branch -d 브랜치명
  ```

- 브랜치 강제 삭제

  ```
  $ git branch -D 브랜치명
  ```

  > merge가 되지 않은 브랜치는 강제로 삭제해야 함