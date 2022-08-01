-- Retrieve alphabetically the states that had
-- over 100 counties with unemployment rates above 6.0%
-- in 2008.
-- Hint: Unemployment rate = unemployed / labour force
-- 1.1 marks: <8 operators
-- 1.0 marks: <9 operators
-- 0.9 marks: <11 operators
-- 0.8 marks: correct answer

SELECT abbr
FROM county
	JOIN state
		ON state.id=county.state
	JOIN countylabourstats
		ON countylabourstats.county=county.fips 
		AND countylabourstats.year=2008 
		AND (countylabourstats.unemployed/countylabourstats.labour_force)*100 > 6
	GROUP BY abbr
    HAVING count(abbr) > 100
    ORDER BY abbr;
