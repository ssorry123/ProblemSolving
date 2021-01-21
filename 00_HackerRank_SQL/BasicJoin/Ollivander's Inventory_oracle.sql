select main.id, main.age, main.coins_needed, main.power
from
    (select power, age, min(coins_needed) as min_coins
    from wands join wands_property using (code)
    where is_evil = 0
    group by power, age) sub
    join
    (select *
    from wands join wands_property using (code)
    where is_evil = 0) main on (sub.min_coins = main.coins_needed
                                and sub.power = main.power
                                and sub.age = main.age)
order by main.power desc, main.age desc
;