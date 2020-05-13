from django.db import models

class Information(models.Model):


    email = models.EmailField()
    password = models.CharField(max_length=50)




