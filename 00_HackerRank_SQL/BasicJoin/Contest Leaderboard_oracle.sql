select hacker_id, name, sum(sub.scores)
from (
    select hacker_id as id, max(score) as scores
    from submissions join hackers using (hacker_id)
    group by hacker_id, challenge_id
    ) sub
    join hackers on (sub.id = hackers.hacker_id)
group by hacker_id, name
having sum(sub.scores) > 0
order by sum(sub.scores) desc, hacker_id
;