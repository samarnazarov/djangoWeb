from django.db import models


class Workers(models.Model):
    username=models.CharField(max_length=50,null=False)
    tabelnumber=models.CharField(max_length=7,null=True)
    fullname=models.CharField(max_length=50,null=False)
    shortname=models.CharField(max_length=50,null=False)
    photo=models.CharField(max_length=10,null=False)
    phone=models.CharField(max_length=20, null=False)
    def __str__(self):
        return self.username

class FreeMessage(models.Model):
    message_theme=models.CharField(max_length=100,null=True)
    message_text=models.TextField(null=True,blank=True)
    reciever=models.ForeignKey(to=Workers,on_delete=models.CASCADE)
    date=models.DateTimeField(auto_now_add=True)
    file=models.FileField(upload_to='files/')

    def __str__(self):
        return self.message_theme