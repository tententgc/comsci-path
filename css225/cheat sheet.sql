use sakila;
#1 .แสดงชื่อ นามสกุลของนักแสดงทุกคนที่มีชื่อขึ้นต้นด้วยตัวอักษร G และลงท้ายด้วยตัวอักษร E โดยแสดงผลเรียงตามลำดับตามตัวอักษรตัวแรกของนามสกุลจากน้อยไปมาก รวมถึงรายชื่อหนังที่นักแสดงคนนั้นแสดงด้วย
select first_name, last_name, title from actor join film_actor using (actor_id) join film using (film_id) WHERE first_name LIKE 'G%' and first_name LIKE '%E' ORDER BY last_name;

#2 .แสดงชื่อและนามสกุลของนักแสดงที่เล่นหนังเรื่อง 'Truman crazy'
select first_name, last_name from actor where actor_id in (select actor_id from film_actor where film_id in (select film_id from film where title = "Truman crazy"));

#3.แสดง category ที่มีจำนวนหนังใน category นั้นมากที่สุด 3 ลำดับแรก โดยแสดงจำนวนหนังใน category นั้นด้วย
select category_id, count(film_id) as film_count from film_category GROUP BY category_id order by count(film_id) DESC Limit 3;

#4. แสดงเรทติ้งของหนังทั้งหมด รวมทั้งจำนวนของหนังที่มีเรทติ้งนั้น และค่าเฉลี่ยความยาวของหนังในแต่ละกลุ่มเรทติ้ง เรียงลำดับจากมากไปหาน้อย
select rating, count(film_id), avg(length) from film group by rating ORDER BY avg(length) desc;

#5.แสดงชื่อและนามสกุลของนักแสดงที่มีผลงานการแสดงมากที่สุด รวมทั้งจำนวนเรื่องที่แสดงด้วย
select first_name, last_name, count(film_id) from film join film_actor using (film_id) join actor using (actor_id) group by actor_id order by count(film_id) desc Limit 1;

#6
CREATE TABLE Branch(
	Branch_code 			VARCHAR(10) 		NOT NULL PRIMARY KEY,
    Branch_name 			VARCHAR(35) 		NOT NULL ,
    Branch_city 			VARCHAR(35)			NOT NULL 
    );
    
CREATE TABLE Customer(
	Customer_code 			VARCHAR(10) 		NOT NULL PRIMARY KEY,
    Customer_name			VARCHAR(35) 		NOT NULL ,
    Customer_street			VARCHAR(80)			NOT NULL , 
    Customer_city			VARCHAR(35)			NOT NULL
    );

CREATE TABLE Loan(
	Loan_code 				VARCHAR(10) 		NOT NULL PRIMARY KEY,
    Branch_code 			VARCHAR(10) 		NOT NULL ,
    Amount					NUMERIC(10,2)		NOT NULL ,
    FOREIGN KEY (Branch_code) REFERENCES Branch(Branch_code)
    );
    
CREATE TABLE Borrower(
	Customer_code 			VARCHAR(10) 		NOT NULL ,
    Loan_code 				VARCHAR(10) 		NOT NULL ,
    PRIMARY KEY(Customer_code, Loan_code) ,
    FOREIGN KEY (Customer_code) REFERENCES Customer(Customer_code) ,
    FOREIGN KEY (Loan_code) REFERENCES Loan(Loan_code)
    );

CREATE TABLE Account(
	Account_number 			VARCHAR(10) 		NOT NULL PRIMARY KEY,
    Branch_code  			VARCHAR(10) 		NOT NULL ,
    Balance					NUMERIC(10,2)		NOT NULL ,
    FOREIGN KEY (Branch_code) REFERENCES Branch(Branch_code)
    );

CREATE TABLE Depositor(
	Customer_code 			VARCHAR(10) 		NOT NULL ,
	Account_number			VARCHAR(10) 		NOT NULL ,
    PRIMARY KEY(Customer_code, Account_number) ,
    FOREIGN KEY (Customer_code) REFERENCES Customer(Customer_code) ,
    FOREIGN KEY (Account_number) REFERENCES Account(Account_number)
    );

