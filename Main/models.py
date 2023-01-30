from datetime import datetime

from django.db import models


# Create your models here.
class Release(models.Model):
    class Meta:
        db_table = "release"

    version = models.CharField(max_length=16)

    def __str__(self):
        return self.version


class Issue(models.Model):
    class Meta:
        db_table = "issue"

    release = models.ForeignKey(Release, on_delete=models.CASCADE)
    project_name = models.CharField(max_length=30)
    issue = models.CharField(max_length=30)
    designer_name = models.CharField(max_length=30)
    executor_name = models.CharField(max_length=30)
    design_date = models.DateField(default=datetime.now)
    execution_date = models.DateField(default=datetime.now)

    def __str__(self):
        return self.issue


class Case(models.Model):
    class Meta:
        db_table = "case"

    issue = models.ForeignKey(Issue, on_delete=models.CASCADE)
    title = models.TextField(max_length=128)
    summary = models.TextField(max_length=1024)
    steps = models.TextField(max_length=4096)
    expected_result = models.TextField(max_length=1024)
    actual_result = models.TextField(max_length=1024)

    class Status(models.TextChoices):
        ToDo = 'ToDo'
        Ok = 'Ok'
        NotOk = 'Not Ok'
        Review = 'Review'
        InProgress = 'In Progress'

    status = models.CharField(
        max_length=11,
        choices=Status.choices,
        default=Status.Ok,
    )

    notes = models.TextField(max_length=4096)
    logs = models.TextField(max_length=8192)
    database_records = models.TextField(max_length=8192)

    def __str__(self):
        return ' Title: ' + self.title
