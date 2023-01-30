import sqlite3
conn = sqlite3.connect("student.sqlite")
cursor = conn.cursor()

select_j = """
SELECT *
FROM students
WHERE firstname LIKE "J%";
"""

j_firstnames = cursor.execute(select_j).fetchmany(5)

find_gendernums = """
SELECT gender, COUNT(firstname)
FROM students
GROUP BY gender;
"""

gendernums = cursor.execute(find_gendernums).fetchall()

find_agenums = """
SELECT SUBSTR(firstname, 1, 1), SUM(age)
FROM students
GROUP BY SUBSTR(firstname, 1, 1);
"""

agenums = cursor.execute(find_agenums).fetchall()

