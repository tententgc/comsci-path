use sakila;
#1 แสดงชื่อลูกค้าที่ไม่เคยเช่าหนังเลย
select first_name,last_name from customer where customer_id not in (select customer_id from rental);
 
#2แสดงชื่อหมวดหมู่หนังทั้งหมดพร้อมกับจํานวนหนังในแต่ละหมวดนั้นเรียงจากชื่อหมวดAไปZ
select name,count(film_id) as countfilm from category join film_category using(category_id) group by name;

#3 แสดงรายชื่อหนังที่มีความยาวสูงสุด3อันดับแรกในแต่ละrate

select title,rating from film where rating ='PG' order by length(title) desc limit 3;
select title,rating from film where rating ='G' order by length(title) desc limit 3;
select title,rating from film where rating ='NC-17' order by length(title) desc limit 3;
select title,rating from film where rating ='PG-13' order by length(title) desc limit 3;
select title,rating from film where rating ='R' order by length(title) desc limit 3;

#4 แสดงผลต่างของความยาวหนังที่มากที่สุดและความยาวหนังที่น้อยที่สุดในร้าน
select max(length)- min(length) from film;

#5 แสดงข้อความ“xxxistheanswer!”โดยที่xxxคือชื่อหนังที่มีความยาวสูงที่สุด

select concat(title,' is the answer!') from film order by length(title) desc limit 1;

#7แสดงรายละเอียดทุกอย่างของหนังที่ลงท้ายด้วยerและขึ้นต้นด้วยm
select * from film where title like 'm%' and title like '%er';

#8แสดง10รายชื่อแรกที่เช่าหนังมากที่สุด
select first_name,last_name,count(*) as numbercount  from customer join rental using(customer_id) group by customer_id order by numbercount desc limit 10;

#9แสดงสาขาที่มีความนิยมสูงที่สุด
select staff_id as storename from rental join staff using (staff_id) group by staff_id order by count(*) desc limit 1;


#12ตั้งโจทย์เอง 1 ข้อที่ใช้การ join ตารางตั้งแต่ 2 ตารางขึ้นไป โดยกําหนดทั้งโจทย์ และ SQL ที่สอดคล้องกับโจทย์นั้น

# แสดงชื่อและนามสกุลของนักแสดงที่มีผลงานการแสดงมากที่สุด บอกจำนวนหนังด้วย
select first_name, last_name, count(film_id) from film join film_actor using (film_id) join actor using (actor_id) group by actor_id order by count(film_id) desc Limit 1;

#13แสดงข้อมูลการเช่าทั้งหมดของ rental_id 1 ได้แก่ชื่อหนัง วันเวลาที่ยืม วันเวลาที่คืน ชื่อคนที่ยืม ยืมจากสาขาไหน เป็นต้น.  --> ทำไม่ทันครับแต่เผามาก่อน
select * from customer join rental using (customer_id) join store using(store_id) where rental_id = 1;

#14จาก ER diagram ต่อไปนี้ จงเขียนคําสั่ง SQL สร้าง table ทั้งหมด

CREATE TABLE Customer(
	Customer_ID				VARCHAR(10) 		NOT NULL PRIMARY KEY,
	fullname				VARCHAR(10) 		NOT NULL ,
    contact_add				NUMERIC(10,2)		NOT NULL ,
    address					VARCHAR(100)			NOT NULL
);

CREATE TABLE Categories(
	category_ID 			VARCHAR(10) 		NOT NULL PRIMARY KEY,
    category_name 			VARCHAR(35) 		NOT NULL ,
    category_type 			VARCHAR(35)			NOT NULL 
    );
    
CREATE TABLE Shopping_Order(
	order_ID				VARCHAR(10) 		NOT NULL PRIMARY KEY,
    Customer_ID				VARCHAR(35) 		NOT NULL,
	date_time 				DATE				not null,
    FOREIGN KEY (Customer_ID) REFERENCES Customer(Customer_ID)
);

CREATE TABLE Deliveries(
	Deliveries_ID			VARCHAR(10) 		NOT NULL ,
    Customer_ID 			varchar(10)			not null,
    date_time 				DATE 				not null,
    FOREIGN KEY (Customer_ID) REFERENCES Customer(Customer_ID)
);

CREATE TABLE Payment(
	Payment_ID				VARCHAR(10) 		NOT NULL PRIMARY KEY,
    category_ID  			VARCHAR(10) 		NOT NULL ,
    date_time				date 				NOT NULL ,
    FOREIGN KEY (category_ID) REFERENCES Categories(category_ID)
    );
    
CREATE TABLE Seller(
	seller_ID				VARCHAR(10) 		NOT NULL ,
    product_ID				VARCHAR(10) 		NOT NULL ,
	fullname 				VARCHAR(25) 		NOT NULL,
    FOREIGN KEY (product_ID) REFERENCES Product(product_ID)
    );

CREATE TABLE Products(
	Product_ID			VARCHAR(10) 		NOT NULL ,
	category_ID			VARCHAR(10) 		NOT NULL ,
    product_name 		varchar(25) 		not null,
    FOREIGN KEY (category_ID) REFERENCES Categories(category_ID)
    );

CREATE TABLE Transaction_Reports(
	report_ID				VARCHAR(10) 		NOT NULL primary key ,
    customer_ID			VARCHAR(10) 		NOT NULL ,
    Order_ID 			VARCHAR(10) 		not null,
    Product_ID 			varchar(10) 		not null,
	Payment_ID 			Varchar(10) 		not null,
    FOREIGN KEY (customer_ID) REFERENCES Customer(customer_ID) ,
    FOREIGN KEY (Order_ID) REFERENCES Shopping_order(Order_ID) ,
    FOREIGN KEY (Product_ID) REFERENCES Product(Product_ID) ,
    FOREIGN KEY (Payment_ID) REFERENCES Payment(Payment_ID)
    );
    
