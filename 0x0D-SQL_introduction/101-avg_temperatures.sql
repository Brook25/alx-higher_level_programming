-- displays the average temperature  in Fahrenheit by city ordered by temperature in descending order
-- display average value of every city
SELECT city, AVG(value) AS avg_temp FROM temperatures GROUP BY city ORDER BY avg_temp DESC;
