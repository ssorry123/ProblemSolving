-- exclude duplicates
-- 중복을 제외하다.
SELECT DISTINCT CITY
FROM STATION
WHERE MOD(ID, 2) = 0;