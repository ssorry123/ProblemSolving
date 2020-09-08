def make_combi(i, n, ret_list, start = 0, cnt = 0, tmp_list = []):
    '''0~n-1 까지의 수 중에서, i개를 사용하여 만들 수 있는 모든 조합(오름차순)
    참조형식인 ret_list에 담아서 반환'''
    if cnt == i:
        ret_list.append(tmp_list)
        return

    # 순서가 상관 없으므로, start부터 만든다
    for si in range(start, n):
        # 지금까지 만든 조합에서 숫자 하나를 추가하여 새로운 조합을 만듬
        new_list = tmp_list + [si]
        # i개를 사용할때까지 만든다
        make_combi(i, n, ret_list,si+1, cnt+1, new_list)

# superkey들을 비교하기 위해 문자열로
def cb_to_string(cb):
    '''list에 담긴 값들을 하나의 string으로 합친 후 반환'''
    ret = ''
    for i in cb:
        ret += str(i)
    return ret

def check_minimum(super_dict):
    ''' 최소성 검사 '''
    willDelSuperKey = []    # 삭제 예정인 슈퍼키

    # 여러 키들의 조합인 슈퍼키에서, 한 키를 뺐을 경우에도 유일성을 만족하는지 확인
    for superkey in super_dict:
        # 슈퍼키가 하나의 조합인 경우, 최소성도 만족함
        if len(superkey) == 1:
            continue
        # 두 키 이상의 조합으로 만든 슈퍼키에서, 한 키를 뺀 후, 슈퍼키에 속하는지 확인
        for i in range(len(superkey)):
            tmp_key = superkey[:i] + superkey[i+1:]
            # 한 키를 빼도 슈퍼키에 속하는 경우, 그 슈퍼키는 삭제한다
            if tmp_key in super_dict:
                willDelSuperKey.append(superkey)

    # 검사를 다 하고 한 번에 삭제
    for dk in willDelSuperKey:
        if dk in super_dict:
            super_dict.pop(dk)

    return
    
def solution(relation):
    answer = 0
    # 가능한 모든 속성들의 조합으로, 슈퍼키(유일성)를 만든다
    # 만들어진 슈퍼키들의 최소성을 검사한다

    col_cnt = len(relation[0])  # 속성의 개수
    super_dict = dict()         # 슈퍼키를 담을 dictionary

    # 1개 조합부터,  컬럼 수 조합까지, 작은 개수의 조합부터 후보키를 만들어 나감
    for i in range(1, col_cnt+1):
        combi = list()  # ex 2개 조합) combi = [[0, 1], [0, 2], [0, 3], [1, 2], [1, 3], [2, 3]]
        make_combi(i, col_cnt, combi)

        # i개로 만든 조합 combi를 모두 다 해보면서 후보키를 찾는다
        for cb in combi:    # ex) cb = [0,3] 0,3 속성 조합
            cb_str = cb_to_string(cb)   # 조합을 문자열로 변환

            check_dict = list() # 해당 키로 만들어진 튜플 저장
            for col in relation:
                key = ''
                for att_idx in cb:  
                    key += col[att_idx]
                # 만든 키로 유일성 파악
                if key in check_dict:
                    check_dict = list() # 초기화
                    break
                else:
                    check_dict.append(key)

            # check_dict가 비어있다면, 해당 조합은 슈퍼키 조합이 될 수 없음
            if len(check_dict) == 0:
                continue
            #check_dict가 비어있지 않다면, cb_str은 슈퍼키 조합임
            super_dict[cb_str] = 'spk'

    check_minimum(super_dict)   # 만들어진 슈퍼키들 최소성 검사
    answer = len(super_dict)    # 최소성 검사를 통과한 슈퍼키들의 개수(후보키들의 개수)
    return answer