--alter table health_facility_registry drop column index

/*Which Geo-political zone has the highest number of health professionals and the area with the lowest*/
select region, sum(no_of_health_personnel) as sum_of_person
from health_facility_registry
group by region
having region notnull
and sum(no_of_health_personnel) notnull
order by sum_of_person desc

/*2.What is the distribution of health professionals across the country? Do we have more Doctors,
Nurses or Lab scientists? */

select 
	sum(no_of_doctors) as doctors,
	sum(no_of_nurses) as nurses,
	sum(no_of_lab_scientists) as lab_scientists,
	sum(no_of_pharmacists) as pharmacists,
	sum(dentist) as dentist,
	sum(dental_technicians) as dental_tech,
	sum(pharmacy_technicians) as pham_tech,
	sum(midwifes) as midwifes,
	sum(lab_technicians) as lab_tech,
	sum(nurse_midwife) as nur_mdw,
	sum(him_officers) as HIM_officer,
	sum(community_health_officer) as comm_h_officer,
	sum(community_extension_workers) as comm_ext_workers,
	sum(jun_community_extension_worker) as jun_comm_ext_workers,
	sum(env_health_officers) as env_h_officers,
	sum(no_of_attendants) as health_attendants
from health_facility_registry

/*3.What's the average number of beds per facility? 
Are there facilities that do not have beds at all? If yes, which facility and what state?*/
select distinct R.state
from
(
	select state,facility_name, AVG(no_of_beds) as avg_bed
	from health_facility_registry
	group by facility_name , state
	having AVG(no_of_beds) isnull
)as R
	

/*4.Which year had the highest number of health facilities inaugurated?*/
select start_year, count(start_year) as coun
from health_facility_registry
group by start_year 
order by coun desc


/*5.Do privately owned facilities have more health personnel than Public?*/
select ownership, sum(no_of_health_personnel) 
from health_facility_registry
group by ownership

/*6.Which state has the highest number of privately owned health facilities?*/
select state, count(ownership)
from health_facility_registry
group by state, ownership
having ownership = 'Private'
order by count(ownership) desc 


/*7.Are there regions and facilities with no health personnel? 
What year were they inaugurated? Are they privately or publicly owned, 
and what is the Facility level?*/
with rf as
(
	select region, facility_name, start_year, ownership, facility_level
	from health_facility_registry
	where (no_of_health_personnel isnull) 
	or (no_of_health_personnel = 0)
), 
facility as
(select region,facility_name,start_year ,ownership,facility_level 
from rf)
select *
from facility


/*8.Which facility has the lowest hour of operation? What's the operation hour?*/
select f.facility_name, min(f.Hours_Of_Operation)
from
(SELECT facility_name,
		operation_status,
       REGEXP_REPLACE(operation_hour, '[^0-9]([0-9]{2}).', '\\1') AS Hours_Of_Operation
FROM health_facility_registry
WHERE operation_hour IS NOT NULL
GROUP BY 1, 2, 3) as f
group by f.facility_name , operation_status
having f.operation_status = 'Operational'
order by min(f.Hours_Of_Operation)


/*9.Which state has the highest number of unlicensed health facilities?*/
select state, count(license_status) as unlicense
from health_facility_registry
group by state ,license_status 
having license_status = 'Not Licensed'
order by unlicense desc

/*10.Which state has the highest number of licensed health facilities?*/
select state, count(license_status) as licensed
from health_facility_registry
group by state ,license_status 
having license_status = 'Licensed'
order by licensed desc

/*11.What is the ratio of Doctors to Nurses in each State?*/

select  state, round((sum_dn.sum_doctor/sum_dn.sum_nurse),2) as doctor_nurse_ratio
from
(select state, sum(no_of_doctors) as sum_doctor, sum(no_of_nurses) as sum_nurse
from health_facility_registry
group by state) as sum_dn
where (sum_dn.sum_nurse notnull and sum_dn.sum_nurse <> 0)
and (sum_dn.sum_doctor notnull and sum_dn.sum_doctor <> 0);

