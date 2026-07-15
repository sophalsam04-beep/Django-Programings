   #========================
    #     CRUD With ORM
    #========================
       # CREATE DATA
             # - Methods 1

from django.db import models

class Student(models.Model):
        name = models.CharField(max_length=100);
        email = models.EmailField();
        age = models.IntegerField();    
      
        
        def __str__(self):
            return self.name
        
        

students = Student(
        name = "Un virak",
        email = "virakun221@gmail.com",
        age = 22,
);

students.save();

            # - Methods 2
Student.objects.create(
    name = "Sam sophal",
    email = "samsophal222@gamil.com",
    age = 22,
    
    
    );


   # READ -> Read all data
students = Student.objects.all();
for student in students:
    print(student.name, student.email, student.age);

        # Read one data
    print(student.name);
    
    
    # Fliter -> search data
students = Student.objects.filter(age = 22);

for student in students:
    print(student.name);
    
    
    # Order by 
        # Ascending
students = Student.objects.order_by("name");

        # Descending
students = Student.objects.order_by("-age");


        # Update
students = Student.objects.get(id = 101);
students.age = 23,
students.email = "samsophal@gmail.com",

students.save();


    # Update by QuerySet
Student.objects.filter(id=101).update(age = 30);
Student.objects.filter(id=101).update(age = 25);


    # DELETE
students = Student.objects.get(id=101);
students.delete();


    # Delete alot data
students = Student.objects.filter(age__lt = 18).delete();


   # COUNT
total = Student.objects.count();
print(total);


   # FIRSTS / LAST
first = Student.objects.first();
last = Student.objects.last();


   # Exist
exists = Student.objects.filter(
    email = "sophal@gmail.com",
).exists();
print(exists);