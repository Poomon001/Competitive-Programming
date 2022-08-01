-- Show which county has the largest relative population decrease
-- from 2010 to 2019.
-- 1.1 marks: <11 operators
-- 1.0 marks: <13 operators
-- 0.9 marks: <16 operators
-- 0.8 marks: correct answer

SELECT name, A.population AS '2010', B.population AS '2019', abbr, 100-((B.population/A.population)*100) AS 'Loss (%)' 
FROM county
	JOIN state
		ON state.id=county.state
	JOIN countypopulation AS A
		ON A.county=county.fips AND A.year=2010
	JOIN countypopulation AS B
		ON B.county=county.fips AND B.year=2019
ORDER BY 100-((B.population/A.population)*100) DESC
LIMIT 1;
