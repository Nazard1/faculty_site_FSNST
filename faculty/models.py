from django.db import models

class Department(models.Model):
    name = models.CharField(max_length=100)
    head_of_department = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Program(models.Model):
    department = models.ForeignKey(Department, on_delete = models.CASCADE)
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=10)
    description = models.TextField()
    coordinator = models.CharField(max_length=100)
    coordinator_contacts = models.CharField(max_length=250)

    def __str__(self):
        return self.name

class Subject(models.Model):
    program = models.ForeignKey(Program, on_delete = models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField()
    credits = models.IntegerField()
    semester = models.IntegerField()

    def __str__(self):
        return self.name

class Teacher(models.Model):
    name = models.CharField(max_length = 100)
    degree = models.CharField(max_length = 100, null = True, blank = True)
    position = models.CharField(max_length = 100)
    department = models.ForeignKey(Department, on_delete = models.SET_NULL, null = True, blank = True)
    
    def __str__(self):
        return self.name


class HomePage(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    contacts = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title
