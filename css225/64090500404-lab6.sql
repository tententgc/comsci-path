use sakila;
#1
select film_id, title,7 rental_duration from film;

#2
select ucase(substr(title,1,3)) as name_movie from film;

#3
SELECT DATE_FORMAT(FROM_DAYS(DATEDIFF(NOW(),'2003-02-14')), '%Y')  + 0 AS age;



#4
select concat(date_format(curdate(),'%y'),dayofyear(curdate())) as JulianDate;

#5
select date_format(curdate(),'%Y-%M-%e') as today;
select date_format(curdate(),'%e-%c-%Y') as today;
select date_format(curdate(),'%c %e %Y') as today;
select date_format(curdate(),'%Y-%M-%d') as today;
select date_format(curdate(),'%Y-%c-%e') as today;
