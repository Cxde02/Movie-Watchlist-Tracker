CREATE TABLE Movies (
  ID int PRIMARY KEY,
  Name varchar(255),
  Genre varchar(255),
  Date date,
  Personal_Rating int CHECK (Personal_Rating >= 1 AND Personal_Rating <= 10)
);

--SELECT * FROM Movies

--DROP TABLE Movies

INSERT INTO Movies Values
(1, 'Eternals', 'Action, Adventure, Fantasy', '2024-02-07', 3),
(2, '65', 'Action, Adventure, Drama', '2024-01-27', 7),
(3, 'How to Train Your Dragon', 'Animation, Action, Adventure', '2024-02-13', 10),
(4, 'The Marvels', 'Action, Adventure, Fantasy', '2024-01-20', 7)
;

SELECT * FROM Movies WHERE Genre LIKE '%Drama%';
