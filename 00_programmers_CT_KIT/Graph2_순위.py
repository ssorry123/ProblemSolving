# 위상정렬 모양 그래프

Tree = dict()
class Node:
    def __init__(self, me):
        self.win = list()
        self.lose = list()

        global Tree
        Tree[me] = self


visited = set()
g_win = 0
g_lose = 0
def dfs_win(me):
    ''' 자신이 이길 수 있는 사람만 카운팅 한다 ''' 
    if len(Tree[me].win)==0:
        return
    
    global visited, g_win, g_lose
    for there in Tree[me].win:
        if not there in visited:
            g_win += 1
            visited.add(there) 
            dfs_win(there)
    return

def dfs_lose(me):
    ''' 자신이 질 수 있는 사람만 카운팅 한다'''
    if len(Tree[me].lose)==0:
        return
    
    global visited, g_win, g_lose
    for there in Tree[me].lose:
        if not there in visited:
            g_lose += 1
            visited.add(there)
            dfs_lose(there)
    return

def check(me, n):
    global visited, g_win, g_lose
    visited = set()
    g_win = g_lose = 0

    # 두 함수 합쳐서 O(n)
    dfs_lose(me)    # 자신이 지는 사람
    dfs_win(me)     # 자신이 이기는 사람

    if g_lose + g_win + 1 == n:
        return True
    else:
        return False


def solution(n, results):
    answer = 0

    # 그래프 만들기
    global Tree
    for a, b in results:
        if not a in Tree:
            Node(a)
        if not b in Tree:
            Node(b)

        Tree[a].win.append(b)
        Tree[b].lose.append(a)

    # 모든 사람 검사 하기
    # check함수 O(n), for문 O(n)
    # O(n^2), n은 100이하
    for person in Tree:
        if check(person, n):
            answer+=1
    
    print(answer)
    return answer

solution(5, [[4,3],[4,2],[3,2],[1,2],[2,5]])