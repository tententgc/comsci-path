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


use University;
desc course;
# 2_1
insert into course(course_id, title, credits) values ("CS-001", 'Weekly Seminar', 0);
#error เพราะ credit เป็น 0 ไม่ได้

#2_2
insert into section(course_id,sec_id,semester,year) values ("CS-001", '1', 'Fall', 2017);
#error ไม่รหัสวิชา CS-001

#2-3
insert into takes(id, course_id, sec_id, semester, year) select student.id , "CS-001", '1', 'Fall', 2017 from student where dept_name = 'Comp. Sci.';

#2-4
delete from takes where (id in (select id from student where name = 'Chavez')) and (course_id = "CS-001") and (sec_id = '1') and (semester = 'Fall') and (year = 2017);

#2-5
delete from course where course_id = "CS-001";

#2-6
delete from takes where course_id = (select course_id  from course where (title like '%Database%' or title like 'Database%' or title like '%Database') and course_id != (select course_id  from course where title = 'Database'));


