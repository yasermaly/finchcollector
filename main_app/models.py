from django.db import models
from django.urls import reverse


MEALS = (
    ('B', 'Breakfast'),
    ('L', 'Lunch'),
    ('D', 'Dinner')
)
# Create your models here.


class Finch(models.Model):
    name = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    description = models.CharField(max_length=250)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail', kwargs={'finch_id': self.id})


class Feeding(models.Model):
  date = models.DateField('feeding date')
  meal = models.CharField(max_length=1, choices=MEALS, default=MEALS[0][0])
  # Create a cat_id FK
  finch = models.ForeignKey(Finch, on_delete=models.CASCADE)

  def __str__(self):
      # Nice method for obtaining the friendly value of a Field.choice
    return f"{self.get_meal_display()} on {self.date}"

# Create your models here.
