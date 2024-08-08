from django.db import models

# Create your models here.
class Student_Management:
    student_id = models.CharField(max_length=200, null=True)
    full_name = models.CharField(max_length=200, null=True)
    age = models.PositiveIntegerField
    grade = models.CharField(max_length=10, null=True) #Khối lớp: vd 11
    year_of_birth = models.PositiveIntegerField
    gender=models.CharField(max_length=10, null=True)
    school = models.CharField(max_length=50, null=True)
    student_code = models.CharField(max_length=50)
    def __str__(self) -> str:
        return self.full_name
    
class ClassSchedule(models.Model):
    date = models.DateField()  # Ngày học
    start_time = models.TimeField()  # Giờ bắt đầu
    end_time = models.TimeField()  # Giờ kết thúc

    def __str__(self):
        return f"{self.class_instance.name} - {self.date} ({self.start_time} to {self.end_time})"
    
class Classroom_Management:
    classroom_id = models.CharField(max_length=200, null=True)
    class_name = models.CharField(max_length=200, null=True)
    address = models.CharField(max_length=200, null=True)
    schedule = models.ForeignKey("ClassSchedule",on_delete=models.CASCADE)
    school = models.CharField(max_length=50, null=True)
    classroom_code = models.CharField(max_length=50)
    attendance_sheet_id = models.CharField(max_length=200, null=True)
    def __str__(self) -> str:
        return self.class_name
    @property
    def get_student_id(self): # lấy student_id từ trường Student_Management
        students = self.student_set.all() 
        student_order = students.student_id
        return student_order
    
class Attendance_Management:
    attendance_id =  models.CharField(max_length=200, null=True)
    date_attendance = models.DateTimeField(auto_now_add=True)
    time_attendance = models.TimeField(auto_now_add=True)
    @property
    def get_student_id(self): # lấy student_id từ trường Student_Management
        students = self.student_set.all() 
        student_order = students.student_id
        return student_order