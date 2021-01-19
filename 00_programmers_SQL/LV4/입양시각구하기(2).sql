-- 코드를 입력하세요
SET @hour := -1;    -- 로컬 변수

SELECT (@hour := @hour + 1) AS HOUR,    -- hour+1을 hour에 대입
        (
            SELECT COUNT(*)
            FROM ANIMAL_OUTS
            WHERE HOUR(DATETIME) = @hour
        ) AS COUNT  -- hour를 시간으로 가지는 그룹의 수를 센다
FROM ANIMAL_OUTS
WHERE @hour < 23    -- hour가 23일때 종료