from django.db import models
from django.utils.html import mark_safe
from autoslug import AutoSlugField
from ckeditor_uploader.fields import RichTextUploadingField


# Create your models here.


class Department(models.Model):
    departmentid = models.AutoField(primary_key=True)
    departmentname = models.CharField(max_length=500, null=False, blank=False)
    isactive = models.BooleanField(default='1', null=False, blank=False)

    class Meta:
        db_table = 'Department'


class Employee(models.Model):
    employeeid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=250, null=False, blank=False)
    email = models.EmailField(
        max_length=500, null=False, blank=False, default='')
    dateofjoining = models.DateTimeField(auto_now_add=True)
    department = models.ForeignKey(
        'Department', on_delete=models.CASCADE,  null=False, blank=False)
    isactive = models.BooleanField(default='1', null=False, blank=False)

    class Meta:
        db_table = 'Employee'


class Project(models.Model):
    projectid = models.AutoField(primary_key=True)
    projectname = models.CharField(max_length=250, null=False, blank=False)
    project_start_date = models.DateTimeField(
        auto_now_add=True, blank=False, null=False)
    project_end_date = models.DurationField(null=True, blank=True)
    project_manager_name = models.ForeignKey(
        'Employee', on_delete=models.CASCADE, null=False, blank=False)
    project_manager_email = models.EmailField(
        max_length=250, null=False, blank=False)

    class Meta:
        db_table = 'Project'
