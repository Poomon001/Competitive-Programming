-- Retrieve by increasing snowfall the number of employees
-- in 'Mining, quarrying, and oil and gas extraction' for all
-- counties that have the words 'iron', 'coal', or 'mineral'
-- in their name.
-- 1.1 marks: <13 operators
-- 1.0 marks: <15 operators
-- 0.9 marks: <20 operators
-- 0.8 marks: correct answer

SELECT county.name, abbr, employees
FROM county
	JOIN state
		ON state.id=county.state 
	JOIN industry
		ON industry.name='Mining, quarrying, and oil and gas extraction'
	LEFT JOIN countyindustries
		ON county=fips AND industry.id=countyindustries.industry
WHERE county.name LIKE '%iron%' OR county.name LIKE '%coal%' OR county.name LIKE '%mineral%'
ORDER BY snow;
