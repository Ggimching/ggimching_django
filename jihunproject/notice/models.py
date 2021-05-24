from django.db import models

# Create your models here.
class Notice(models.Model):
    title = models.CharField(max_length=200)
    writer = models.CharField(max_length=100)
    runner = models.IntegerField()
    pub_date = models.DateTimeField('date published')
    body = models.TextField()

    def __str__(self):
        return self.title

    def summary(self):             #자기 자신을 인자로 받는 함수 summary
        return self.body[:100]     #body를 리턴을 해주는데 100글자로 상한선을 정함
