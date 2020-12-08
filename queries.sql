--1.	What is the average distance traveled by trips with a maximum of 2 passengers;
select avg(trip_distance) 
from funcional.trips 
where passenger_count <= 2;

--2.	Which are the 3 biggest vendors based on the total amount of money raised;
select 
v.name as "Vendor", sum(total_amount) as "Total" 
from funcional.trips t, funcional.vendor v 
where t.vendor_id = v.vendor_id 
group by Vendor 
order by Total desc 
limit 3;

--3.	Make a histogram of the monthly distribution over 4 years of rides paid with cash;
select
to_char(pickup_datetime, 'YYYY-MM') as periodo,sum(total_amount)
from funcional.trips
where payment_type ilike '%cash%'
group by periodo
order by periodo asc;

--4.	Make a time series chart computing the number of tips each day for the last 3 months of 2012.
select
to_char(pickup_datetime, 'YYYY-MM-DD') as data,sum(tip_amount) as soma
from funcional.trips
where extract(mon from pickup_datetime) between '10' and '12' and
      extract(Y from pickup_datetime) = '2012'
group by data
order by data asc;

--What is the average trip time on Saturdays and Sundays;
select 
CASE 
WHEN extract(dow from pickup_datetime) = '6' THEN 'Saturday'
WHEN extract(dow from pickup_datetime) = '0' THEN 'Sunday'
END as dayofweek,
avg(trip_distance) as avg
from funcional.trips 
where extract(dow from pickup_datetime) in ('0', '6')
group by dayofweek;

--Make a latitude and longitude map view of pickups and dropoffs in the year 2010;
select pickup_longitude AS longitude, pickup_latitude as latitude
from funcional.trips
where to_char(pickup_datetime, 'YYYY') = 2010
UNION ALL
select dropoff_longitude, dropoff_latitude
from funcional.trips
where to_char(pickup_datetime, 'YYYY') = 2010;