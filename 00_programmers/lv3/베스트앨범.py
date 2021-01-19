def solution(genres, plays):
    answer = []
    music = dict()  # key = 장르, value = (노래고유번호, 재생횟수)
    genre_rank = dict() # key = 장르, value = 장르에 속한 음악들의 총 재생 횟수
    
    for i in range(len(plays)):
        genre, play_time = genres[i], plays[i]
        if not genre in music:
            music[genre] = list()
        if not genre in genre_rank:
            genre_rank[genre] = 0
        
        genre_rank[genre] += play_time      # 장르에 속한 노래의 재생 횟수 더함
        music[genre].append((i, play_time)) # 노래의 고유 번호와 재생 횟수 저장

    
    genre_rank = genre_rank.items() # 리스트 변환
    genre_rank = sorted(genre_rank, key = lambda x:-x[1]) # 재생 횟수가 많은 장르순으로 정렬

    for genre, total_time in genre_rank:
        # 노래의 재생횟수많은 우선, 노래의 고유번호 작은 우선
        tmp = sorted(music[genre], key = lambda x : (-x[1], x[0]))
        for i in range(len(tmp)):
            answer.append(tmp[i][0])
            if i==1:
                break

    
    return answer

print(solution(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500]))