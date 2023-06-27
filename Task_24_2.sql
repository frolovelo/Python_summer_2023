--view sql
create view frol as select distinct author from book
where amount = (select min(amount) from book);
select * from frol;
drop view frol;