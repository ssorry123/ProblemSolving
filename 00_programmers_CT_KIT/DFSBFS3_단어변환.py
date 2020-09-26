# target부터 bfs?
import queue

def diff_word(n, begin ,words):
    ret = list()

    for word in words:
        cnt = 0
        for i in range(len(begin)):
            if begin[i] != word[i]:
                cnt+=1
            if cnt > n:
                break
        if cnt==n:
            ret.append(word)
    
    return ret


def solution(begin, target, words):
    answer = 0

    if not target in words:
        return 0

    # bfs
    q = queue.Queue()
    q.put((begin, 0))
    cache = set()
    cache.add(begin)

    while not q.empty():
        me, level = q.get()
        if me == target:
            return level
        
        # 현재 단어와 1개 다른 언어들
        next_words = diff_word(1, me, words)
        for word in next_words:
            # 방문한 적이 없다면
            if not word in cache:
                q.put((word, level+1))
                cache.add(word)


    return 0

print(solution('hit', 'cog', ['hot', 'dot', 'dog', 'lot', 'log', 'cog']))

print(solution('hit', 'cog', ['hot', 'dot', 'dog', 'lot', 'log']))