#7เพิ่มลูกค้ารายใหม่ โดยที่ลูกค้านั้นเปิดบัญชีเงินฝากด้วย (สามารถใช้ได้มากกว่า 1 คำสั่ง) – สามารถกำหนดข้อมูลได้เอง ภาษาอะไรก็ได้
Insert into Branch VALUES ("GG1","GG_atBangkok","Bangkok");
Insert into Branch VALUES ("GG2","GG_atChonburi","Chonburi");
Insert into Branch VALUES ("GG3","GG_atChiangMai","Chiang Mai");
Insert into Customer VALUES ("Cus0001","Kanate Boonsiri","126 Pracha Uthit Rd, Bang Mot, Thung Khru, Bangkok 10140","Bangkok");
Insert into Customer VALUES ("Cus0002","Thitipong Thongkam","1518​ Pracharat 1 Rd, Wong Sawang, Bang Sue, Bangkok 10800","Bangkok");
Insert into Customer VALUES ("Cus0003","Kantinan Meesuk","169 Long Had Bangsaen Rd, Saen Suk, Chonburi District, Chon Buri 20131","Chonburi");
Insert into Account VALUES ("Acc0001","GG1",76000);
Insert into Account VALUES ("Acc0002","GG1",45000);
Insert into Account VALUES ("Acc0003","GG2",50000);
Insert into Loan VALUES ("Loan0001","GG1",10000);
Insert into Loan VALUES ("Loan0002","GG1",15000);
Insert into Loan VALUES ("Loan0003","GG2",30000);
Insert into Borrower VALUES ("Cus0001","Loan0001");
Insert into Borrower VALUES ("Cus0002","Loan0002");
Insert into Borrower VALUES ("Cus0003","Loan0003");
Insert into Depositor VALUES ("Cus0001","Acc0001");
Insert into Depositor VALUES ("Cus0002","Acc0002");
Insert into Depositor VALUES ("Cus0003","Acc0003");

#8แสดงชื่อลูกค้าที่อยู่ในจังหวัด “Bangkok” ที่มียอดเงินฝากมากกว่ายอดเงินกู้ของลูกค้าทุกคนที่อยู่ในจังหวัด “Chonburi”
select * from Customer join Depositor using (Customer_code) join Account using (Account_number) where Customer_city = "Bangkok" and balance > (select sum(Amount) from branch join loan using (Branch_code) where Branch_city = "Chonburi" group by Branch_code);

#9ทางธนาคารต้องการแก้โครงสร้างของบางตารางเพื่อเก็บข้อมูลหมายเลขโทรศัพท์ของลูกค้าเพิ่มเติม จงเขียนคำสั่ง SQL สำหรับการทำงานข้างต้น โดยเลือกตารางให้เหมาะสม
ALTER TABLE Customer add Phone VARCHAR(12) NOT NULL;

#10แสดงรายชื่อลูกค้าที่มียอดเงินฝากมากกว่ายอดเงินกู้
select distinct Customer_name from Customer join Borrower using (Customer_code) join loan using (Loan_code) join Depositor using (Customer_code) join Account using (Account_number) where Balance > Amount;



select payment_id,customer_id,round(amount) AS 'rounding amount' from payment;
select sum(amount) 'Sum of amount' from payment where amount > 10.99;
select film_id,title,release_year from film where title < 'B';

#ขึ้นต้นด้วย B และถ้า C จะออก C เฉยๆจะออก
select * from film where title between 'B' AND 'C';  

select rental_id,rental_date from rental where rental_date > '2005-05-25';

select rental_id,rental_date from rental where rental_date between '2005-05-25' and '2005-05-26';
select rental_id,rental_date,staff_id from rental where rental_date between "2005-05-26 22:00:00" and "2005-05-27 00:00:00";


use University;

