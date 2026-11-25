
-- 1. Create student table
CREATE TABLE students (
    student_id INT PRIMARY KEY,
    name VARCHAR(50),
    math INT,
    science INT,
    english INT,
    computer INT,
    history INT
);

-- 2. Display all students
SELECT * FROM students;

-- 3. Display students who scored above 80% overall
SELECT name,
       (math + science + english + computer + history) / 5.0 AS percentage
FROM students
WHERE (math + science + english + computer + history) / 5.0 > 80;

-- 4. Find the highest scorer
SELECT name,
       (math + science + english + computer + history) AS total_marks
FROM students
ORDER BY total_marks DESC
LIMIT 1;

-- 5. Display students who passed
SELECT name
FROM students
WHERE math >= 40
  AND science >= 40
  AND english >= 40
  AND computer >= 40
  AND history >= 40;

-- 6. Count total students
SELECT COUNT(*) AS total_students FROM students;
