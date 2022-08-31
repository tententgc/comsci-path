use University ;
select * from advisor;
select name,title from student natural join takes,course where takes.course_id = course.course_id; 
select name,title from student natural join takes natural join course; 


select name,course_id from instructor,teaches where instructor.id = teaches.id;

select * from student natural join takes;