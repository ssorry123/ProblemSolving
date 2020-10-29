-- 코드를 입력하세요
SELECT NAME, count(*)
FROM ANIMAL_INS
GROUP BY NAME
HAVING count(NAME)>=2   -- 동명이 두명 이상
ORDER BY NAME