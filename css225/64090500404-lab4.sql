use University;

select * from course;

-- 1_1
select title from course where dept_name = "Comp. Sci." and credits = 3;

-- 1_2
select distinct takes.id from takes join (teaches join instructor using (id)) using(course_id, sec_id, semester, year) where instructor.name = 'Einstein'; 

-- 1_3
select dept_name, max(salary) from instructor group by dept_name; 

-- 1_4
select id,name,salary from instructor where salary=(select max(salary) from instructor);

-- 1_5 
select course_id ,sec_id,count(id) from takes where(semester,year) in (select semester,year from takes where semester="Fall" and year = 2009 ) group by course_id ,sec_id;

-- 1_6 
with max_enrollment(course_id, sec_id, enrollment) as (select course_id, sec_id, count(id) from takes where semester = 'Fall' and year = 2009 group by course_id, sec_id)
select max(enrollment) from max_enrollment;

-- 1_7
with max_enrollment(course_id, sec_id, enrollment) as (select course_id, sec_id, count(id) from takes where semester = 'Fall' and year = 2009 group by course_id, sec_id)
select course_id, sec_id, enrollment from max_enrollment where enrollment = (select max(enrollment) from max_enrollment);



