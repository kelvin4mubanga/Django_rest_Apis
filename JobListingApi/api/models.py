
from django.db import models

class Company(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    website = models.URLField(null=True, blank=True)
    description = models.TextField()

    def __str__(self):
        return self.name

class JobCategory(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Job(models.Model):
    JOB_TYPE_CHOICES = [
        ('full_time', 'Full Time'),
        ('part_time', 'Part Time'),
        ('contract', 'Contract'),
        ('internship', 'Internship'),
        ('freelance', 'Freelance'),
    ]

    title = models.CharField(max_length=255)
    company = models.ForeignKey(Company, related_name='jobs', on_delete=models.CASCADE)
    category = models.ForeignKey(JobCategory, related_name='jobs', on_delete=models.SET_NULL, null=True)
    job_type = models.CharField(max_length=20, choices=JOB_TYPE_CHOICES)
    description = models.TextField()
    location = models.CharField(max_length=255)
    salary_range = models.CharField(max_length=100)
    posted_at = models.DateTimeField(auto_now_add=True)
    last_date_to_apply = models.DateField()

    def __str__(self):
        return f"{self.title} at {self.company.name}"
