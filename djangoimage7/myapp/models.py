from django.db import models

class imageupload(models.Model):
    name=models.CharField(max_length=18)
    age=models.IntegerField(null=True)
    image=models.ImageField(upload_to="images/")



