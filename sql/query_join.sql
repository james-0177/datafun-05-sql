-- Using INNER JOIN in a query.

SELECT *
FROM books
INNER JOIN authors ON books.author_id = authors.author_id
WHERE authors.last = 'Tolkien';