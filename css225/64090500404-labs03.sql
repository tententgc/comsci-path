use University ;

select * from student natural left join takes;

select * from student natural right join takes;

select distinct I.ID, I.NAME, (Select count(*) from teaches as T where I.ID = T.ID) as "number of sections" from instructor as I;

select name, course_id, sec_id from instructor AS I, teaches as T where semester = "Spring" AND year = 2010 and I.ID = T.ID;

select distinct dept_name, count(dept_name) as "number of instructor" from instructor as I group by I.dept_name;
