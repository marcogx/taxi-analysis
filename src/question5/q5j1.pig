-- for negative income

FARE_RAW = LOAD 's3://zcxfinalproject/input/trip_fare_*.csv' USING PigStorage(',') AS (medallion:chararray, hack_license:chararray, vendor_id:chararray, pickup_datetime:chararray, payment_type:chararray, fare_amount:double, surcharge:double, mta_tax:double, tip_amount:double, tolls_amount:double, total_amount:double);

FARE = FILTER FARE_RAW BY medallion != 'medallion';

NEGATIVE_FARE = FILTER FARE BY total_amount < 0.0;

REDUCED_NEGATIVE = FOREACH NEGATIVE_FARE GENERATE 
hack_license, pickup_datetime, total_amount;
STORE REDUCED_NEGATIVE INTO 's3://zcxfinalproject/output/q5j1';

CTD_DATA = FOREACH REDUCED_NEGATIVE GENERATE hack_license, pickup_datetime, total_amount, 1 AS num_count;
GRP_DRV_DATA = GROUP CTD_DATA BY hack_license;
RESULT_BY_DRIVER = FOREACH GRP_DRV_DATA GENERATE 
group AS driver, SUM(CTD_DATA.num_count) AS count, SUM(CTD_DATA.total_amount) AS amount;
STORE RESULT_BY_DRIVER INTO 's3://zcxfinalproject/output/q5j1driver';


GRP_DAT_DATA = GROUP CTD_DATA BY SUBSTRING(pickup_datetime, 0,10);
RESULT_BY_DAT = FOREACH GRP_DAT_DATA GENERATE 
group AS date, SUM(CTD_DATA.num_count) AS count, SUM(CTD_DATA.total_amount) AS amount;
STORE RESULT_BY_DAT INTO 's3://zcxfinalproject/output/q5j1date';
