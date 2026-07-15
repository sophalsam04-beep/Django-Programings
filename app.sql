    -- =============================
    --         SQL CRUD ORM       --
    -- =============================

    -- CREATE DATA
insert into student (name, age, email)
values ('Sophal','daravirak221@gmail.com', 22);

    -- READ DATA
select * from student;
    
    -- read one data
SELECT * FROM student
where id = 101;

    -- fliter -> search data. --
SELECT * FROM student
where age = 22;


    -- update ---
update student
   set age=22
where id = 101;


    -- Delete --
delete from student
 where id = 101;