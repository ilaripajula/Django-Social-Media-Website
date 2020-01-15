from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.

# Creating a database action is done using a class, which uses the models class of Django. Certain inputs
# and data types require imports, and all variables and data need to call from the 'models' class.

class Post(models.Model):
    title = models.CharField(max_length=80)
    content = models.TextField()
    date = models.DateTimeField(default= timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

'''
1.After a class is created it needs to be migrated by first entering python manage.py makemigrations, and then python manage.py migrate.
Migrations are done to update the server side code with new instruction on how to process code.
2.The objects need to imported into the python file first, then they can be rendered to html using the object variable names determined in the 
object class

'''