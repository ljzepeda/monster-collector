from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User

RECORD = (
  ('W', 'Won'),
  ('L', 'Lost'),
  ('D', 'Completed'),
)

# Create your models here.

# Type Model (Many to Many)
class Type(models.Model):
  name = models.CharField(max_length=50)
  weakness = models.CharField(max_length=100)

  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return reverse('types_detail', kwargs={'pk': self.id})


# Monster Model (Main)
class Monster(models.Model):
  name = models.CharField(max_length=100)
  type = models.CharField(max_length=100)
  description = models.TextField(max_length=250)
  number = models.IntegerField()
  types = models.ManyToManyField(Type)
  user = models.ForeignKey(User, on_delete=models.CASCADE)

  def __str__(self):
    return f'{self.name} ({self.id})'

  def get_absolute_url(self):
    return reverse('detail', kwargs={'monster_id': self.id})
  
  def battle_for_today(self):
    return self.battle_set.filter(date=date.today()).count() >= 1

#Battle Model (One to Many)
class Battle(models.Model):
  date = models.DateField('battle date')
  record = models.CharField(
    max_length=1,
    choices=RECORD,
    default=RECORD[0][0]
  )
  # Create a monster_id FK
  monster = models.ForeignKey(
    Monster,
    on_delete=models.CASCADE
  )

  def __str__(self):
    return f"{self.get_record_display()} on {self.date}"

  class Meta:
    ordering = ['-date']