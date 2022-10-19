use University;
drop database  University;
/*1-1*/
select title from course where dept_name = "Comp. Sci." and credits = 3;
/*1-2*/
select distinct takes.id from takes join (teaches join instructor using(id)) using(course_id, sec_id, semester, year) where   instructor.name = 'Einstein'; 
/*1-3*/
select max(salary) from instructor; 
select  dept_name, max(salary) from instructor group by dept_name;
/*1-4*/
select id, name, salary from instructor where salary = (select max(salary) from instructor); 
/*1-5*/
select course_id, sec_id, count(id) from takes where semester = 'Fall' and year = 2009 group by course_id, sec_id;
/*1-6*/
with max_enrollment(course_id, sec_id, enrollment) as (select course_id, sec_id, count(id) from takes where semester = 'Fall' and year = 2009 group by course_id, sec_id)
select max(enrollment) from max_enrollment;
/*1-7*/
with max_enrollment(course_id, sec_id, enrollment) as (select course_id, sec_id, count(id) from takes where semester = 'Fall' and year = 2009 group by course_id, sec_id)
select course_id, sec_id, enrollment from max_enrollment where enrollment = (select max(enrollment) from max_enrollment);



desc course;
/*2-1*/
insert into course(course_id, title, credits) values ("CS-001", 'Weekly Seminar', 0);
/*error เพราะ  credit ต้องมากกว่า  0*/

/*2-2*/
insert into section(course_id,sec_id,semester,year) values ("CS-001", '1', 'Fall', 2017);
/*error เพราะว่า โครงสร้างของ section มี  course_id ที่่อ้างอิงจากตาราง  course ซึ่งตอนนี้ไม่มี course ที่ชื่อว่า  CS-001*/ 

/*2-3*/
insert into takes(id, course_id, sec_id, semester, year) select student.id , "CS-001", '1', 'Fall', 2017 from student where dept_name = 'Comp. Sci.';
/*error เพราะว่า โครงสร้างของ takes มี  course_id และ sec_id ที่่อ้างอิงจากตาราง  section ซึ่งตอนนี้ไม่มี course ที่ชื่อว่า  CS-001*/ 

/*2-4*/
delete from takes where (id in (select id from student where name = 'Chavez')) and (course_id = "CS-001") and (sec_id = '1') and (semester = 'Fall') and (year = 2017);
/*ไม่ error เพราะไม่มีข้อมูลในตาราง  */

/*2-5*/
delete from course where course_id = "CS-001";
/*ไม่ error ข้อมูลใน  section และ  takes จะหายไป เพาระ โครงสร้างข้อมูลของ section และ takes กำหนด on dalate cascade ทำให้การที่ลบตารางแม่หรือเปลี่ยนแปลงข้อมูล จะลบตารางลูกด้วย */

/*2-6*/
delete from takes where course_id = (select course_id  from course where (title like '%Database%' or title like 'Database%' or title like '%Database') and course_id != (select course_id  from course where title = 'Database'));




insert into course(course_id, title, credits) values ("CS-002", 'Database', 1);
select * from course;
delete from course where course_id = "CS-002";
insert into section(course_id,sec_id,semester,year) values ("CS-002", '1', 'Fall', 2017);
select * from section;
delete from section where course_id = "CS-002";

select id  from student where dept_name = 'Comp. Sci.';
insert into takes(id, course_id, sec_id, semester, year) select student.id , "CS-002", '1', 'Fall', 2017 from student where dept_name = 'Comp. Sci.';

select * from takes;
select * from takes where course_id = (select course_id  from course where title = 'Database');
delete from takes where course_id = "CS-002";

delete from takes where id = (select id from student where name = 'Zhang');

delete from takes where (id in (select id from student where name = 'Chavez')) and (course_id = "CS-002") and (sec_id = '1') and (semester = 'Fall') and (year = 2017);

delete from course where course_id = "CS-002";
