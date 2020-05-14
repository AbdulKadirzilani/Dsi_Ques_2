

#Use Object Relational Mapping ( ORM )

from django.db import models

class DatabaseField(models.Model):

     email = models.EmailField()
     password = models.CharField(max_length=50)




