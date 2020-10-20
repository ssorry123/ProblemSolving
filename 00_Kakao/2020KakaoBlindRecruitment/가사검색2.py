import sys
# 문자열 최대 길이 10000, 트라이 최대 깊이 약 10**4
# 재귀함수 깊이 제한 설정
sys.setrecursionlimit(10**5)

class Trie:
    def __init__(self):
        self.cnt = 0    # 자신보다 밑에 있는 단말노드의 개수
        self.child = dict()

    def add_s(self,s,i=-1):
        # 루트노드인경우
        if i==-1:
            if not s[0] in self.child:
                self.child[s[0]] = Trie()
            self.cnt += 1   # 자신을 거쳐 내려가는 경우
            return self.child[s[0]].add_s(s, 0)
        # 단말까지 내려온 경우
        if i == len(s)-1:
            return

        # 아래로 아래로 내려간다
        if not s[i+1] in self.child:
            self.child[s[i+1]] = Trie()
        self.cnt += 1   # 자신을 거쳐 내려가는 경우
        return self.child[s[i+1]].add_s(s, i+1)
    
    # n길이까지만 검색하고, 그 아래에 있는 단말노드의 개수 반환
    def find_s_n(self, s, n, i=-1):
        # 0길이까지만 검색하는 경우, 쿼리가 모두 ?인 경우이므로
        # 모든 단말노드의 개수(루트의 cnt)를 반환
        if n==0:
            return self.cnt
        # 루트 노드인 경우
        if i==-1:
            if not s[0] in self.child:
                return 0
            return self.child[s[0]].find_s_n(s, n, 0)

        # n개의 문자열을 찾았거나, 문자열의 끝까지 찾은 경우
        if i == n-1 or i == len(s)-1:
            return self.cnt
        # 아래로 아래로 내려간다
        if not s[i+1] in self.child:
            return 0
        return self.child[s[i+1]].find_s_n(s, n, i+1)

def solution(words, queries):
    answer = []
    # 단어 길이에 따라 트라이 구현
    by_len = dict()
    for w in words:
        key = len(w)
        if not key in by_len:
            by_len[key] = [Trie(), Trie()]  # normal, reverse
        by_len[key][0].add_s(w)
        by_len[key][1].add_s(w[::-1])
    
    # 메모이제이션용 변수
    cache = dict()

    for q in queries:
        # 메모이제이션
        if q in cache:
            answer.append(cache[q])
            continue
        # 쿼리의 길이에 맞는 단어가 없을 경우
        if not len(q) in by_len:
            answer.append(0)
            continue

        ''' 매치되는지 확인 '''
        # ?가 앞인지 뒤인지 확인
        front = True
        if q[-1] == '?':
            front = False
        # 쿼리의 길이 확인
        key = len(q)
        # ?의 개수 확인
        wildcard_cnt = q.count('?') # ?가 몇글자인지 확인   
    
        # 트라이 탐색, ?부분을 자르지 않는다
        ret = 0
        q_cut = len(q) - wildcard_cnt   # ?를 제외한 q의 길이
        if front:
            ret = by_len[key][1].find_s_n(q[::-1], q_cut)
        else:
            ret = by_len[key][0].find_s_n(q, q_cut)

        answer.append(ret)
        cache[q] = ret  # 메모이제이션

    return answer

print(
    solution(["frodo", "front", "frost", "frozen", "frame", "kakao"],["fro??", "????o", "fr???", "fro???", "pro?"])
)