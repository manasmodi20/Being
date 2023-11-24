from django.db import models
class Student(models.Model):
    student_name = models.CharField(max_length = 50)
    roll_number = models.CharField(max_length = 20)
    email = models.EmailField(unique = True)
    date_of_birth = models.DateField()
    
    def __str__(self):
        return self.roll_number
