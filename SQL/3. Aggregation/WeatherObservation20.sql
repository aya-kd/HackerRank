WITH SortedData AS (
    SELECT LAT_N
    FROM STATION
    ORDER BY LAT_N
),
CountedData AS (
    SELECT LAT_N,
           ROW_NUMBER() OVER (ORDER BY LAT_N) AS RowAsc,
           ROW_NUMBER() OVER (ORDER BY LAT_N DESC) AS RowDesc
    FROM SortedData
)
SELECT ROUND(AVG(LAT_N),4) AS Median
FROM CountedData
WHERE RowAsc = RowDesc
   OR RowAsc + 1 = RowDesc
   OR RowAsc = RowDesc + 1;