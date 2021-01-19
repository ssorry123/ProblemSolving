global g_cache1
g_cache1 = list()

# 모든 도시 이름은 소문자로 저장
# LFU : 가장 오랫동안 사용되지 않은 것 교환
def solution(cacheSize, cities):
    answer = 0  # 총 실행 시간

    # 캐시가 없는 경우
    if cacheSize == 0:
        return 5*len(cities)

    for ct in cities:
        ct = ct.lower() # 소문자로 통일
        # 캐시 히트 
        if ct in g_cache1:
            answer += 1
            # 히트된 캐시 빼서 맨 뒤로
            g_cache1.append(g_cache1.pop(g_cache1.index(ct)))
        # 캐시 미스
        else:
            answer += 5
            # 캐시가 꽉 찬 경우 가장 앞에 있는 캐시를 뺀다
            if len(g_cache1) == cacheSize:
                del g_cache1[0]
            # 캐시를 추가한다
            g_cache1.append(ct)

    return answer

print(solution(3,["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"] ))