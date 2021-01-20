select hac.hacker_id, hac.name
from submissions sub
    join hackers hac on (sub.hacker_id = hac.hacker_id)
    join challenges cha on (sub.challenge_id = cha.challenge_id)
    join difficulty dif on (cha.difficulty_level = dif.difficulty_level)
where sub.score = dif.score
group by hac.hacker_id, hac.name
having count(hac.hacker_id) > 1 -- 두문제 이상 모두 맞춘 사람
order by count(hac.hacker_id) desc, hac.hacker_id
;