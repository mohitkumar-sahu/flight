from django.db import models

# Create your models here.

class UserDetails(models.Model):
    name=models.CharField(max_length=50)
    age=models.IntegerField()
    address=models.CharField(max_length=150)

class Status(models.Model):
    title=models.CharField(max_length=50)
    sub_title=models.CharField(max_length=50)
    upload_time=models.DateTimeField( auto_now_add=True)
    description=models.TextField()
    status_pic=models.ImageField(upload_to='statuspic/', height_field=None, width_field=None, max_length=None)
    user=models.ForeignKey(UserDetails,related_name="users",on_delete=models.CASCADE)

    def __str__(self):
        return self.title
