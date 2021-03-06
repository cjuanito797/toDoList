from django.db import models
from django.conf import settings
# Create your models here.
class item (models.Model):
    task = models.CharField(max_length=30, blank=False)
     # urgency_levels = (("0", "low"), ("1", "normal"), ("2", "High"), ("3", "Critical"))
    # urgency_level = models.CharField(max_length=10, choices=urgency_levels, default="low")
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.task

class list (models.Model):
    item = models.ManyToManyField(item)
    name = models.CharField(max_length=15, blank=False)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE,
                             null=True)

    def delete(self, using=None, keep_parents=False):
        item.delete(self)


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,
                                on_delete=models.CASCADE,
                                unique=True)
    date_of_birth = models.DateField(blank=True, null=True)
    image = models.ImageField(upload_to='users/%Y/%m/%d',
                              blank=True)

