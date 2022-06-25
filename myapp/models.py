from django.db import models
import datetime
import os

def filepath(request, filename):
    old_filename = filename
    timeNow = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    filename = "%s%s" % (timeNow, old_filename)
    path = 'uploads/'
    return os.path.join(path , filename)

# Create your models here.
class Users(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    password = models.CharField(max_length=50)
    image = models.ImageField(upload_to=filepath)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table = 'Users'