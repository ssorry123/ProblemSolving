SELECT N,
    (CASE
     -- 부모가 NULL이면 루트
     WHEN P IS NULL THEN 'Root' 
     -- 루트가 아니고, 누군가의 부모면 중간 노드
     WHEN N IN (SELECT P FROM BST WHERE P IS NOT NULL) THEN 'Inner'
     ELSE 'Leaf'
    END)
FROM BST
ORDER BY N;