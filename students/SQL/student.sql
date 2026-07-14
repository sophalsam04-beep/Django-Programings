  -- Create data in sql
insert into student (name, age)
values (101,'un virak', 35)

  -- READ DATA in SQL
SELECT * FROM student;

  -- Fliter data Search data
SELECT * FROM student
WHERE id = 101;

  -- Update data 
update student
   SET age = 22
        WHERE id = 101;

  -- Delete data
delete from student
where id = 101;