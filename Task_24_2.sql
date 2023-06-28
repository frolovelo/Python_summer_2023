--view sql
create view frol as select name_author, sum(amount)
as Количество from author inner join book using(author_id)
group by name_author
having sum(amount) = (select min(sum_amount) from (select sum(amount) as sum_amount
from book group by author_id) as query_min);

select * from frol;

drop view frol;