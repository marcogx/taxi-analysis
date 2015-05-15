-- for suspect income

FARE_RAW = LOAD 's3://zcxfinalproject/input/trip_fare_*.csv' USING PigStorage(',') AS (medallion:chararray, hack_license:chararray, vendor_id:chararray, pickup_datetime:chararray, payment_type:chararray, fare_amount:double, surcharge:double, mta_tax:double, tip_amount:double, tolls_amount:double, total_amount:double);

FARE = FILTER FARE_RAW BY medallion != 'medallion';

SUSPECT_DATA = FILTER FARE BY (total_amount - tolls_amount - tip_amount - mta_tax - surcharge - fare_amount > 5.0);

RESULT = FOREACH SUSPECT_DATA GENERATE 
hack_license AS driver,
pickup_datetime AS pickup_datetime,
total_amount AS total_amount,
(total_amount - tolls_amount - tip_amount - mta_tax - surcharge - fare_amount) AS overcharge,
1 AS num_count;

DATA_BY_DRV = GROUP RESULT BY driver;
RESULT_BY_DRV = FOREACH DATA_BY_DRV GENERATE 
group AS driver,
SUM(RESULT.num_count) AS count,
SUM(RESULT.overcharge) AS total_overcharge,
SUM(RESULT.total_amount);
STORE RESULT_BY_DRV INTO 's3://zcxfinalproject/output/q5j2driver';

DATA_BY_DATE = GROUP RESULT BY SUBSTRING(pickup_datetime, 0,10);
RESULT_BY_DATE = FOREACH DATA_BY_DATE GENERATE 
group AS date,
SUM(RESULT.num_count) AS count,
SUM(RESULT.overcharge) AS total_overcharge,
SUM(RESULT.total_amount);
STORE RESULT_BY_DATE INTO 's3://zcxfinalproject/output/q5j2date';