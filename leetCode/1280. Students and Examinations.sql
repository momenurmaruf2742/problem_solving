-- # Write your MySQL query statement below
# select student_id,student_name,subject_name,count(subject_name) attended_exams from Examinations a

SELECT
    s.student_id,
    s.student_name,
    e.subject_name,
    COALESCE(COUNT(a.student_id), 0) AS attended_exams
FROM
    (SELECT DISTINCT student_id,student_name FROM Students) s
CROSS JOIN
    (SELECT DISTINCT subject_name FROM Subjects) e
LEFT JOIN
    Examinations a ON s.student_id = a.student_id AND e.subject_name = a.subject_name
GROUP BY
    s.student_id, e.subject_name
ORDER BY
    s.student_id, e.subject_name;


-- Create table If Not Exists Students (student_id int, student_name varchar(20))
-- Create table If Not Exists Subjects (subject_name varchar(20))
-- Create table If Not Exists Examinations (student_id int, subject_name varchar(20))
-- Truncate table Students
-- insert into Students (student_id, student_name) values ('1', 'Alice')
-- insert into Students (student_id, student_name) values ('2', 'Bob')
-- insert into Students (student_id, student_name) values ('13', 'John')
-- insert into Students (student_id, student_name) values ('6', 'Alex')
-- Truncate table Subjects
-- insert into Subjects (subject_name) values ('Math')
-- insert into Subjects (subject_name) values ('Physics')
-- insert into Subjects (subject_name) values ('Programming')
-- Truncate table Examinations
-- insert into Examinations (student_id, subject_name) values ('1', 'Math')
-- insert into Examinations (student_id, subject_name) values ('1', 'Physics')
-- insert into Examinations (student_id, subject_name) values ('1', 'Programming')
-- insert into Examinations (student_id, subject_name) values ('2', 'Programming')
-- insert into Examinations (student_id, subject_name) values ('1', 'Physics')
-- insert into Examinations (student_id, subject_name) values ('1', 'Math')
-- insert into Examinations (student_id, subject_name) values ('13', 'Math')
-- insert into Examinations (student_id, subject_name) values ('13', 'Programming')
-- insert into Examinations (student_id, subject_name) values ('13', 'Physics')
-- insert into Examinations (student_id, subject_name) values ('2', 'Math')
-- insert into Examinations (student_id, subject_name) values ('1', 'Math')