-- Retrieve the state with the median number of
-- employees in 'Education Services'
-- 1.1 marks: < 10 operators
-- 1.0 marks: < 11 operators
-- 0.8 marks: correct answer

SELECT abbr, sum(employees) AS TotalEmployees 
FROM countyindustries 
	JOIN county 
		ON (county = fips) 
	JOIN state 
		ON (state = id) 
	JOIN industry 
		ON (industry.name='Educational services' AND industry.id=countyindustries.industry) 
GROUP BY abbr
ORDER BY TotalEmployees 
LIMIT 1 OFFSET 25;