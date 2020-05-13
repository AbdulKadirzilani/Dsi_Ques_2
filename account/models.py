from django.db import models


# Use Object Relational Mapping ( ORM )


class DatabaseField(models.Model):

     email = models.EmailField()
     password = models.CharField(max_length=50)




