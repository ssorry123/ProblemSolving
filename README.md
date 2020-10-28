###### *공개할 수 없는 문제는 올리지 않음*
###### *직접 작성한 코드만 업로드*
<br>

---
#### ※2020.07..~with python3 or C(C++)
<br>

##### ㅁ dd_baekjoon_cccccccccccc
###### BOJ, 단계별로 풀어보기 or 알고리즘 분류
###### (2015..~2019)
###### (boj 단계별로 풀어보기 with C, C#, Java)
###### (대부분 업로드 되지 않음. 해당 단계 풀이 시 업로드)
<br>

##### ㅁ programmers
###### 알고리즘 주관적 분류
<br>

##### ㅁ programmers_CT_KIT
###### 프로그래머스 코딩테스트 고득점 KIT
<br>

##### ㅁ programmers_SQL_KIT
###### 프로그래머스 SQL 고득점 KIT
<br>

##### ㅁ 프로그래머스월간코드챌린지시즌1
###### 프로그래머스월간코드챌린지시즌1
<br>

##### ㅁ small_cpp_info
###### C++의 편리한 기능을 사용하기 위한 정보들

<br>

*************************************************************************

* python3 시간 초과가 발생할 경우
```py
python3 대신 pypy3 으로 돌려보기(BOJ)

input() 대신 sys.stdin.readline().strip() 사용해보기
항상 readline()을 사용하자

//
파이썬으로는 풀 수 없는 문제도 있는 것 같다...
추가 시간이 주어지지 않는 경우.. 문제에 따라 언어를 잘 선택할 것
```
```py
queue의 priorityqueue 대신, heapq 사용하기
heapq가 더 빠른듯, heapq로 시간초과 해결

''' min priority q '''
import queue
pq = queue.PriorityQueue()  # init
pq.put(3)           # push
pq.get()            # pop
pq.put(pq.get())    # top
# sum
sum=0
while not pq.empty():
    sum += pq.get()

''' min heap q'''
import heapq
# init
hq = [ ... ]    # some list
heapq.heapify(hq)

heapq.heappush(hq, 3)   # push
heapq.heappop(hq)       # pop
hq[0]                   # top
# sum
sum=0
for c in hq:
    sum += c

```
<br>

* C++ 시간 초과가 발생할 경우
```cpp
출력시 cout << endl 을 사용한 경우(fflush) ->
cout << endl을 사용하지 말고 cout<<"\n" 을 사용하기
or printf사용하기

입력시 cin을 사용한 경우 ->
or scanf 사용하기 (이것만 바꿔서 통과된 경우 있음..)

또는 ->
ios_base::sync_with_stdio(false);
cin.tie(NULL);
cout.tie(NULL);

->
쓸데없이 함수의 반환 값이 있는 경우 void로 리턴하기
```
<br>

* C(C++) 매우 큰 배열 등 할당
```cpp
main() 또는 함수 내에 매우 큰 배열을 할당할 경우
지역변수(stack영역)로 할당되어 StackOverflow
->
전역or정적변수(data영역)로 할당
```
<br>

* Python3 재귀함수 깊이 제한 설정
```py
import sys
sys.setrecursionlimit(10**6)    # 깊이 제한 10^6 설정
```

