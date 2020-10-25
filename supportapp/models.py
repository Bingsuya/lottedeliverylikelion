from django.db import models
from mypageapp.models import User

# Create your models here.

class Qna(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    q_title = models.CharField(max_length = 200)
    q_content = models.TextField()
    q_type = models.CharField(max_length = 200)
    q_boxcode = models.CharField(max_length = 30)
    q_time = models.DateTimeField(auto_now = True)
    public = models.BooleanField(null=True)
    pic = models.ImageField(null = True, upload_to="%Y/%m/%d")
    today = models.IntegerField(default = '0')
    answers = models.TextField(null=True)

   
class Answer(models.Model):
    a_qna = models.ForeignKey(Qna, on_delete =models.CASCADE)
    a_title = models.CharField(max_length = 200)
    a_contents = models.TextField()
    a_time = models.DateTimeField(auto_now = True)