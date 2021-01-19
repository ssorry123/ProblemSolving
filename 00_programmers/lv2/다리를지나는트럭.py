def solution(bridge_length, weight, truck_weights):
    answer = 0

    time = 0
    idx = 0
    truckCnt = len(truck_weights)   # 대기중인 트럭의 개수
    on_bridge = list()  # (weight, time)
    sum_on_bridge = 0
    while idx < truckCnt or len(on_bridge)!=0:
        # 트럭이 다리를 빠져나올 시각이라면 빼준다
        while len(on_bridge) !=0 and on_bridge[0][1] == time:
            sum_on_bridge -= on_bridge[0][0]
            del on_bridge[0]

        # 다리에 올라갈 수 있다면, 트럭을 올린다
        if idx < truckCnt and sum_on_bridge + truck_weights[idx] <= weight:
            on_bridge.append((truck_weights[idx], time + bridge_length))    # 다리 위 트럭 기록
            sum_on_bridge += truck_weights[idx] # 다리의 총 무게 기록
            idx+=1  # 다음 트럭으로 이동

        time += 1

    print(time)
    answer = time
    return answer


solution(2, 10, [7,4,5,6])