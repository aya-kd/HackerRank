SELECT CONCAT(Name,"(",LEFT(Occupation, 1),")")
FROM OCCUPATIONS
ORDER BY Name;

SELECT
  CASE
    WHEN Occupation = 'Doctor' THEN CONCAT('There are a total of ',COUNT(Occupation), ' doctors.')
    WHEN Occupation = 'Actor' THEN CONCAT('There are a total of ',COUNT(Occupation), ' actors.')
    WHEN Occupation = 'Professor' THEN CONCAT('There are a total of ',COUNT(Occupation), ' professors.')
    ELSE CONCAT('There are a total of ',COUNT(Occupation), ' singers.')
  END
FROM OCCUPATIONS
GROUP BY Occupation
ORDER BY COUNT(Occupation), Occupation;