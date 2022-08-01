-- Show the percentage of counties that have more
-- females than males.
-- 1.1 marks: <8 operators
-- 1.0 marks: <10 operators
-- 0.9 marks: <13 operators
-- 0.8 marks: correct answer

SELECT count(*)/(count(*)+max(K)) AS Fraction
FROM genderbreakdown AS A
	JOIN genderbreakdown AS B
		ON A.county=B.county AND A.gender<>B.gender AND B.gender='male' AND A.population > B.population
	JOIN (	SELECT count(*) AS K
			FROM genderbreakdown AS C
				JOIN genderbreakdown AS D
					ON C.county=D.county AND C.gender<>D.gender AND D.gender='male' AND C.population <= D.population) AS X;
