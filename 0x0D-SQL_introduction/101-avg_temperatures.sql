-- Import in hbtn_0c_0 database 
SELECT city , AVG(value) as avg_temp
FROM temperatures
GROUB BY city
ORDER BY avg_temp DESC;
