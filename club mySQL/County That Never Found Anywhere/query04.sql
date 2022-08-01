-- Retrieve alphabetically all states in which
-- every county has a name not found anywhere else
-- in the US
-- 1.1 marks: <8 operators
-- 1.0 marks: <9 operators
-- 0.8 marks: correct answer

SELECT DISTINCT abbr 
FROM county 
	JOIN state
		ON state.id=county.state
WHERE state NOT IN ( 
	SELECT A.state
	FROM county AS A
		JOIN county AS B
			ON A.name = B.name AND A.state <> B.state)
ORDER BY abbr;