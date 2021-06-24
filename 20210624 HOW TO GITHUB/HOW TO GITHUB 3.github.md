# **원격 저장소 (remote repository)**

## **기본 설정**

1. 로컬 git 저장소 준비

2. Github repository 생성

   ![image-20210623170259834](HOW%20TO%20GITHUB%203.github.assets/image-20210623170259834.png)

3. Repository default branch 변경 (settings -> repositories)

   - main -> master로 변경

   ![tempsnip](HOW%20TO%20GITHUB%203.github.assets/tempsnip.png)

## **명령어**

### **원격 저장소 주소 추가**

```
$ git remote add origin 저장소URL
```

> "git아, 원격 저장소(remote) 추가해줘(add) origin 이라는 이름으로 저장소  URL을!!!"

- origin은 원격 저장소 이름!

### **원격 저장소 목록 보기**

```
$ git remote -v
origin  <https://github.com/woongedu/TIL.git> (fetch)
origin  <https://github.com/woongedu/TIL.git> (push)
```

> 잘못 add 한 경우 삭제하기$ git remote rm origin

### **원격 저장소에 업로드 (push)**

```
$ git push -u origin master

Enumerating objects: 8, done.
Counting objects: 100% (8/8), done.
Delta compression using up to 12 threads
Compressing objects: 100% (4/4), done.
Writing objects: 100% (8/8), 645 bytes | 645.00 KiB/s, done.
Total 8 (delta 0), reused 0 (delta 0), pack-reused 0
To <https://github.com/woongedu/TIL.git>
 * [new branch]      master -> master
Branch 'master' set up to track remote branch 'master' from 'origin'.
```

> "git아, push 해줘 origin이라는 이름의 원격저장소에 master 브랜치로!!!!"

> 원격 저장소에는 commit이 올라간다 !!!즉, commit 이력이 없다면 push 할 수 없다.

- 두번째 push 부터는 `u` 생략 가능

### **pull**

- 원격 저장소의 변경사항을 받아옴 (업데이트)

```
$ git pull origin master
```

### **clone**

- 원격 저장소 전체를 복제

```
$ git clone 저장소URL
```

> [주의사항]clone 받은 프로젝트는 이미 git init이 되어있음 (remote 도 추가되어 있음)