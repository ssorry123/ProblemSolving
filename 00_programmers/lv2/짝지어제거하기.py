def solution(s):

    st = list()

    for i in range(len(s)):
        c = s[i]

        # 스택이 비어있거나, top이 다르다면
        if len(st)==0 or st[-1] != c:
            st.append(c)

        # 스택이 비어있지 않고, top이 같다면
        # 짝지어 제거한다
        elif st[-1] == c:
            del st[-1]
        

    if len(st)==0:
        return 1
    return 0

solution('cdcd')