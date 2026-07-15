        # ORM
      # Save used two type -> create / update
   # CREATE DATA
student = Student(101,name = "Un virak", age = 22);
student.save();

   # READ DATA Display
students = Student.objects.all(); 

   # Fliter data Search data
Student.objects.fliter(id = 101);

   # Update data
student = Student.objects.get(id=101);
student.age = 22;
student.save();


   # DELETE DATA
student = Student.objects.get(id = 101);
student.delete();

   # 