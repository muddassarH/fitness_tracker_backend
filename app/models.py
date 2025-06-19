from django.db import models
from user_profile.models import User

class Excercise(models.Model):
    name = models.CharField(max_length=100)
    muscle_group  = models.CharField(max_length=100)
    instructions = models.TextField()
    equipment = models.CharField(max_length=100, blank=True, null=True)

class Workout(models.Model):
    title = models.CharField(max_length=100)
    Description = models.TextField()
    excercises = models.ManyToManyField(Excercise, related_name='workouts')
    difficulty = models.CharField(max_length=50, choices=[
        ('easy', 'Easy'),
        ('medium', 'Medium'),
        ('hard', 'Hard'),], default='easy')
    duration = models.IntegerField(help_text="Duration in minutes")

class HealthMetric(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    metric_type = models.CharField(max_length=50, choices=[
        ('weight', 'Weight'),
        ('height', 'Height'),
        ('bmi', 'BMI'),
        ('body_fat', 'Body Fat Percentage'),], default='weight')
    value = models.DecimalField(max_digits=5, decimal_places=2)
    date_recorded = models.DateField(auto_now_add=True)

class FitnessEntry(models.Model):
    user_profile = models.ForeignKey(User, on_delete=models.CASCADE, related_name='fitness_entries')
    weight = models.DecimalField(max_digits=5, decimal_places=2)
    height = models.DecimalField(max_digits=4, decimal_places=2)
    bmi = models.DecimalField(max_digits=4, decimal_places=2) 
    body_fat = models.DecimalField(max_digits=4, decimal_places=2)
    date = models.DateField(auto_now_add=True)