-- Retrieve alphabetically the names of industries that
-- employ at least five million workers across
-- the US, excluding California.
-- 1.1 marks: <9 operators
-- 1.0 marks: <11 operators
-- 0.9 marks: <14 operators
-- 0.8 marks: correct answer

SELECT industry.name
FROM county
	JOIN state
		ON state.id=county.state AND state.abbr<>'CA'
	JOIN countyindustries
		ON countyindustries.county=county.fips
	JOIN industry
		ON industry.id=countyindustries.industry
GROUP BY countyindustries.industry
Having sum(employees) >= 5000000
ORDER BY industry.name;
