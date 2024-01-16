-- average of two citys
SELECT city, AVG(value) as avg_temp
FROM temperatures
WHERE month = 7 OR month = 8
GROUB BY city 
ORDER BY avg_temp  DESC
LIMIT 3;
