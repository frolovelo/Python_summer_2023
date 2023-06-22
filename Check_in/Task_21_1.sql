--SQL базовая таблица учеников--
CREATE TABLE Pupil(id INT PRIMARY KEY, name text, surname text, lastname text, id_contract int, level_education text, payed bool, finished bool);
INSERT INTO Pupil VALUES(1, 'Daniil', 'Vyacheslavovich', 'Frolov', 98473, 'higher education', True, False);
SELECT * FROM Pupil;
