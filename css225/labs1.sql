use sakila ;
desc film; 
select * from category;

select * from actor;
select first_name,last_name from actor;
select payment_id,customer_id,amount+1 from payment ;
select payment_id,customer_id,round(amount) rounding from payment ;

select sum(amount) 'sum of amount' from payment where amount > 10.99;

SELECT film_id, title, release_year FROM film WHERE title < 'B';
select payment_id,payment_date,amount from payment where amount != 0.99;
SELECT * FROM film WHERE title BETWEEN 'B' AND 'C';

SELECT * FROM film WHERE rating IN ('R', 'NC-17');

SELECT * FROM film WHERE title LIKE 'B%';
SELECT * FROM address WHERE address2 IS NOT NULL;

select * from city WHERE city LIKE 'a%' and city LIKE '%a';
select * from city WHERE city LIKE 'a%' OR city LIKE '%a';

select rental_id,return_date from rental WHERE return_date like '2005-06%';

select rental_id,rental_date , staff_id from rental where return_date;

