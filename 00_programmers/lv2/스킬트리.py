def check(skill, skill_tree):
    at = [-1] * len(skill)
    # skill[i]가 skill_tree의 몇번째에 위치한지 기록
    for i in range(len(skill)):
        c = skill[i]
        for j in range(len(skill_tree)):
            if c == skill_tree[j]:
                at[i] = j

    # -1뒤에는 모두 -1이어야함
    for i in range(len(at)):
        if at[i]==-1:
            for j in range(i+1, len(at)):
                if at[j]!=-1:
                    return 0
    
    # 위 조건을 통과했다면, 증가수열인지만 검사
    for i in range(len(at)-1):
        if at[i+1]==-1:
            return 1
        if at[i] > at[i+1]:
            return 0
    # 증가수열이면 1 리턴
    return 1

def solution(skill, skill_trees):
    answer = 0

    for skill_tree in skill_trees:
        answer += check(skill, skill_tree)
        # print(answer)

    return answer