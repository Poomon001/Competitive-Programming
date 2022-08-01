-- Out of those counties with at least 25000 residents,
-- retrieve the pair from the same state
-- that had the absolute closest
-- population in 2018
-- 1.1 marks: <11 operators
-- 1.0 marks: <12 operators
-- 0.9 marks: <14 operators
-- 0.8 marks: correct answer

SELECT C.name, D.population, A.name, B.population
FROM county AS A
	JOIN countypopulation AS B
		ON A.fips=B.county AND B.population >= 25000 AND B.year=2018
	JOIN county AS C
		ON A.name<>C.name AND A.state=C.state
	JOIN countypopulation AS D
		ON C.fips=D.county AND D.population >= 25000 AND D.year=2018
ORDER BY abs(B.population-D.population) 
LIMIT 1;
