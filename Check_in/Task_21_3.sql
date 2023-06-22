--SQL создание таблицы
CREATE TABLE book(id INT PRIMARY KEY, author text, title text, id_publisher int);
INSERT INTO book VALUES (1, 'Ремарк Э.М.', 'Три товарища', 10),
(2, 'Оруэлл Д.', '1984', 20),
(3, 'Булгаков М.А.', 'Мастер и Маргарита', 30),
(4, 'Достоевский Ф.М.', 'Идиот', 40);
SELECT author, title FROM book;

