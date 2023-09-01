from django.db import models

# Create your models here.

class Attendance(models.Model):
  username = models.CharField(max_length = 150)
  subject = models.CharField(max_length = 150, null=True)
  class_attended = models.IntegerField(default=1)

  class Meta:
    db_table = 'attendance'

class StudentCourses(models.Model):
  username = models.CharField(max_length = 150, null=True)
  course = models.CharField(max_length = 150, null=True)
  number_of_subjects = models.IntegerField(default = 0)
  subject1 = models.CharField(max_length = 150, null=True)
  subject2 = models.CharField(max_length = 150, null=True)
  subject3 = models.CharField(max_length = 150, null=True)
  subject4 = models.CharField(max_length = 150, null=True)
  subject5 = models.CharField(max_length = 150, null=True)
  subject6 = models.CharField(max_length = 150, null=True)
  subject7 = models.CharField(max_length = 150, null=True)
  subject8 = models.CharField(max_length = 150, null=True)
  subject9 = models.CharField(max_length = 150, null=True)
  subject10 = models.CharField(max_length = 150, null=True)
  subject11 = models.CharField(max_length = 150, null=True)
  subject12 = models.CharField(max_length = 150, null=True)
  subject13 = models.CharField(max_length = 150, null=True)
  subject14 = models.CharField(max_length = 150, null=True)
  subject15 = models.CharField(max_length = 150, null=True)
  subject16 = models.CharField(max_length = 150, null=True)
  subject17 = models.CharField(max_length = 150, null=True)
  subject18 = models.CharField(max_length = 150, null=True)
  subject19 = models.CharField(max_length = 150, null=True)
  subject20 = models.CharField(max_length = 150, null=True)

  class Meta:
    db_table = 'student_courses'