/*12.Facilities within 1km of each other in same LGA*/

SELECT
    *,
    111.045 * DEGREES(ACOS(COS(RADIANS(LagLat)) * 
    COS(RADIANS(latitude)) * COS(RADIANS(LagLong - longitude)) 
    + SIN(RADIANS(LagLat)) * SIN(RADIANS(latitude)))) AS KM
FROM
    (
        select
        	lga
        	facility_name,
            latitude,
            longitude,
            LAG(latitude) OVER (ORDER BY facility_name) AS LagLat,
            LAG(longitude) OVER (ORDER BY facility_name) AS LagLong
        FROM
            health_facility_registry hd 
    ) sub
  where 111.045 * DEGREES(ACOS(COS(RADIANS(LagLat)) * 
  COS(RADIANS(latitude)) * COS(RADIANS(LagLong - longitude)) + 
  SIN(RADIANS(LagLat)) * SIN(RADIANS(latitude)))) >= 0
	and 111.045 * DEGREES(ACOS(COS(RADIANS(LagLat)) * 
	COS(RADIANS(latitude)) * COS(RADIANS(LagLong - longitude)) +
	SIN(RADIANS(LagLat)) * SIN(RADIANS(latitude)))) <= 1 



/*13.First established Facility per LGA*/
select lga, min(start_date) as date_established
from health_facility_registry
group by lga;

/*14.How many facilities per LGA & Ward with their curresponding total per LGA and Ward separately*/
select distinct lga,count(g.facility_name)
from 
(
select lga, ward,facility_name
from health_facility_registry
) as g
group by lga;

select lga, count(facility_name)
from health_facility_registry
group by lga;

select ward, count(facility_name)
from health_facility_registry
group by ward; 


/*15.What facilities/facility have their tenure above the average facility tenure in their Ward as of today*/

select h2.facility_name, h2.tenure
from health_facility_registry as h2
join
(select ward, avg(tenure) as avg_tenure
from health_facility_registry
group by ward) as avg_ward_tenure
on avg_ward_tenure.ward = h2.ward 
and h2.tenure > avg_ward_tenure.avg_tenure
order by h2.facility_name;


/*16.Write a query to select earliet and latest Facilities per ward*/
select ward,  min(start_date) as earliest_date, max(start_date) as latest_date
from health_facility_registry
group by ward

/*17.When (in years) is the duration between the latest and earliest Facility per ward in each LGA.*/
select lga, ward, (max(start_year)-min(start_year)) as duration
from health_facility_registry
group by lga, ward 
order by lga 

/*18.What is the 3-years moving average of facility establishment per State*/
SELECT state, start_year, 
       AVG(count(facility_name)) OVER (PARTITION BY state ORDER BY start_year ROWS BETWEEN 2 PRECEDING AND CURRENT ROW) AS moving_average
FROM health_facility_registry
group by state, start_year ;


/*19.Find (in months) average month it takes for new facilities to be established per LGA.*/

select lga, round(AVG(start_month))AS avg_month
from health_facility_registry
group by lga;

/*20.From your exploration, If you are to advise the Minister of Health, 
which state or Region has the lowest should the Minister focus more on strengthening with more Facilities
and hiring more Health professionals?*/
select state,min(g.total_facilities), min(g.total_personnel)
from
(
	select state, count(facility_name) as total_facilities, sum(no_of_health_personnel) as total_personnel
	from health_facility_registry
	group by state
	order by total_facilities, total_personnel
) as g
group by state 
order by min(g.total_facilities), min(g.total_personnel)
limit 1;


-- to get the region the minister of health should focus more on strengthening with more facilities and more health proffessionals
select region,min(g.total_facilities), min(g.total_personnel)
from
(
	select region, count(facility_name) as total_facilities, sum(no_of_health_personnel) as total_personnel
	from health_facility_registry
	group by region
	order by total_facilities, total_personnel
) as g
group by region
order by min(g.total_facilities), min(g.total_personnel)
limit 1;

