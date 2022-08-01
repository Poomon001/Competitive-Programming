-- Show which industries in which states (except DC)
-- employed at least 7.5% of the state's 2019 population,
-- ordered by the total payroll for that industry
-- in that state.
-- 1.1 marks: <26 operators
-- 1.0 marks: <30 operators
-- 0.9 marks: <35 operators
-- 0.8 marks: correct answer

SELECT DISTINCT abbr, industry.name, sum(payroll) AS 'Total Payrolls', (sum(employees)/x.total_population)*100 AS '% of Population'
FROM county
	JOIN state
		ON state.id=county.state AND state.abbr <> 'DC'
	JOIN (
		SELECT sum(p.population) AS total_population, s.id AS state_id
        FROM countypopulation AS p
			JOIN county AS c
				ON c.fips=p.county
			JOIN state AS s
				ON s.id=c.state
		WHERE p.year=2019
		GROUP BY id
    ) AS x
		ON state.id=state_id
	JOIN countylabourstats
		ON county.fips=countylabourstats.county
	JOIN countyindustries
		ON countyindustries.county=fips
	JOIN industry
		ON countyindustries.industry=industry.id
GROUP BY industry.name, state, countylabourstats.year, x.total_population
HAVING `% of Population` >= 7.5
ORDER BY sum(payroll) DESC;