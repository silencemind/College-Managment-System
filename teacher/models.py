from django.db import models
from django.db.models.fields.related import ForeignKey, ManyToManyField, OneToOneField
from users.models import Users
from django.contrib.auth.models import Group
from department.models import *
import uuid
# Create your models here.

class Teacher(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.OneToOneField(Users, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=100)
    dept = models.ForeignKey('department.Dept', on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.name

class teacher_assignnment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    assign = ForeignKey('department.Assign', on_delete=models.CASCADE, unique=False)
    assignnment_file = models.FileField(upload_to='documents/')
    assignnment= models.CharField(max_length=2000)
    assignment_date = models.DateField()
    deadline_date = models.DateField()
