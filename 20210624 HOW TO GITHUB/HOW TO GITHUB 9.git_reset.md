# **reset vs revert**

## **reset**

> https://git-scm.com/docs/git-reset"시계를 마치 과거로 돌리는 듯한 행위"특정 커밋으로 되돌아가며 되돌아간 특정 커밋 이후의 커밋들은 모두 사라지며,파일 상태는 옵션을 통해 결정

- git reset 설명 이미지

**3가지 옵션**

1. ```
   -soft
   ```

   - 돌아가려는 커밋으로 되돌아가고,
   - 이후의 commit된 파일들을 `staging area`로 돌려놓음 (commit 하기 전 상태)
   - 즉, 다시 커밋할 수 있는 상태가 됨

2. ```
   -mixed
   ```

   - 돌아가려는 커밋으로 되돌아가고,
   - 이후의 commit된 파일들을 `working directory`로 돌려놓음 (add 하기 전 상태)
   - 즉, unstage 된 상태로 남아있음
   - 기본값

3. `-hard`

- 돌아가려는 커밋으로 되돌아가고,
  - 이후의 commit된 파일들(`tracked 파일들`)은 모두 working directory에서 삭제
- 단, Untracked 파일은 Untracked로 남음

```
# --hard 예시

$ git log --oneline
d56a232 (HEAD -> master) hello
7f6c24c foo & bar
006dc87 rename commit message
3551584 asdasd
71ccbf1 first

$ git reset --hard 3551584
HEAD is now at 3551584 asdasd

$ git log --oneline
3551584 (HEAD -> master) asdasd
71ccbf1 first

$ git status
On branch master
nothing to commit, working tree clean
```

- `reset`은 과거로 돌아가게 되면 돌아간 커밋 이후의 커밋은 모두 히스토리에서 사라짐
- 커밋 히스토리가 바뀌기 때문에 다른 사람과 공유하는 브랜치에서 사용 시 충돌이 발생
- 공유하는 브랜치에서 이전 커밋을 수정하고 싶을 때는 `git revert` 사용

# git reflog

git reflog를 활용하면 이때까지 HEAD가 가르켰던 커밋 아이디가 모두 나온다.

![Untitled](HOW%20TO%20GITHUB%209.git_reset.assets/Untitled.png)

이를 통해서 커밋 아이디를 찾고, `git reset --hard 커밋아이디` 를 활용하면 코드를 복구할 수 있다.

------

## **revert**

> https://git-scm.com/docs/git-revert"특정 사건을 없었던 일로 만드는 행위"이전 커밋 내역을 그대로 남겨둔 채 새로운 커밋을 생성커밋 히스토리 변경 없이 해당 커밋 내용만을 삭제한 상태의 새로운 커밋을 생성

```
$ git log --oneline
7f6c24c (HEAD -> master) foo & bar
006dc87 rename commit message
3551584 asdasd
71ccbf1 first

# revert commit 편집기 실행
$ git revert 71ccbf1
Removing foo.txt
Removing bar.txt
[master 3b55051] Revert "first"
 2 files changed, 0 insertions(+), 0 deletions(-)
 delete mode 100644 bar.txt
 delete mode 100644 foo.txt

$ git log --oneline
3b55051 (HEAD -> master) Revert "foo & bar"
7f6c24c foo & bar # 히스토리는 남아있음
006dc87 rename commit message
3551584 asdasd
71ccbf1 first
```

- 다른 사람과 공유하는 브랜치에서 이전 커밋을 수정하고 싶을 때 사용
- 커밋 히스토리가 바뀌지 않기 때문에 충돌이 발생하지 않음
- git reset을 쓰면 커밋이 과거로 돌아가기 때문에 remote 레포지토리에 push를 할 수 없음 따라서 git revert를 사용

