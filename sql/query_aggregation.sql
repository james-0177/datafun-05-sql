-- Using aggregation functions, to include COUNT, AVG, AND SUM.

SELECT COUNT(*)
FROM books
WHERE year_published < 1980;

SELECT AVG(year_published)
FROM books;

SELECT SUM(year_published)
FROM books;