select * from advisor;
# เปรียบเทียบ แค่ course id กับ tkes id 
select name,title from student natural join takes,course where takes.course_id = course.course_id;
# เปรียบเทียบทุกตัว
select name,title from student natural join takes natural join course;

select * from student join takes on student.ID = takes.ID;
select * from student,takes where student.ID = takes.ID;

#ไม่มีโอกาสได้ใช้หลอก
select * from instructor, department;

select name, course_id from instructor,teaches where instructor.ID = teaches.ID;
select name,course_id from instructor join teaches using(ID);

select name,title from student natural join takes,course where takes.course_id = course.course_id;
select name,title from student natural join takes natural join course;

select name,course_id from instructor,teaches where instructor.id = teaches.id;
select name,title from instructor natural join teaches natural join course;
select name,title from (instructor natural join teaches)join course using (course_id);
select name,title from instructor join teaches using (id) join course using (course_id);

select T.name,S.course_id from instructor as T,teaches AS S 
where T.ID = S.ID;

select distinct T.name from instructor AS T,instructor as S
where T.salary > S.salary and s.dept_name = 'Biology';

select distinct course_id from section where semester = "Fall" and year = 2017 and course_id not in 
(select course_id from section where semester="Spring" and year =2018);

select count(distinct ID) from takes 
where (course_id,sec_id,semester,year) in 
(select course_id,sec_id,semester,year from teaches where teaches.ID = 10101);

select distinct T.name from instructor as T,instructor as S where T.salary > S.salary AND S.dept_name ='Biology';

select name from instructor where salary > some(select salary from instructor where dept_name='Biology');
select name from instructor where salary < all(select salary from instructor where dept_name='Biology');

select dept_name,avg(salary) from instructor group by dept_name;
select dept_name from instructor group by dept_name having avg(salary) >= all(select avg(salary) from instructor group by dept_name);

select course_id from section as s where semester = 'Fall' and year =2017 
and exists(select * from section as T where semester = 'Spring' and year = 2018
and S.course_id = T.course_id);

select T.course_id from course as T 
where 1 <= (select count(R.course_id) from section as R where T.course_id = R.course_id And R.year = 2009 );

select concat(name,' come form ',dept_name,' department.') from instructor;

select ucase(name) from instructor;

select Lcase(name) from instructor;

#sql start 1st index ที่ 1  ใส่่ 0 ไม่บัคแต่ไม่ออก  ถ้าใส่ -1 ที่ start จากตำแหน่งหลัง แต่จะไม่วน end <= 0 ไม่ได้ ถ้าใส่ทศนิยมจะปัด แบบเลขปกติ
select substr('CSS225 is easy',1,6) as result;
select substr(name,1,6) from instructor;

# replace => replace all 
select replace('css225 is easy','225','222') as result;

# trim Ltrim Rtrim ตัด space 
#lenght นับความยาวประโยค

use sakila;
select * from address;
select address,coalesce(address2,'none') new_address from address;

#ปรับคำตามจำนวน len 
select LPAD('css225 is easy',25,'.') as result;
select RPAD('css225 is easy',10,'.') as result;

select ascii('Css225 is easy') as result; 
select abs(-10);

select distinct(date_format(rental_date,'%d %b %Y')) from rental;

select current_date(),curdate(), current_time(),current_timestamp();
select dayofmonth(RENTAL_DATE) as day ,month(RENTAL_DATE) as month ,YEAR(RENTAL_DATE) as year from RENTAL;

select dayofmonth(curdate());
select datediff(curdate(),'2003-02-14');
select datediff('2008-01-14','2003-02-14');

select date_add('2020-01-01',INTERVAL 11 MONTH);
select date_add('2020-01-01',INTERVAL 10 DAY);

select * from RENTAL where RENTAL_DATE >= LAST_DAY(RENTAL_DATE)-20;

select 10 + '10';
select cast(10 as char);

# ifnull(notnull,null)

-- CASE value 
-- when [compare_value] then result
-- [when [compare_value] then result...]
-- [else result] 
-- end;


select * from film 
order by 
(case 
when rating is null then length else release_year
end);
