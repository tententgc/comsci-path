use sakila;

SELECT DISTINCT(rental_duration) FROM film;
SELECT MIN(length), MAX(length), AVG(length) FROM film where length between 60 and 100;
SELECT * FROM city WHERE city LIKE 'G%' or city LIKE '%z%'; 
select sum(amount) 'sum of amount' from payment;
select * from film order by replacement_cost desc;
