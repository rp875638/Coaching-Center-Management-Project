# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    accepted = models.IntegerField(default=False,blank=True, null=True)
    @property
    def is_accepted(self):
        if User.objects.filter(id = self.id,accepted=1):
            return True
        return False
class Assignment(models.Model):
    idassignment = models.IntegerField(primary_key=True)
    idbatch = models.IntegerField()
    topic = models.CharField(max_length=45)
    subject = models.CharField(max_length=45)
    issuedate = models.DateField()
    duedate = models.DateField()

    class Meta:
        
        db_table = 'assignment'
        unique_together = (('idassignment', 'idbatch'),)


class Batch(models.Model):
    idteacher = models.IntegerField(primary_key=True)
    subject = models.CharField(max_length=45)
    type = models.CharField(max_length=45)
    start_time = models.TimeField()
    end_time = models.TimeField()

    class Meta:
        
        db_table = 'batch'


class Fees(models.Model):
    idfees = models.AutoField(primary_key=True)
    idstudent = models.IntegerField()
    amount = models.IntegerField()
    month = models.CharField(max_length=45)
    year = models.CharField(max_length=45)
    dates = models.DateField()

    class Meta:
        
        db_table = 'fees'
        unique_together = (('idfees', 'idstudent'),)


class Notifications(models.Model):
    idnotifications = models.IntegerField(primary_key=True)
    notifications = models.CharField(max_length=45)
    dates = models.DateField()

    class Meta:
        
        db_table = 'notifications'
class Result(models.Model):
    idresult = models.IntegerField(primary_key=True)
    idstudent = models.IntegerField()
    subject = models.CharField(max_length=45)
    obtain_marks = models.IntegerField()
    total_marks = models.IntegerField()
    rdate = models.DateField()

    class Meta:
        db_table = 'result'

class Salary(models.Model):
    idsalary = models.AutoField(primary_key=True)
    iduser = models.IntegerField()
    amount = models.IntegerField()
    dates = models.DateField()
    month = models.CharField(max_length=45)
    year = models.CharField(max_length=45)

    class Meta:
        
        db_table = 'salary'
        unique_together = (('idsalary', 'iduser'),)


class Staff(models.Model):
    idstaff = models.IntegerField(primary_key=True)
    type = models.CharField(max_length=45)
    amount = models.IntegerField()

    class Meta:
        
        db_table = 'staff'


class Student(models.Model):
    idstudent = models.AutoField(primary_key=True)
    subject1 = models.CharField(max_length=45)
    subject2 = models.CharField(max_length=45)
    subject3 = models.CharField(max_length=45)
    type = models.CharField(max_length=45)
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    email = models.CharField(max_length=45)
    contact = models.CharField(max_length=45)
    dob = models.DateField()
    username = models.CharField(unique=True, max_length=45)
    class Meta:
        
        db_table = 'student'


class StudentAttendence(models.Model):
    idstudent = models.IntegerField(primary_key=True)
    dates = models.DateField()
    is_present = models.CharField(max_length=12)
    is_reject = models.IntegerField()

    class Meta:
        
        db_table = 'student_attendence'
        unique_together = (('dates', 'idstudent'),)

class StudentBatch(models.Model):
    batchid = models.IntegerField(primary_key=True)
    studentid = models.CharField(max_length=45)

    class Meta:
        
        db_table = 'student_batch'
        unique_together = (('batchid', 'studentid'),)


class StudentNotification(models.Model):
    idnotification = models.IntegerField(primary_key=True)
    idstudent = models.IntegerField()
    is_seen = models.IntegerField()
    notify = models.CharField(max_length=45)
    ndate = models.DateTimeField()

    class Meta:
        
        db_table = 'student_notification'
        unique_together = (('idnotification', 'idstudent'),)

class Teacher(models.Model):
    idteacher = models.AutoField(primary_key=True)
    subject = models.CharField(max_length=45)
    first_name = models.CharField(max_length=256)
    last_name = models.CharField(max_length=45)
    dob = models.DateField()
    contact = models.CharField(max_length=45)
    email = models.CharField(max_length=45)
    username = models.CharField(unique=True, max_length=45)
    class Meta:
        
        db_table = 'teacher'

class TeacherAttendence(models.Model):
    idteacher = models.IntegerField(primary_key=True)
    dates = models.DateField()
    is_present = models.CharField(max_length=12)

    class Meta:
        
        db_table = 'teacher_attendence'
        unique_together = (('idteacher', 'dates'),)


class TeacherNotification(models.Model):
    idnotification = models.AutoField(primary_key=True)
    idteacher = models.IntegerField(unique=True, blank=True, null=True)
    is_seen = models.IntegerField()
    notify = models.CharField(max_length=256)
    ndate = models.DateTimeField()

    class Meta:
        
        db_table = 'teacher_notification'
class Test(models.Model):
    idtest = models.AutoField(primary_key=True)
    subject = models.CharField(max_length=45)
    topic = models.CharField(max_length=45)
    start_time = models.TimeField()
    end_time = models.TimeField()
    dates = models.DateField()
    idbatch = models.IntegerField()
    class Meta:
        db_table = 'test'