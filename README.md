###### *공개할 수 없는 문제는 올리지 않음*
###### *직접 작성한 코드만 업로드*
<br>

---
#### ※2020.07..~with python3 or C(C++)
<br>

##### ㅁ dd_baekjoon_cccccccccccc
###### BOJ, 단계별로 풀어보기
###### (2015..~2019)
###### (boj 단계별로 풀어보기 with C, C#, Java)
###### (대부분 업로드 되지 않음. 해당 단계 풀이 시 업로드)

##### ㅁ programmers_CT_KIT
###### 프로그래머스 코딩테스트 고득점 KIT

##### ㅁ programmers_SQL_KIT
###### 프로그래머스 SQL 고득점 KIT

##### ㅁ 프로그래머스월간코드챌린지시즌1
###### 프로그래머스월간코드챌린지시즌1

##### ㅁ small_cpp_info
###### C++의 편리한 기능을 사용하기 위한 정보들

<br>

*************************************************************************

* BOJ python3 시간 초과가 발생할 경우
```
python3 대신 pypy3 으로 돌려보기

input() 대신 readline() 사용해보기

//
파이썬으로는 풀 수 없는 문제도 있는 것 같다...
추가 시간이 주어지지 않는 경우.. 문제에 따라 언어를 잘 선택할 것
```

* BOJ C++ 시간 초과가 발생할 경우
```
출력시 endl 을 사용한 경우(fflush)
endl을 사용하지 말고 \n 을 사용하기

입력시 cin을 사용한 경우
scanf 사용하기 (이것만 바꿔서 통과된 경우 있음..)

쓸데없이 함수의 반환 값이 있는 경우 void로 리턴하기
```

* C(C++) 매우 큰 배열 등 할당
```
main() 또는 함수 내에 매우 큰 배열을 할당할 경우
지역변수(stack영역)로 할당되어 StackOverflow

전역or정적변수(data영역)로 할당
```

* Python3 재귀함수 깊이 제한 설정
```py
import sys
sys.setrecursionlimit(10**6)    # 깊이 제한 10^6 설정
```

